from _typeshed import Incomplete

class Logger:
    COLAB: Incomplete
    OUTPUT_FOLDER: Incomplete
    LOGGING_FREQ_HZ: Incomplete
    NUM_DRONES: Incomplete
    PREALLOCATED_ARRAYS: Incomplete
    counters: Incomplete
    timestamps: Incomplete
    states: Incomplete
    controls: Incomplete
    def __init__(
        self,
        logging_freq_hz: int,
        output_folder: str = "results",
        num_drones: int = 1,
        duration_sec: int = 0,
        colab: bool = False,
    ) -> None: ...
    def log(self, drone: int, timestamp, state, control=...): ...
    def save(self) -> None: ...
    def save_as_csv(self, comment: str = ""): ...
    def plot(self, pwm: bool = False) -> None: ...
