import time
from pathlib import Path

from .commands import CommonCommands
from .errors import ChannelNotExistException, ClearAlarmException
from .models import (
    Channel,
    CurrentWorkStatusModel,
    ApplyStatusModel,
    WorkStatus,
    AlarmStatus,
    OP_INFO,
)
from .serial_write_read import SerialWriteRead
from .logger import device_logger, serial_write_read_logger
from .utils import (
    assert_channel_setup,
    assert_apply_setup,
    assert_ocp_setup,
    assert_ovp_setup,
)

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

    def get_ocp_alarm(self, chl: str | Channel = Channel.ch1) -> AlarmStatus:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_ALARM.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            AlarmStatus.Yes
            if response.upper() in AlarmStatus.Yes.value
            else AlarmStatus.No
        )

    def get_ovp_alarm(self, chl: str | Channel = Channel.ch1) -> AlarmStatus:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_ALARM.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            AlarmStatus.Yes
            if response.upper() in AlarmStatus.Yes.value
            else AlarmStatus.No
        )

    def get_ocp_status(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_STATUS.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            WorkStatus.ON if response.upper() in WorkStatus.ON.value else WorkStatus.OFF
        )

    def get_ovp_status(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_STATUS.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            WorkStatus.ON if response.upper() in WorkStatus.ON.value else WorkStatus.OFF
        )

    def get_ocp_value(self, chl: str | Channel = Channel.ch1) -> float:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CHECK.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return float(response)

    def get_ovp_value(self, chl: str | Channel = Channel.ch1) -> float:
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CHECK.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return float(response)

    def get_op_info(self, chl: str | Channel = Channel.ch1) -> OP_INFO:
        return {
            "ocp": {
                "status": self.get_ocp_status(chl),
                "alarm": self.get_ocp_alarm(chl),
                "value": self.get_ocp_value(),
            },
            "ovp": {
                "status": self.get_ovp_status(chl),
                "alarm": self.get_ovp_alarm(chl),
                "value": self.get_ovp_value(),
            },
        }

    def ocp_setup(self, setup: float, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        assert_ocp_setup(setup)
        cmd = f"{CommonCommands.OCP_SETUP.value} {chl},{setup}"
        self.write(cmd)
        return self.get_ocp_value()

    def turn_ocp_on(self, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CONTROL.value} {chl},{WorkStatus.ON.value}"
        self.write(cmd)
        return self.get_ocp_value()

    def turn_ocp_off(self, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CONTROL.value} {chl},{WorkStatus.OFF.value}"
        self.write(cmd)
        return self.get_ocp_value()

    def turn_ovp_on(self, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CONTROL.value} {chl},{WorkStatus.ON.value}"
        self.write(cmd)
        return self.get_ocp_value()

    def turn_ovp_off(self, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CONTROL.value} {chl},{WorkStatus.OFF.value}"
        self.write(cmd)
        return self.get_ocp_value()

    def ovp_setup(self, setup: float, chl: str | Channel = Channel.ch1):
        chl = assert_channel_setup(chl)
        assert_ovp_setup(setup)
        cmd = f"{CommonCommands.OVP_SETUP.value} {chl},{setup}"
        self.write(cmd)
        return self.get_ocp_value()

    def clear_op_alarm(self, chl: str | Channel = Channel.ch1) -> None:
        chl = assert_channel_setup(chl)

        cmd = f"{CommonCommands.OVP_CLEAR.value} {chl}"
        self.write(cmd)
        cmd = f"{CommonCommands.OCP_CLEAR.value} {chl}"
        self.write(cmd)
        response = self.get_op_info(chl)
        ovp_alarm = response["ovp"]["alarm"]
        ocp_alarm = response["ocp"]["alarm"]

        if ocp_alarm is AlarmStatus.Yes:
            raise ClearAlarmException(f"Clear OCP Alarm Fail")
        if ovp_alarm is AlarmStatus.Yes:
            raise ClearAlarmException(f"Clear OVP Alarm Fail")
        return
