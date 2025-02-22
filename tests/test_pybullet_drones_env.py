import gymnasium as gym
import pytest
from gym_pybullet_drones.utils.enums import ActionType

from lerobot_env_extensions.gym_pybullet_drones import PybulletDronesEnv


def test_config_invalid_act_type():
    with pytest.raises(ValueError):
        PybulletDronesEnv(act_type="invalid")


def test_default_environment_creation():
    env = gym.make("gym_pybullet_drones/Hover-v0")
    env.close()


@pytest.mark.parametrize(
    "fps, act_type, expected_act_shape, expected_state_shape",
    [
        (30, ActionType.ONE_D_RPM, 1, 27),  # 30//2 * 1 + 12 = 27
        (30, ActionType.RPM, 4, 72),  # 30//2 * 4 + 12 = 72
        (60, ActionType.ONE_D_RPM, 1, 42),  # 60//2 * 1 + 12 = 42
        (60, ActionType.RPM, 4, 132),  # 60//2 * 4 + 12 = 132
    ],
)
def test_custom_environment_creation(fps, act_type, expected_act_shape, expected_state_shape):
    # test config creation
    config = PybulletDronesEnv(fps=fps, render_mode="rgb_array", act_type=act_type)
    assert config.task == "hover"
    assert config.fps == fps
    assert config.render_mode == "rgb_array"
    assert config.act_type == act_type
    assert config.features["action"].type == "ACTION"
    assert config.features["action"].shape == (expected_act_shape,)
    assert config.features["state"].shape == (expected_state_shape,)

    # test environment creation
    env = gym.make("gym_pybullet_drones/Hover-v0", **config.gym_kwargs)
    assert env.metadata["render_fps"] == fps
    assert env.render_mode == "rgb_array"
    assert env.action_space.shape == (expected_act_shape,)
    assert env.observation_space["agent_pos"].shape == (expected_state_shape,)
    env.close()
