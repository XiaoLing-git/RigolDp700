import logging

from rigol_dp700 import (Driver,
                         WorkStatus,
                         serial_connection_logger,
                         serial_write_read_logger,
                         device_logger,
                         )

if __name__ == '__main__':


    for i in range(100):
        print(i)
    # serial_connection_logger.setLevel(logging.DEBUG)
    # serial_write_read_logger.setLevel(logging.DEBUG)
    # device_logger.setLevel(logging.DEBUG)

    # ser = Driver(port="COM7")
    # ser.connect()
    # res = ser.engage_apply_setup()
    # print(res)
    # res = ser.current_status()
    # print(res)
    #
    # res = ser.ocp_setup(5.2)
    # print(res)
    #
    # res = ser.ovp_setup(20)
    # print(res)
    #
    # res = ser.turn_ocp_off()
    # print(res)
    #
    # res = ser.turn_ovp_on()
    # print(res)
    #
    # res = ser.get_op_info(chl="CH1")
    # print(res)

