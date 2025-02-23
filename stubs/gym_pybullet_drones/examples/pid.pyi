from datetime import datetime as datetime

from _typeshed import Incomplete
from gym_pybullet_drones.control.DSLPIDControl import DSLPIDControl as DSLPIDControl
from gym_pybullet_drones.envs.CtrlAviary import CtrlAviary as CtrlAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics
from gym_pybullet_drones.utils.Logger import Logger as Logger
from gym_pybullet_drones.utils.utils import str2bool as str2bool
from gym_pybullet_drones.utils.utils import sync as sync

DEFAULT_DRONES: Incomplete
DEFAULT_NUM_DRONES: int
DEFAULT_PHYSICS: Incomplete
DEFAULT_GUI: bool
DEFAULT_RECORD_VISION: bool
DEFAULT_PLOT: bool
DEFAULT_USER_DEBUG_GUI: bool
DEFAULT_OBSTACLES: bool
DEFAULT_SIMULATION_FREQ_HZ: int
DEFAULT_CONTROL_FREQ_HZ: int
DEFAULT_DURATION_SEC: int
DEFAULT_OUTPUT_FOLDER: str
DEFAULT_COLAB: bool

def run(
    drone=...,
    num_drones=...,
    physics=...,
    gui=...,
    record_video=...,
    plot=...,
    user_debug_gui=...,
    obstacles=...,
    simulation_freq_hz=...,
    control_freq_hz=...,
    duration_sec=...,
    output_folder=...,
    colab=...,
) -> None: ...
