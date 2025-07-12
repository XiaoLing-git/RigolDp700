from enum import Enum


class Commands(Enum):
    pass


class GeneralCommands(Commands):
    Reset = "*RST"
    Self_Check = "*TST?"
    Information = "*IDN?"
    Service = "*OPT?"
