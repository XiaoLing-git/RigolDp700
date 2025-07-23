from pathlib import Path

from .commands import CommonCommands
from .errors import ClearAlarmException
from .models import (
    OP_INFO,
    AlarmStatus,
    ApplyStatusModel,
    Channel,
    CurrentWorkStatusModel,
    WorkStatus,
)
from .serial_write_read import SerialWriteRead
from .utils import (
    assert_apply_setup,
    assert_channel_setup,
    assert_ocp_setup,
    assert_ovp_setup,
)

CURRENT_FILE_NAME = Path(__file__).stem


class CommonCommandsConnection(SerialWriteRead):
    def apply_status(self) -> ApplyStatusModel:
        """
        get apply status
        :return: ApplyStatusModel
        """
        self.write(CommonCommands.APPLY_STATUS)
        response: str = self.read()
        return ApplyStatusModel.parse_str(response)

    def apply_setup(
        self, current: float, voltage: float, chl: str | Channel = Channel.ch1
    ) -> ApplyStatusModel:
        """
        proset current, voltage and channel,then get apply status
        :param current: 0 < value 5.3 A
        :param voltage: 0 < value 32 V
        :param chl: default CH1
        :return: ApplyStatusModel
        """
        chl = assert_channel_setup(chl)
        assert_apply_setup(current, voltage)

        cmd: str = f"{CommonCommands.APPLY_SETUP.value} {chl},{voltage},{current}"
        self.write(cmd)
        return self.apply_status()

    def engage_apply_setup(self, chl: str | Channel = Channel.ch1) -> ApplyStatusModel:
        """
        enable apply setup
        :param chl: default CH1
        :return: ApplyStatusModel
        """
        chl = assert_channel_setup(chl)

        cmd: str = f"{CommonCommands.TURN_ON.value} {chl},{WorkStatus.ON.value}"
        self.write(cmd)
        return self.apply_status()

    def disengage_apply_setup(
        self, chl: str | Channel = Channel.ch1
    ) -> ApplyStatusModel:
        """
        enable apply setup
        :param chl: default CH1
        :return: ApplyStatusModel
        """
        chl = assert_channel_setup(chl)

        cmd: str = f"{CommonCommands.TURN_OFF.value} {chl},{WorkStatus.OFF.value}"
        print(cmd)
        self.write(cmd)
        return self.apply_status()

    def current_status(
        self, chl: str | Channel = Channel.ch1
    ) -> CurrentWorkStatusModel:
        """
        get work status
        :param chl: default is CH1
        :return: CurrentWorkStatusModel
        """

        assert_channel_setup(chl)

        self.write(CommonCommands.CURRENT_STATUS)
        response: str = self.read()
        return CurrentWorkStatusModel.parse_str(response)

    def get_channel_status(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        get channel status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """
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
        """
        Set channel status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """
        if setup not in list(WorkStatus):
            raise ValueError(
                f"Chanel {chl} status setup Error, {setup} not in {list(WorkStatus)}"
            )
        chl = assert_channel_setup(chl)
        cmd: str = f"{CommonCommands.CHANNEL_SETUP.value} {chl},{setup.value}"
        self.write(cmd)
        return self.get_channel_status(chl)

    def get_ocp_alarm(self, chl: str | Channel = Channel.ch1) -> AlarmStatus:
        """
        get ocp alarm status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """
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
        """
        get ovp alarm status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """

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
        """
        get ocp work status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_STATUS.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            WorkStatus.ON if response.upper() in WorkStatus.ON.value else WorkStatus.OFF
        )

    def get_ovp_status(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        get ovp work status  ON/OFF
        :param chl:  default is CH1
        :return: ON/OFF
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_STATUS.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return (
            WorkStatus.ON if response.upper() in WorkStatus.ON.value else WorkStatus.OFF
        )

    def get_ocp_value(self, chl: str | Channel = Channel.ch1) -> float:
        """
        get ocp setup value
        :param chl:  default is CH1
        :return: float Unit=A
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CHECK.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return float(response)

    def get_ovp_value(self, chl: str | Channel = Channel.ch1) -> float:
        """
        get ovp setup value
        :param chl:  default is CH1
        :return: float Unit=v
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CHECK.value} {chl}"
        self.write(cmd)
        response: str = self.read()
        return float(response)

    def get_op_info(self, chl: str | Channel = Channel.ch1) -> OP_INFO:
        """
        get all op info
        :param chl: default is CH1
        :return:
        """
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

    def ocp_setup(self, setup: float, chl: str | Channel = Channel.ch1) -> float:
        """
        proset ocp value
        :param setup:
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        assert_ocp_setup(setup)
        cmd = f"{CommonCommands.OCP_SETUP.value} {chl},{setup}"
        self.write(cmd)
        return self.get_ocp_value()

    def ovp_setup(self, setup: float, chl: str | Channel = Channel.ch1) -> float:
        """
        proset ovp value
        :param setup:
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        assert_ovp_setup(setup)
        cmd = f"{CommonCommands.OVP_SETUP.value} {chl},{setup}"
        self.write(cmd)
        return self.get_ocp_value()

    def turn_ocp_on(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        turn on ocp function
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CONTROL.value} {chl},{WorkStatus.ON.value}"
        self.write(cmd)
        return self.get_ocp_status()

    def turn_ocp_off(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        turn off ocp function
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OCP_CONTROL.value} {chl},{WorkStatus.OFF.value}"
        self.write(cmd)
        return self.get_ocp_status()

    def turn_ovp_on(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        turn on ovp function
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CONTROL.value} {chl},{WorkStatus.ON.value}"
        self.write(cmd)
        return self.get_ocp_status()

    def turn_ovp_off(self, chl: str | Channel = Channel.ch1) -> WorkStatus:
        """
        turn off ovp function
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CONTROL.value} {chl},{WorkStatus.OFF.value}"
        self.write(cmd)
        return self.get_ocp_status()

    def clear_op_alarm(self, chl: str | Channel = Channel.ch1) -> None:
        """
        clear all op alarm,
        :param chl:
        :return:
        """
        chl = assert_channel_setup(chl)
        cmd = f"{CommonCommands.OVP_CLEAR.value} {chl}"
        self.write(cmd)
        cmd = f"{CommonCommands.OCP_CLEAR.value} {chl}"
        self.write(cmd)
        response = self.get_op_info(chl)
        ovp_alarm = response["ovp"]["alarm"]
        ocp_alarm = response["ocp"]["alarm"]

        if ocp_alarm is AlarmStatus.Yes:
            raise ClearAlarmException("Clear OCP Alarm Fail")
        if ovp_alarm is AlarmStatus.Yes:
            raise ClearAlarmException("Clear OVP Alarm Fail")
        return
