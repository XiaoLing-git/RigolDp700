from .errors import ApplySetupError, ChannelNotExistException
from .logger import device_logger
from .models import MAX_CURRENT, MAX_VOLTAGE, MIN_CURRENT, MIN_VOLTAGE, Channel


def assert_channel_setup(chl: str | Channel) -> str:
    """
    Assert that channel input is supported,
    :param chl: str or Channel
    :return: if supported return str, if no raise ChannelNotExistException
    """
    if isinstance(chl, Channel) or chl in [i.value for i in list(Channel)]:
        if isinstance(chl, Channel):
            chl = chl.value
        return chl
    error_msg = f"{chl} is not currently supported"
    device_logger.warn(error_msg)
    raise ChannelNotExistException(error_msg)


def assert_apply_setup(current: float, voltage: float) -> None:
    """
    Setting value verification
    :param current: 0 < value 5.3 A
    :param voltage: 0 < value 32 V
    :return: if everything is ok return None otherwise raise ApplySetupError
    """
    if MIN_CURRENT <= current <= MAX_CURRENT and MIN_VOLTAGE < voltage <= MAX_VOLTAGE:
        return
    error_msg = (
        f"The apply setup value must be within the threshold range"
        f"{MIN_CURRENT}<=Current<={MAX_CURRENT} | {MIN_VOLTAGE}<=Voltage<={MAX_VOLTAGE}"
    )
    device_logger.warn(error_msg)
    raise ApplySetupError(error_msg)


def assert_ocp_setup(current: float) -> None:
    """
    Setting value verification
    :param current: 0 < value 5.3 A
    :return: if everything is ok return None otherwise raise ApplySetupError
    """
    if MIN_CURRENT + 0.01 <= current <= MAX_CURRENT - 0.01:
        return
    error_msg = (
        f"The ocp setup value must be within the threshold range "
        f"{MIN_CURRENT} <= Current <= {MAX_CURRENT}"
    )
    device_logger.warn(error_msg)
    raise ApplySetupError(error_msg)


def assert_ovp_setup(voltage: float) -> None:
    """
    Setting value verification
    :param voltage: 0 < value 32 V
    :return: if everything is ok return None otherwise raise ApplySetupError
    """
    if MIN_VOLTAGE + 0.01 <= voltage <= MAX_VOLTAGE - 0.01:
        return
    error_msg = (
        f"The ocp setup value must be within the threshold range "
        f"{MIN_VOLTAGE + 0.01} <= Voltage <= {MAX_VOLTAGE - 0.01}"
    )
    device_logger.warn(error_msg)
    raise ApplySetupError(error_msg)
