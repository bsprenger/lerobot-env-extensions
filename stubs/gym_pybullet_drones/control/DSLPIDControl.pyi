from _typeshed import Incomplete
from gym_pybullet_drones.control.BaseControl import BaseControl as BaseControl
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel

class DSLPIDControl(BaseControl):
    P_COEFF_FOR: Incomplete
    I_COEFF_FOR: Incomplete
    D_COEFF_FOR: Incomplete
    P_COEFF_TOR: Incomplete
    I_COEFF_TOR: Incomplete
    D_COEFF_TOR: Incomplete
    PWM2RPM_SCALE: float
    PWM2RPM_CONST: float
    MIN_PWM: int
    MAX_PWM: int
    MIXER_MATRIX: Incomplete
    def __init__(self, drone_model: DroneModel, g: float = 9.8) -> None: ...
    last_rpy: Incomplete
    last_pos_e: Incomplete
    integral_pos_e: Incomplete
    last_rpy_e: Incomplete
    integral_rpy_e: Incomplete
    def reset(self) -> None: ...
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
