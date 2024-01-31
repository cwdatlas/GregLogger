from pydantic import BaseModel
from datetime import date


class MachineLog(BaseModel):
    """
    BacktradeData is the parent of the family of models used to create backtrades
    child of BaseModel from Pydantic, so it can act similar to a dataclass while still being a parent to other classes
    """
    logged_time: date
    machine: str
    state: str
    message: str

    #@model_validator(mode='after')
    #def general_validation(self):
