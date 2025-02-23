from _typeshed import Incomplete
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel

class CTBRControl:
    DRONE_MODEL: Incomplete
    GRAVITY: Incomplete
    KF: Incomplete
    KM: Incomplete
    def __init__(self, drone_model: DroneModel, g: float = 9.8) -> None: ...
    control_counter: int
    def reset(self) -> None: ...
    def computeControlFromState(
        self, control_timestep, state, target_pos, target_rpy=..., target_vel=..., target_rpy_rates=...
    ): ...
    def computeControl(
        self,
        control_timestep,
        cur_pos,
        cur_quat,
        cur_vel,
        cur_ang_vel,
        target_pos,
        target_rpy=...,
        target_vel=...,
        target_rpy_rates=...,
    ): ...
    P_COEFF_FOR: Incomplete
    I_COEFF_FOR: Incomplete
    D_COEFF_FOR: Incomplete
    P_COEFF_TOR: Incomplete
    I_COEFF_TOR: Incomplete
    D_COEFF_TOR: Incomplete
    def setPIDCoefficients(
        self,
        p_coeff_pos: Incomplete | None = None,
        i_coeff_pos: Incomplete | None = None,
        d_coeff_pos: Incomplete | None = None,
        p_coeff_att: Incomplete | None = None,
        i_coeff_att: Incomplete | None = None,
        d_coeff_att: Incomplete | None = None,
    ) -> None: ...
