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
    CHANNEL_STATUS = ":OUTPut?"
    CHANNEL_SETUP = ":OUTPut"
    OCP_CHECK = ":OUTPut:OCP:ALAR?"
    OVP_CHECK = ":OUTPut:OVP:ALAR?"
