from enum import Enum
from pathlib import Path

from pydantic import BaseModel

from src.errors import ParseStrToModelException
from src.utils import logger

CURRENT_FILE_NAME = Path(__file__).stem

RESPONSE_END_TAG: str = "\n"

COMMAND_END_TAG: str = "\n"


class BaseStatus(Enum):
    PASS = 1
    FAIL = 0
    UNKNOWN = -1


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


class WorkStatusModel(BaseModel):
    channel: Channel = Channel.ch1
    voltage: float
    current: float

    @classmethod
    def parse_str(cls, content: str):
        try:
            response: list[str] = content.strip().split(",")
            if len(response) != 2:
                raise ParseStrToModelException(
                    f"Get Current Work Status Fail, Original Content:{content}"
                )
            return cls(
                voltage=float(response[0].strip()), current=float(response[1].strip())
            )
        except Exception as e:
            logger.warn(e)
            raise ParseStrToModelException(e)
