from _typeshed import Incomplete
from gym_pybullet_drones.envs.BaseAviary import BaseAviary as BaseAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics

class CtrlAviary(BaseAviary):
    def __init__(
        self,
        drone_model: DroneModel = ...,
        num_drones: int = 1,
        neighbourhood_radius: float = ...,
        initial_xyzs: Incomplete | None = None,
        initial_rpys: Incomplete | None = None,
        physics: Physics = ...,
        pyb_freq: int = 240,
        ctrl_freq: int = 240,
        gui: bool = False,
        record: bool = False,
        obstacles: bool = False,
        user_debug_gui: bool = True,
        output_folder: str = "results",
    ) -> None: ...
