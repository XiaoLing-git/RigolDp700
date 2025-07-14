from pathlib import Path

from .commands import CommonCommands
from .errors import ChannelNotExistException
from .models import Channel, CurrentWorkStatusModel
from .serial_write_read import SerialWriteRead
from .logger import device_logger

CURRENT_FILE_NAME = Path(__file__).stem


class CommonCommandsConnection(SerialWriteRead):
    def get_current_status(
        self, chl: str | Channel = Channel.ch1
    ) -> CurrentWorkStatusModel:
        if isinstance(chl, Channel) or chl in [i.value for i in list(Channel)]:
            self.write(CommonCommands.CURRENT_STATUS)
            response: str = self.read()
            return CurrentWorkStatusModel.parse_str(response)
        error_msg = f"{chl} is not currently supported"
        device_logger.warn(error_msg)
        raise ChannelNotExistException(error_msg)
