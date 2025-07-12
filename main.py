import logging

from src.serial_connection import SerialConnection
from src.serial_write_read import SerialWriteRead
from src.utils import logger

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)

    ser = SerialWriteRead(port="COM7")
    ser.connect()
    ser.write("*oPT?")
    res =  ser.read()

    ser.disconnect()

    ser.connect()
    ser.write("*oPT?")
    ser.read()