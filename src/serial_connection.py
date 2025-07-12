from pathlib import Path

import serial  # type: ignore[import-untyped]

from .models import RESPONSE_END_TAG
from .utils import logger

CURRENT_FILE_NAME = Path(__file__).stem


class SerialConnection:

    def __init__(
        self,
        port: str,
        baud: int = 9600,
        bytesize: int = serial.EIGHTBITS,
        stop_bits: float = serial.STOPBITS_ONE,
        parity: str = serial.PARITY_NONE,
        timeout: float = 3,
    ) -> None:
        self.__ser: serial.Serial = serial.Serial(
            port=port,
            baudrate=baud,
            bytesize=bytesize,
            parity=parity,
            stopbits=stop_bits,
            timeout=timeout,
        )

    @property
    def serial(self) -> serial.Serial:
        return self.__ser

    def read(self) -> bytes:
        response: bytes = self.__ser.read_until(RESPONSE_END_TAG.encode())
        logger.debug(
            f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Read: {response!r}"
        )
        return response

    def write(self, content: bytes):
        logger.debug(f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Send: {content!r}")
        self.__ser.flush()
        self.__ser.write(content)

    def disconnect(self) -> None:
        if self.__ser.is_open:
            self.__ser.close()
