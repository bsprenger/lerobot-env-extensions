from dataclasses import dataclass, field
from typing import ClassVar

import gymnasium as gym
import numpy as np
import pybullet as p
from gym_pybullet_drones.utils.enums import ActionType, ObservationType
from gymnasium.envs.registration import register
from lerobot.common.constants import ACTION, OBS_ROBOT
from lerobot.common.envs.configs import EnvConfig
from lerobot.configs.types import FeatureType, PolicyFeature

_DEFAULT_FPS = 30


class PybulletDronesLeRobotWrapper(gym.Wrapper):
    metadata: ClassVar[dict] = {
        "render_fps": _DEFAULT_FPS,
        "render_modes": ["rgb_array"],
    }

    def __init__(
        self,
        ctrl_freq: int = _DEFAULT_FPS,
        render_mode="rgb_array",
        act: ActionType = ActionType.ONE_D_RPM,
        **kwargs,
    ):
        # Create base environment
        env = gym.make(
            "hover-aviary-v0",
            ctrl_freq=ctrl_freq,
            obs=ObservationType("kin"),
            act=act,
            **kwargs,
        )

        # Update metadata
        env.metadata["render_fps"] = ctrl_freq
        env.unwrapped.render_mode = render_mode
        super().__init__(env)
        self.metadata["render_fps"] = ctrl_freq

        # Observation and action space setup
        self.observation_space = gym.spaces.Dict({
            "agent_pos": gym.spaces.Box(
                low=self.observation_space.low.squeeze(0),
                high=self.observation_space.high.squeeze(0),
                dtype=self.observation_space.low.dtype,
            ),
        })
        self.action_space = gym.spaces.Box(
            low=self.action_space.low.squeeze(0),
            high=self.action_space.high.squeeze(0),
            dtype=self.action_space.low.dtype,
        )

        # Rendering setup
        self.render_width = 640
        self.render_height = 480

        # Camera setup for rendering
        self.camera_distance = 3
        self.camera_yaw = -30
        self.camera_pitch = -30
        self.camera_target = [0, 0, 0]

        # Set up camera matrices
        self.view_matrix = p.computeViewMatrixFromYawPitchRoll(
            distance=self.camera_distance,
            yaw=self.camera_yaw,
            pitch=self.camera_pitch,
            roll=0,
            cameraTargetPosition=self.camera_target,
            upAxisIndex=2,
            physicsClientId=self.env.unwrapped.CLIENT,
        )
        self.proj_matrix = p.computeProjectionMatrixFOV(
            fov=60.0, aspect=self.render_width / self.render_height, nearVal=0.1, farVal=1000.0
        )

    def observation(self, obs):
        obs = obs.squeeze(0)
        return {"agent_pos": obs}

    def step(self, action):
        action = action[None, ...]  # unsqueeze
        obs, reward, terminated, truncated, info = self.env.step(action)
        info["is_success"] = False  # Always False for now
        return self.observation(obs), reward, terminated, truncated, info

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        return self.observation(obs), info

    def render(self):
        if self.render_mode is None:
            return

        # Get camera image from PyBullet
        (_, _, rgb, _, _) = p.getCameraImage(
            width=self.render_width,
            height=self.render_height,
            viewMatrix=self.view_matrix,
            projectionMatrix=self.proj_matrix,
            shadow=1,
            renderer=p.ER_BULLET_HARDWARE_OPENGL,
            physicsClientId=self.env.unwrapped.CLIENT,
        )

        # Convert the RGB array to proper format (H, W, 3)
        rgb_array = np.array(rgb, dtype=np.uint8)
        rgb_array = rgb_array[:, :, :3]  # Remove alpha channel
        return rgb_array


register(
    id="gym_pybullet_drones/Hover-v0",
    entry_point="lerobot_env_extensions.gym_pybullet_drones:PybulletDronesLeRobotWrapper",
)


@EnvConfig.register_subclass("pybullet_drones")
@dataclass
class PybulletDronesEnv(EnvConfig):
    task: str = "hover"
    fps: int = 30
    render_mode: str = "rgb_array"

    act_type: ActionType = ActionType.ONE_D_RPM

    features: dict[str, PolicyFeature] = field(
        default_factory=lambda: {
            "action": PolicyFeature(type=FeatureType.ACTION, shape=()),
            "state": PolicyFeature(type=FeatureType.STATE, shape=()),
        }
    )
    features_map: dict[str, str] = field(
        default_factory=lambda: {
            "action": ACTION,
            "state": OBS_ROBOT,
        }
    )

    @property
    def gym_kwargs(self) -> dict:
        return {
            "ctrl_freq": self.fps,
            "max_episode_steps": 200,
            "render_mode": self.render_mode,
            "act": self.act_type,
        }

    def __post_init__(self):
        # Adjust action shape based on act_type
        if self.act_type == ActionType.ONE_D_RPM:
            action_shape = (1,)
        elif self.act_type == ActionType.RPM:
            action_shape = (4,)
        else:
            raise ValueError(f"Unsupported act_type: {self.act_type}")  # noqa: TRY003
        self.features["action"].shape = action_shape
        # there is a 0.5s action buffer in the observation and the state is 12-dimensional
        self.features["state"].shape = (self.fps // 2 * action_shape[0] + 12,)
