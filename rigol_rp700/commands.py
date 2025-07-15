from enum import Enum


class Commands(Enum):
    """Base Command Class for device."""

    pass


class GeneralCommands(Commands):
    """
    General Command Class for device.
    Reset : reset device command
    Self_Check : make device self check command
    Information : get device information
    Service : get device supported services
    """

    Reset = "*RST"
    Self_Check = "*TST?"
    Information = "*IDN?"
    Service = "*OPT?"


class CommonCommands(Commands):
    """General Command Class for device."""

    APPLY_STATUS = ":APPLy?"
    APPLY_SETUP = ":APPLy"
    CURRENT_STATUS = "MEASure:ALL?"
    CHANNEL_STATUS = ":OUTPut?"
    CHANNEL_SETUP = ":OUTPut"

    OCP_STATUS = ":OUTPut:OCP?"
    OVP_STATUS = ":OUTPut:OVP?"

    OCP_ALARM = ":OUTPut:OCP:ALAR?"
    OVP_ALARM = ":OUTPut:OVP:ALAR?"

    OCP_CHECK = ":OUTPut:OCP:VALUE?"
    OVP_CHECK = ":OUTPut:OVP:VALUE?"

    OCP_CONTROL = ":OUTPut:OCP"
    OVP_CONTROL = ":OUTPut:OVP"

    OCP_SETUP = ":OUTPut:OCP:VALUE"
    OVP_SETUP = ":OUTPut:OVP:VALUE"

    OCP_CLEAR = ":OUTPut:OCP:CLEAR"
    OVP_CLEAR = ":OUTPut:OVP:CLEAR"
