from dataclasses import dataclass, field
from typing import Any

import gymnasium as gym
import numpy as np
from gymnasium.envs.registration import register
from gymnasium.spaces import Dict
from lerobot.common.constants import ACTION, OBS_ROBOT
from lerobot.common.envs.configs import EnvConfig
from lerobot.configs.types import FeatureType, PolicyFeature


class PendulumDictWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env) -> None:
        super().__init__(env)
        self.observation_space = Dict({"agent_pos": self.env.observation_space})

    def observation(self, obs: np.ndarray) -> dict[str, np.ndarray]:
        return {"agent_pos": obs}

    def step(self, action: np.ndarray) -> tuple[dict, float, bool, bool, dict]:
        obs, reward, terminated, truncated, info = self.env.step(action)
        info["is_success"] = False  # Always False for now
        return self.observation(obs), float(reward), terminated, truncated, info

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[dict, dict]:
        obs, info = self.env.reset(seed=seed, options=options)
        return self.observation(obs), info


def make_pendulum_dict(**kwargs: dict) -> PendulumDictWrapper:
    env = gym.make("Pendulum-v1", **kwargs)  # type: ignore[arg-type] # TODO: Fix this
    return PendulumDictWrapper(env)


register(
    id="gym_pendulum_v1/Pendulum-v1",
    entry_point=make_pendulum_dict,
)


@EnvConfig.register_subclass("pendulum_v1")
@dataclass
class PendulumEnv(EnvConfig):
    task: str = "Pendulum-v1"
    fps: int = 30
    episode_length: int = 200
    obs_type: str = "state"
    render_mode: str = "rgb_array"
    features: dict[str, PolicyFeature] = field(
        default_factory=lambda: {
            "action": PolicyFeature(type=FeatureType.ACTION, shape=(1,)),
            "state": PolicyFeature(type=FeatureType.STATE, shape=(3,)),
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
            "render_mode": self.render_mode,
            "max_episode_steps": self.episode_length,
        }
