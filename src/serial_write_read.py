from pathlib import Path

import serial  # type: ignore[import-untyped]

from .errors import SerialConnectError
from .models import COMMAND_END_TAG
from .serial_connection import SerialConnection
from .utils import logger

CURRENT_FILE_NAME = Path(__file__).stem


class SerialWriteRead:
    def __init__(
        self,
        port: str,
        baud: int = 9600,
        data_bits: int = serial.EIGHTBITS,
        stop_bits: float = serial.STOPBITS_ONE,
        parity: str = serial.PARITY_NONE,
        timeout: float = 3,
    ) -> None:
        self.__port = port
        self.__baud = baud
        self.__data_bits = data_bits
        self.__stop_bits = stop_bits
        self.__parity = parity
        self.__timeout = timeout
        self.__ser: SerialConnection | None = None

    @property
    def serial(self) -> SerialConnection | None:
        return self.__ser

    def connect(self) -> None:
        try:
            if self.serial is None:
                logger.debug(f"{self.__class__.__name__} Serial Port Connecting~~~")
                self.__ser = SerialConnection(
                    port=self.__port,
                    baud=self.__baud,
                    bytesize=self.__data_bits,
                    parity=self.__parity,
                    stop_bits=self.__stop_bits,
                    timeout=self.__timeout,
                )
                logger.debug(
                    f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Connected Already"
                )
            elif not self.serial.serial.is_open:
                logger.debug(
                    f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Closed Already, Try Open It Again"
                )
                self.serial.serial.open()
                logger.debug(
                    f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Connected Already"
                )
            else:
                logger.debug(
                    f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Connected Already"
                )
        except Exception as e:
            logger.warn(
                f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Connection Error, Msg = {e}"
            )
            raise SerialConnectError(f"Connection Error, Msg = {e}")

    def disconnect(self) -> None:
        if self.serial is not None and self.serial.serial.is_open:
            logger.debug(
                f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Disconnecting~~~"
            )
            self.serial.disconnect()
        logger.debug(
            f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Serial Port Disconnected Already"
        )

    def read(self) -> str:
        if self.serial is not None and self.serial.serial.is_open:
            return self.serial.read().decode()
        logger.warn(
            f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Try Read Data Before Connected"
        )
        raise SerialConnectError("Try Read Data Before Connected")

    def write(self, cmd: str) -> None:
        cmd = cmd if cmd.endswith(COMMAND_END_TAG) else cmd + COMMAND_END_TAG
        if self.serial is not None and self.serial.serial.is_open:
            self.serial.write(cmd.encode())
            return
        logger.warn(
            f"{CURRENT_FILE_NAME}.{self.__class__.__name__} Try Read Data Before Connected"
        )
        raise SerialConnectError("Try Write Data Before Connected")
