class SerialException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

    def __repr__(self):
        return self._msg


class SerialConnectError(SerialException):
    """Raise Error while serial connect fail."""

    pass


class SerialDisconnectError(SerialException):
    """Raise Error while serial disconnect fail."""

    pass


class SerialReadConnectError(SerialException):
    """Raise Error while serial read before connect."""

    pass


class SerialWriteConnectError(SerialException):
    """Raise Error while serial write before connect."""


class ParseStrToModelException(SerialException):
    """Raise Error while parse response to model fail."""

    pass


class ResetException(SerialException):
    """Raise Error while reset fail."""

    pass


class ChannelNotExistException(SerialException):
    """Raise Error while channel not exist."""

    pass


class ApplySetupError(SerialException):
    """Raise Error while apply setup value error."""

    pass


class ClearAlarmException(SerialException):
    """Raise Error while clear alarm flag fail."""

    pass
