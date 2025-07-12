import logging

from src.general_commands import GeneralCommandsConnection
from src.serial_connection import SerialConnection
from src.serial_write_read import SerialWriteRead
from src.utils import logger

if __name__ == '__main__':

    # logger.setLevel(logging.DEBUG)

    ser = GeneralCommandsConnection(port="COM7")
    ser.connect()
    res = ser.get_work_status().model_dump_json()
    print(res)