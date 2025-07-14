import logging

from src.common_commands import CommonCommandsConnection
from src.driver import Driver
from src.general_commands import GeneralCommandsConnection
from src.models import Channel, WorkStatus
from src.serial_connection import SerialConnection
from src.serial_write_read import SerialWriteRead

if __name__ == '__main__':

    # logger.setLevel(logging.DEBUG)

    ser = Driver(port="COM7")
    ser.connect()
    res = ser.apply_status()
    print(res)

    res = ser.apply_set(voltage=10,current=3,chl="CH1")
    print(res)
    res = ser.get_channel_status()
    print(res)
    res = ser.set_channel_status(chl="CH1",setup=WorkStatus.OFF)
    print(res)
    res = ser.current_status(chl="CH1")
    print(res)

    res = ser.get_alarm_info(chl="CH1")
    print(res)