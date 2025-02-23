from _typeshed import Incomplete
from gym_pybullet_drones.control.DSLPIDControl import DSLPIDControl as DSLPIDControl
from gym_pybullet_drones.envs.CtrlAviary import CtrlAviary as CtrlAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics
from gym_pybullet_drones.utils.Logger import Logger as Logger
from gym_pybullet_drones.utils.utils import str2bool as str2bool
from gym_pybullet_drones.utils.utils import sync as sync

DEFAULT_DRONE: Incomplete
DEFAULT_GUI: bool
DEFAULT_RECORD_VIDEO: bool
DEFAULT_SIMULATION_FREQ_HZ: int
DEFAULT_CONTROL_FREQ_HZ: int
DEFAULT_DURATION_SEC: int
DEFAULT_OUTPUT_FOLDER: str
DEFAULT_COLAB: bool

def run(
    drone=...,
    gui=...,
    record_video=...,
    simulation_freq_hz=...,
    control_freq_hz=...,
    duration_sec=...,
    output_folder=...,
    plot: bool = True,
    colab=...,
) -> None: ...
