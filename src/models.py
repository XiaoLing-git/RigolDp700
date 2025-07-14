from enum import Enum
from pathlib import Path

from pydantic import BaseModel

from src.errors import ParseStrToModelException
from src.logger import device_logger

CURRENT_FILE_NAME = Path(__file__).stem

RESPONSE_END_TAG: str = "\n"

COMMAND_END_TAG: str = "\n"

# Unit = V
MAX_VOLTAGE: float = 32
MIN_VOLTAGE: float = 0

# Unit = A
MAX_CURRENT: float = 5.3
MIN_CURRENT: float = 0


class BaseStatus(Enum):
    PASS = 1
    FAIL = 0
    UNKNOWN = -1


class WorkStatus(Enum):
    ON = "ON"
    OFF = "OFF"


class AlarmStatus(Enum):
    Yes = "YES"
    No = "NO"


class Channel(Enum):
    ch1 = "CH1"


class InformationModel(BaseModel):
    model: str
    sn: str
    version: str

    @classmethod
    def parse_str(cls, content: str):
        try:
            response: list[str] = content.strip().split(",")
            cls.model = response[1]
            cls.sn = response[2]
            cls.version = response[3]
            return cls(
                model=response[1].strip(),
                sn=response[2].strip(),
                version=response[3].strip(),
            )
        except Exception as e:
            raise ParseStrToModelException(e)


class SelfCheckModel(BaseModel):
    fan: BaseStatus

    @classmethod
    def parse_str(cls, content: str):
        try:
            response: list[str] = content.strip().split(":")
            results: str = response[1].strip().lower()
            if "pass" in results:
                statue = BaseStatus.PASS
            elif "fail" in results:
                statue = BaseStatus.FAIL
            else:
                statue = BaseStatus.UNKNOWN
            return cls(fan=statue)
        except Exception as e:
            raise ParseStrToModelException(e)


class ServiceModel(BaseModel):
    trigger: bool
    timer: bool
    other: bool

    @classmethod
    def parse_str(cls, content: str):
        try:
            response: list[str] = content.strip().split(",")

            return cls(
                trigger=bool(int(response[0].strip())),
                timer=bool(int(response[1].strip())),
                other=bool(int(response[2].strip())),
            )
        except Exception as e:
            raise ParseStrToModelException(e)


class ApplyStatusModel(BaseModel):
    channel: Channel = Channel.ch1
    voltage: float
    current: float

    @classmethod
    def parse_str(cls, content: str, chl: Channel | None = None):
        try:
            response: list[str] = content.strip().split(",")
            if len(response) != 2:
                raise ParseStrToModelException(
                    f"Get Apply Status Fail, Original Content:{content}"
                )
            if chl is None:
                return cls(
                    voltage=float(response[0].strip()),
                    current=float(response[1].strip()),
                )
            else:
                return cls(
                    channel=chl,
                    voltage=float(response[0].strip()),
                    current=float(response[1].strip()),
                )
        except Exception as e:
            device_logger.warn(e)
            raise ParseStrToModelException(e)

    def __str__(self):
        return (
            f"channel={self.channel} voltage={self.voltage} V current={self.current} A"
        )


class CurrentWorkStatusModel(BaseModel):
    channel: Channel = Channel.ch1
    voltage: float
    current: float
    power: float

    @classmethod
    def parse_str(cls, content: str, chl: Channel | None = None):
        try:
            response: list[str] = content.strip().split(",")
            if len(response) != 3:
                raise ParseStrToModelException(
                    f"Get Current Work Status Fail, Original Content:{content}"
                )
            if chl is None:
                return cls(
                    voltage=float(response[0].strip()),
                    current=float(response[1].strip()),
                    power=float(response[2].strip()),
                )
            else:
                return cls(
                    channel=chl,
                    voltage=float(response[0].strip()),
                    current=float(response[1].strip()),
                    power=float(response[2].strip()),
                )
        except Exception as e:
            device_logger.warn(e)
            raise ParseStrToModelException(e)

    def __str__(self):
        return f"channel={self.channel} voltage={self.voltage} V current={self.current} A power={self.power} W"
