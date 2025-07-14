# import serial  # type: ignore[import-untyped]
# from serial import Serial
#
#
# class Driver:
#     _instances = {}  # type: ignore[var-annotated]
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#     def __init__(
#         self,
#         port: str,
#         baud: int = 9600,
#         data_bits: int = serial.EIGHTBITS,
#         stop_bits: float = serial.STOPBITS_ONE,
#         parity: str = serial.PARITY_NONE,
#         timeout: float = 5,
#     ):
#         self.__port = port
#         self.__baud = baud
#         self.__data_bits = data_bits
#         self.__stop_bits = stop_bits
#         self.__parity = parity
#         self.__timeout = timeout
#         self.__ser: Serial | None = None
#
#     @property
#     def port(self):
#         return self.__port
#
#     @property
#     def serial(self):
#
#         return self.__ser
#
#     def connect(self):
#         if self.serial is None or self.serial.closed:
#             self.__ser = Serial(
#                 port=self.__port,
#                 baudrate=self.__baud,
#                 bytesize=self.__data_bits,
#                 parity=self.__parity,
#                 stopbits=self.__stop_bits,
#                 timeout=self.__timeout,
#             )
#
#     def disconnect(self):
#         if self.serial is not None or self.serial.is_open:
#             self.serial.close()
