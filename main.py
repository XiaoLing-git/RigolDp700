from rigol_dp700 import Driver

if __name__ == '__main__':

    # logger.setLevel(logging.DEBUG)

    ser = Driver(port="COM7")
    ser.connect()
    res = ser.apply_status()
    print(res)

    res = ser.apply_set(voltage=10,current=3,chl="CH1")
    print(res)
    res = ser.get_channel_status()
    print(res)
    res = ser.set_channel_status(chl="CH1",setup=WorkStatus.OFF)
    print(res)
    res = ser.current_status(chl="CH1")
    print(res)

    res = ser.ocp_setup(5.2)
    print(res)

    res = ser.ovp_setup(20)
    print(res)

    res = ser.turn_ocp_off()
    print(res)

    res = ser.turn_ovp_on()
    print(res)

    res = ser.get_op_info(chl="CH1")
    print(res)

    # res = ser.get_op_setup(chl="CH1")
    # print(res)