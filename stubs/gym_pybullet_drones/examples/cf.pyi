from _typeshed import Incomplete
from gym_pybullet_drones.control.CTBRControl import CTBRControl as CTBRControl
from gym_pybullet_drones.envs.CFAviary import CFAviary as CFAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics
from gym_pybullet_drones.utils.Logger import Logger as Logger
from gym_pybullet_drones.utils.utils import str2bool as str2bool
from gym_pybullet_drones.utils.utils import sync as sync
from transforms3d.quaternions import mat2quat as mat2quat
from transforms3d.quaternions import qconjugate as qconjugate
from transforms3d.quaternions import qmult as qmult
from transforms3d.quaternions import rotate_vector as rotate_vector
from transforms3d.utils import normalized_vector as normalized_vector

DEFAULT_DRONES: Incomplete
DEFAULT_PHYSICS: Incomplete
DEFAULT_GUI: bool
DEFAULT_PLOT: bool
DEFAULT_USER_DEBUG_GUI: bool
DEFAULT_SIMULATION_FREQ_HZ: int
DEFAULT_CONTROL_FREQ_HZ: int
DEFAULT_OUTPUT_FOLDER: str
NUM_DRONES: int
INIT_XYZ: Incomplete
INIT_RPY: Incomplete

def run(
    drone=...,
    physics=...,
    gui=...,
    plot=...,
    user_debug_gui=...,
    simulation_freq_hz=...,
    control_freq_hz=...,
    output_folder=...,
) -> None: ...
