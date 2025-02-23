from enum import Enum

class DroneModel(Enum):
    CF2X = "cf2x"
    CF2P = "cf2p"
    RACE = "racer"

class Physics(Enum):
    PYB = "pyb"
    DYN = "dyn"
    PYB_GND = "pyb_gnd"
    PYB_DRAG = "pyb_drag"
    PYB_DW = "pyb_dw"
    PYB_GND_DRAG_DW = "pyb_gnd_drag_dw"

class ImageType(Enum):
    RGB = 0
    DEP = 1
    SEG = 2
    BW = 3

class ActionType(Enum):
    RPM = "rpm"
    PID = "pid"
    VEL = "vel"
    ONE_D_RPM = "one_d_rpm"
    ONE_D_PID = "one_d_pid"

class ObservationType(Enum):
    KIN = "kin"
    RGB = "rgb"
