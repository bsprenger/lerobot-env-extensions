from _typeshed import Incomplete
from gym_pybullet_drones.envs.BaseAviary import BaseAviary as BaseAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics

class CFAviary(BaseAviary):
    ACTION_DELAY: int
    SENSOR_DELAY: int
    STATE_DELAY: int
    CONTROLLER: str
    GYRO_LPF_CUTOFF_FREQ: int
    ACCEL_LPF_CUTOFF_FREQ: int
    QUAD_FORMATION_X: bool
    MOTOR_SET_ENABLE: bool
    RAD_TO_DEG: Incomplete
    firmware_freq: Incomplete
    ctrl_freq: Incomplete
    PWM2RPM_SCALE: float
    PWM2RPM_CONST: float
    MIN_PWM: int
    MAX_PWM: int
    verbose: Incomplete
    def __init__(
        self,
        drone_model: DroneModel = ...,
        num_drones: int = 1,
        neighbourhood_radius: float = ...,
        initial_xyzs: Incomplete | None = None,
        initial_rpys: Incomplete | None = None,
        physics: Physics = ...,
        pyb_freq: int = 500,
        ctrl_freq: int = 25,
        gui: bool = False,
        record: bool = False,
        obstacles: bool = False,
        user_debug_gui: bool = True,
        output_folder: str = "results",
        verbose: bool = False,
    ) -> None: ...
    prev_rpy: Incomplete
    prev_vel: Incomplete
    state_history: Incomplete
    sensor_history: Incomplete
    action_history: Incomplete
    first_motor_killed_print: bool
    action: Incomplete
    def step(self, i): ...
    def sendFullStateCmd(self, pos, vel, acc, yaw, rpy_rate, timestep) -> None: ...
    def sendTakeoffCmd(self, height, duration) -> None: ...
    def sendTakeoffYawCmd(self, height, duration, yaw) -> None: ...
    def sendTakeoffVelCmd(self, height, vel, relative) -> None: ...
    def sendLandCmd(self, height, duration) -> None: ...
    def sendLandYawCmd(self, height, duration, yaw) -> None: ...
    def sendLandVelCmd(self, height, vel, relative) -> None: ...
    def sendStopCmd(self) -> None: ...
    def sendGotoCmd(self, pos, yaw, duration_s, relative) -> None: ...
    def notifySetpointStop(self) -> None: ...
    BRUSHED: bool
    SUPPLY_VOLTAGE: int
