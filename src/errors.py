class SerialException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

    def __repr__(self):
        return self._msg


class SerialConnectError(SerialException):
    pass


class SerialDisconnectError(SerialException):
    pass


class SerialReadConnectError(SerialException):
    pass


class SerialWriteConnectError(SerialException):
    pass


class ParseStrToModelException(SerialException):
    pass


class ResetException(SerialException):
    pass


class ChannelNotExistException(SerialException):
    pass


class ClearAlarmException(SerialException):
    pass
