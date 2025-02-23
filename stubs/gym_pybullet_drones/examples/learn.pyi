from _typeshed import Incomplete
from gym_pybullet_drones.envs.HoverAviary import HoverAviary as HoverAviary
from gym_pybullet_drones.envs.MultiHoverAviary import MultiHoverAviary as MultiHoverAviary
from gym_pybullet_drones.utils.enums import ActionType as ActionType
from gym_pybullet_drones.utils.enums import ObservationType as ObservationType
from gym_pybullet_drones.utils.Logger import Logger as Logger
from gym_pybullet_drones.utils.utils import str2bool as str2bool
from gym_pybullet_drones.utils.utils import sync as sync

DEFAULT_GUI: bool
DEFAULT_RECORD_VIDEO: bool
DEFAULT_OUTPUT_FOLDER: str
DEFAULT_COLAB: bool
DEFAULT_OBS: Incomplete
DEFAULT_ACT: Incomplete
DEFAULT_AGENTS: int
DEFAULT_MA: bool

def run(
    multiagent=..., output_folder=..., gui=..., plot: bool = True, colab=..., record_video=..., local: bool = True
) -> None: ...
