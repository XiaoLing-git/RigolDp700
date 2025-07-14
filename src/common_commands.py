from pathlib import Path

from .serial_write_read import SerialWriteRead
from .logger import device_logger

CURRENT_FILE_NAME = Path(__file__).stem


class GeneralCommandsConnection(SerialWriteRead):
    pass
