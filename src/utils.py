from .errors import ChannelNotExistException
from .models import Channel, MAX_CURRENT, MIN_CURRENT, MIN_VOLTAGE, MAX_VOLTAGE
from .logger import device_logger


def assert_channel_setup(chl: str | Channel) -> str:
    if isinstance(chl, Channel) or chl in [i.value for i in list(Channel)]:
        if isinstance(chl, Channel):
            chl = chl.value
        return chl
    error_msg = f"{chl} is not currently supported"
    device_logger.warn(error_msg)
    raise ChannelNotExistException(error_msg)


def assert_apply_setup(current: float, voltage: float):
    if MIN_CURRENT <= current <= MAX_CURRENT and MIN_VOLTAGE < voltage <= MAX_VOLTAGE:
        return
    error_msg = (
        f"The apply setup value must be within the threshold range"
        f"{MIN_CURRENT}<=Current<={MAX_CURRENT} | {MIN_VOLTAGE}<=Voltage<={MAX_VOLTAGE}"
    )
    device_logger.warn(error_msg)
    raise ChannelNotExistException(error_msg)


def assert_ocp_setup(current: float):
    if MIN_CURRENT + 0.01 <= current <= MAX_CURRENT - 0.01:
        return
    error_msg = (
        f"The ocp setup value must be within the threshold range"
        f"{MIN_CURRENT}<=Current<={MAX_CURRENT}"
    )
    device_logger.warn(error_msg)
    raise ChannelNotExistException(error_msg)


def assert_ovp_setup(current: float):
    if MIN_VOLTAGE + 0.01 <= current <= MAX_VOLTAGE - 0.01:
        return
    error_msg = (
        f"The ocp setup value must be within the threshold range"
        f"{MIN_CURRENT}<=Voltage<={MAX_CURRENT}"
    )
    device_logger.warn(error_msg)
    raise ChannelNotExistException(error_msg)
