from _typeshed import Incomplete
from gym_pybullet_drones.envs.BaseRLAviary import BaseRLAviary as BaseRLAviary
from gym_pybullet_drones.utils.enums import ActionType as ActionType
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import ObservationType as ObservationType
from gym_pybullet_drones.utils.enums import Physics as Physics

class HoverAviary(BaseRLAviary):
    TARGET_POS: Incomplete
    EPISODE_LEN_SEC: int
    def __init__(
        self,
        drone_model: DroneModel = ...,
        initial_xyzs: Incomplete | None = None,
        initial_rpys: Incomplete | None = None,
        physics: Physics = ...,
        pyb_freq: int = 240,
        ctrl_freq: int = 30,
        gui: bool = False,
        record: bool = False,
        obs: ObservationType = ...,
        act: ActionType = ...,
    ) -> None: ...
