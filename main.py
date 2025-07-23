import logging

from rigol_dp700 import (
    Driver,
    device_logger,
    serial_connection_logger,
    serial_write_read_logger,
)

if __name__ == "__main__":
    serial_connection_logger.setLevel(logging.DEBUG)
    serial_write_read_logger.setLevel(logging.DEBUG)
    device_logger.setLevel(logging.DEBUG)

    ser = Driver(port="COM7")
    ser.connect()
    print(ser.engage_apply_setup())

    print(ser.current_status())

    print(ser.ocp_setup(5.2))

    print(ser.ovp_setup(20))

    print(ser.turn_ocp_off())

    print(ser.turn_ovp_on())

    print(ser.get_op_info(chl="CH1"))
