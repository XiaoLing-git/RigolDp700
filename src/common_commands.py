from pathlib import Path

from .commands import CommonCommands
from .errors import ChannelNotExistException
from .models import Channel, CurrentWorkStatusModel, ApplyStatusModel
from .serial_write_read import SerialWriteRead
from .logger import device_logger
from .utils import assert_channel_setup, assert_apply_setup

CURRENT_FILE_NAME = Path(__file__).stem


class CommonCommandsConnection(SerialWriteRead):

    def apply_status(self) -> ApplyStatusModel:
        self.write(CommonCommands.APPLY_STATUS)
        response: str = self.read()
        return ApplyStatusModel.parse_str(response)

    def apply_set(
        self, current: float, voltage: float, chl: str | Channel = Channel.ch1
    ) -> ApplyStatusModel:

        assert_channel_setup(chl)
        assert_apply_setup(current, voltage)

        if isinstance(chl, Channel):
            chl = chl.value

        cmd: str = f"{CommonCommands.APPLY_SETUP.value} {chl},{voltage},{current}"
        print(cmd)
        self.write(cmd)
        return self.apply_status()
        # return ApplyStatusModel.parse_str(response)

    def get_current_status(
        self, chl: str | Channel = Channel.ch1
    ) -> CurrentWorkStatusModel:

        assert_channel_setup(chl)

        self.write(CommonCommands.CURRENT_STATUS)
        response: str = self.read()
        return CurrentWorkStatusModel.parse_str(response)
