from sys import platform as platform

import gymnasium as gym
from _typeshed import Incomplete
from gym_pybullet_drones.utils.enums import DroneModel as DroneModel
from gym_pybullet_drones.utils.enums import ImageType as ImageType
from gym_pybullet_drones.utils.enums import Physics as Physics

class BaseAviary(gym.Env):
    G: float
    RAD2DEG: Incomplete
    DEG2RAD: Incomplete
    CTRL_FREQ: Incomplete
    PYB_FREQ: Incomplete
    PYB_STEPS_PER_CTRL: Incomplete
    CTRL_TIMESTEP: Incomplete
    PYB_TIMESTEP: Incomplete
    NUM_DRONES: Incomplete
    NEIGHBOURHOOD_RADIUS: Incomplete
    DRONE_MODEL: Incomplete
    GUI: Incomplete
    RECORD: Incomplete
    PHYSICS: Incomplete
    OBSTACLES: Incomplete
    USER_DEBUG: Incomplete
    URDF: Incomplete
    OUTPUT_FOLDER: Incomplete
    GRAVITY: Incomplete
    HOVER_RPM: Incomplete
    MAX_RPM: Incomplete
    MAX_THRUST: Incomplete
    MAX_XY_TORQUE: Incomplete
    MAX_Z_TORQUE: Incomplete
    GND_EFF_H_CLIP: Incomplete
    ONBOARD_IMG_PATH: Incomplete
    VISION_ATTR: Incomplete
    IMG_RES: Incomplete
    IMG_FRAME_PER_SEC: int
    IMG_CAPTURE_FREQ: Incomplete
    rgb: Incomplete
    dep: Incomplete
    seg: Incomplete
    CLIENT: Incomplete
    SLIDERS: Incomplete
    INPUT_SWITCH: Incomplete
    VID_WIDTH: Incomplete
    VID_HEIGHT: Incomplete
    FRAME_PER_SEC: int
    CAPTURE_FREQ: Incomplete
    CAM_VIEW: Incomplete
    CAM_PRO: Incomplete
    INIT_XYZS: Incomplete
    INIT_RPYS: Incomplete
    action_space: Incomplete
    observation_space: Incomplete
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
        vision_attributes: bool = False,
        output_folder: str = "results",
    ) -> None: ...
    def reset(self, seed: int | None = None, options: dict | None = None): ...
    last_input_switch: Incomplete
    USE_GUI_RPM: Incomplete
    GUI_INPUT_TEXT: Incomplete
    last_clipped_action: Incomplete
    step_counter: Incomplete
    def step(self, action): ...
    first_render_call: bool
    def render(self, mode: str = "human", close: bool = False) -> None: ...
    def close(self) -> None: ...
    def getPyBulletClient(self): ...
    def getDroneIds(self): ...
