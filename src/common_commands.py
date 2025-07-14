import time
from pathlib import Path

from .commands import CommonCommands
from .errors import ChannelNotExistException
from .models import (
    Channel,
    CurrentWorkStatusModel,
    ApplyStatusModel,
    WorkStatus,
    AlarmStatus,
)
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

        chl = assert_channel_setup(chl)
        assert_apply_setup(current, voltage)

        cmd: str = f"{CommonCommands.APPLY_SETUP.value} {chl},{voltage},{current}"
        print(cmd)
        self.write(cmd)
        return self.apply_status()
        # return ApplyStatusModel.parse_str(response)

    def current_status(
        self, chl: str | Channel = Channel.ch1
    ) -> CurrentWorkStatusModel:

        assert_channel_setup(chl)

        self.write(CommonCommands.CURRENT_STATUS)
        response: str = self.read()
        return CurrentWorkStatusModel.parse_str(response)

    def get_channel_status(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        chl = assert_channel_setup(chl)
        cmd: str = f"{CommonCommands.CHANNEL_STATUS.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            WorkStatus.ON if response.upper() in WorkStatus.ON.value else WorkStatus.OFF
        )

    def set_channel_status(
        self, chl: str | Channel = Channel.ch1, setup: WorkStatus = WorkStatus.OFF
    ) -> WorkStatus:

        if setup not in list(WorkStatus):
            raise ValueError(
                f"Chanel {chl} status setup Error, {setup} not in {list(WorkStatus)}"
            )
        chl = assert_channel_setup(chl)
        cmd: str = f"{CommonCommands.CHANNEL_SETUP.value} {chl},{setup.value}"
        self.write(cmd)
        return self.get_channel_status(chl)

    def get_alarm_info(self, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CHECK.value} {chl}"
        self.write(cmd)
        ocp: str = self.read()
        cmd = f"{CommonCommands.OVP_CHECK.value} {chl}"
        self.write(cmd)
        ovp: str = self.read()
        return {
            "OVP_ALARM": (
                AlarmStatus.Yes
                if ovp.upper() in AlarmStatus.Yes.value
                else AlarmStatus.No
            ),
            "OCP_ALARM": (
                AlarmStatus.Yes
                if ocp.upper() in AlarmStatus.Yes.value
                else AlarmStatus.No
            ),
        }
