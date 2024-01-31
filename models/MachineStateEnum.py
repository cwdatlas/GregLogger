from enum import Enum


class MachineStateEnum(Enum):
    idle: str
    running: str
    stopped: str
    broken: str
