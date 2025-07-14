from enum import Enum


class Commands(Enum):
    pass


class GeneralCommands(Commands):
    Reset = "*RST"
    Self_Check = "*TST?"
    Information = "*IDN?"
    Service = "*OPT?"


class CommonCommands(Commands):

    APPLY_STATUS = ":APPLy?"
    APPLY_SETUP = ":APPLy"
    CURRENT_STATUS = "MEASure:ALL?"
