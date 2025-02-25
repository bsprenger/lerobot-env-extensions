from dataclasses import dataclass, field
from typing import Any, ClassVar, cast

import gymnasium as gym
import numpy as np
import pybullet as p
from gym_pybullet_drones.envs import HoverAviary
from gym_pybullet_drones.utils.enums import ActionType, ObservationType
from gymnasium import spaces
from gymnasium.core import RenderFrame
from gymnasium.envs.registration import register
from lerobot.common.constants import ACTION, OBS_ROBOT
from lerobot.common.envs.configs import EnvConfig
from lerobot.configs.types import FeatureType, PolicyFeature

_DEFAULT_FPS: int = 30


class PybulletDronesLeRobotWrapper(HoverAviary):
    metadata: ClassVar[dict[str, Any]] = {  # type: ignore[misc]
        "render_fps": _DEFAULT_FPS,
        "render_modes": ["rgb_array"],
    }

    observation_space: gym.spaces.Dict
    action_space: gym.spaces.Box
    render_mode: str | None

    def __init__(
        self,
        ctrl_freq: int = _DEFAULT_FPS,
        act: ActionType = ActionType.ONE_D_RPM,
        render_mode: str = "rgb_array",
    ) -> None:
        super().__init__(
            ctrl_freq=ctrl_freq,
            obs=ObservationType("kin"),
            act=act,
        )

        # Update metadata
        self.metadata["render_fps"] = ctrl_freq
        self.render_mode = render_mode

        # Observation and action space setup
        # Squeeze because we only support one drone for now
        base_obs_space = cast(spaces.Box, self.observation_space)
        base_act_space = cast(spaces.Box, self.action_space)
        self.observation_space = gym.spaces.Dict({
            "agent_pos": gym.spaces.Box(
                low=base_obs_space.low.squeeze(0),
                high=base_obs_space.high.squeeze(0),
                dtype=np.float32,
            ),
        })
        self.action_space = gym.spaces.Box(
            low=base_act_space.low.squeeze(0),
            high=base_act_space.high.squeeze(0),
            dtype=np.float32,
        )

        # Rendering setup
        self.render_width = 640
        self.render_height = 480

        # Camera setup for rendering
        self.camera_distance = 3
        self.camera_yaw = -30
        self.camera_pitch = -30
        self.camera_target = [0.0, 0.0, 0.0]

        # Set up camera matrices
        self.view_matrix = p.computeViewMatrixFromYawPitchRoll(
            distance=self.camera_distance,
            yaw=self.camera_yaw,
            pitch=self.camera_pitch,
            roll=0,
            cameraTargetPosition=self.camera_target,
            upAxisIndex=2,
            physicsClientId=self.CLIENT,
        )
        self.proj_matrix = p.computeProjectionMatrixFOV(
            fov=60.0, aspect=self.render_width / self.render_height, nearVal=0.1, farVal=1000.0
        )

    def _process_observation(self, obs: np.ndarray) -> dict:
        return {"agent_pos": obs.squeeze(0)}  # Squeeze because we only support one drone for now

    def step(self, action: np.ndarray) -> tuple[dict, float, bool, bool, dict]:
        action = action[None, ...]  # unsqueeze
        obs, reward, terminated, truncated, info = super().step(action)
        info["is_success"] = False  # Always False for now
        return self._process_observation(obs), reward, terminated, truncated, info

    def reset(
        self,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[dict, dict]:
        obs, info = super().reset(seed=seed, options=options)  # type: ignore[arg-type]
        return self._process_observation(obs), info

    def render(self) -> RenderFrame | list[RenderFrame] | None:  # type: ignore[override]
        """Render the environment."""
        if self.render_mode is None:
            return None

        # Get camera image from PyBullet
        (_, _, rgb, _, _) = p.getCameraImage(
            width=self.render_width,
            height=self.render_height,
            viewMatrix=self.view_matrix,
            projectionMatrix=self.proj_matrix,
            shadow=1,
            renderer=p.ER_BULLET_HARDWARE_OPENGL,
            physicsClientId=self.CLIENT,
        )

        # Convert the RGB array to proper format (H, W, 3)
        rgb_array = np.array(rgb, dtype=np.uint8)
        rgb_array = rgb_array[:, :, :3]  # Remove alpha channel
        return rgb_array  # type: ignore[return-value] # numpy array is compatible with RenderFrame


register(
    id="gym_pybullet_drones/Hover-v0",
    entry_point="lerobot_env_extensions.gym_pybullet_drones:PybulletDronesLeRobotWrapper",
)


@EnvConfig.register_subclass("pybullet_drones")
@dataclass
class PybulletDronesEnv(EnvConfig):
    task: str = "hover"
    fps: int = 30
    episode_length: int = 200
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
            "max_episode_steps": self.episode_length,
            "render_mode": self.render_mode,
            "act": self.act_type,
        }

    def __post_init__(self) -> None:
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
