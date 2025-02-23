from _typeshed import Incomplete
from gym_pybullet_drones.control.DSLPIDControl import DSLPIDControl as DSLPIDControl
from gym_pybullet_drones.envs.BaseAviary import BaseAviary as BaseAviary
from gym_pybullet_drones.utils.enums import ActionType as ActionType
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import ImageType as ImageType
from gym_pybullet_drones.utils.enums import ObservationType as ObservationType
from gym_pybullet_drones.utils.enums import Physics as Physics

class BaseRLAviary(BaseAviary):
    ACTION_BUFFER_SIZE: Incomplete
    action_buffer: Incomplete
    OBS_TYPE: Incomplete
    ACT_TYPE: Incomplete
    ctrl: Incomplete
    SPEED_LIMIT: Incomplete
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
        obs: ObservationType = ...,
        act: ActionType = ...,
    ) -> None: ...
