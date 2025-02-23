from _typeshed import Incomplete
from gym_pybullet_drones.envs.BaseAviary import BaseAviary as BaseAviary
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import Physics as Physics

BASE_PORT_PWM: int
BASE_PORT_STATE: int
BASE_PORT_RC: int

class BetaAviary(BaseAviary):
    UDP_IP: Incomplete
    ARM_TIME: int
    TRAJ_TIME: float
    sock: Incomplete
    sock_pwm: Incomplete
    beta_action: Incomplete
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
        udp_ip: str = "127.0.0.1",
    ) -> None: ...
    def step(self, action, i): ...
    def ctbr2beta(self, thrust, roll, pitch, yaw): ...
