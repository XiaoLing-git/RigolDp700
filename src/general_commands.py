from pathlib import Path

from .commands import GeneralCommands
from .errors import ResetException
from .models import InformationModel, SelfCheckModel, ServiceModel, WorkStatusModel
from .serial_write_read import SerialWriteRead
from .utils import logger

CURRENT_FILE_NAME = Path(__file__).stem


class GeneralCommandsConnection(SerialWriteRead):

    def get_device_information(self) -> InformationModel:
        self.write(GeneralCommands.Information)
        response: str = self.read()
        return InformationModel.parse_str(response)

    def self_check(self) -> SelfCheckModel:
        self.write(GeneralCommands.Self_Check)
        response: str = self.read()
        return SelfCheckModel.parse_str(response)

    def get_work_status(self) -> WorkStatusModel:
        self.write(GeneralCommands.Work_Status)
        response: str = self.read()
        return WorkStatusModel.parse_str(response)

    def get_service(self) -> ServiceModel:
        self.write(GeneralCommands.Service)
        response: str = self.read()
        return ServiceModel.parse_str(response)

    def reset(self) -> None:
        try:
            self.write(GeneralCommands.Reset)
        except Exception as e:
            msg: str = (
                f"System Error While Send Reset Command |{GeneralCommands.Reset}| msg={e}"
            )
            logger.warn(f"{CURRENT_FILE_NAME}.{self.__class__.__name__} {msg}")
            raise ResetException(msg)
        logger.warn(
            f"{CURRENT_FILE_NAME}.{self.__class__.__name__} System Reset Command Send OK"
        )
