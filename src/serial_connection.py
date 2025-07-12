import serial  # type: ignore[import-untyped]
from serial import Serial


class SerialConnection:

    def __init__(
        self,
        port: str,
        baud: int = 9600,
        data_bits: int = serial.EIGHTBITS,
        stop_bits: float = serial.STOPBITS_ONE,
        parity: str = serial.PARITY_NONE,
        timeout: float = 2,
    ):
        self.__port = port
        self.__baud = baud
        self.__data_bits = data_bits
        self.__stop_bits = stop_bits
        self.__parity = parity
        self.__timeout = timeout
        self.__ser: Serial = Serial(
            port=self.__port,
            baudrate=self.__baud,
            bytesize=self.__data_bits,
            parity=self.__parity,
            stopbits=self.__stop_bits,
            timeout=self.__timeout,
        )

    def disconnect(self):
        if self.__ser.is_open:
            self.__ser.close()
