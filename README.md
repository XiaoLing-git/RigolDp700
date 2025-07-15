# RigolDp700
 Python Support for [Rigol DP700](https://www.rigolna.com/products/dc-power-loads/dp700/) Series power supplies.

## Company
https://www.rigolna.com/

## Notes:

Before you start it, please make sure you have installed the following tools

- make
- poetry
- black
- mypy
- ruff

## Commands

### Format Code

```bash
make format
```

### Type Check

```bash
make check
```

### Build Wheel

```bash
make build
```

### Install 

```bash
make install
```

### Enter Venv 

```bash
make shell
```

### Clean

```bash
make clean
```

### Commit To Github

```bash
make commit msg="comments"
```

### Test

```bash
make test
```

### debug

```bash
make debug
```



## Instructions

```python

import logging

from rigol_dp700 import (Driver,
                         WorkStatus,
                         serial_connection_logger,
                         serial_write_read_logger,
                         device_logger,
                         )

if __name__ == '__main__':

    serial_connection_logger.setLevel(logging.DEBUG)
    serial_write_read_logger.setLevel(logging.DEBUG)
    device_logger.setLevel(logging.DEBUG)

    ser = Driver(port="COM7")
    ser.connect()
    res = ser.apply_status()
    print(res)
    res = ser.apply_setup(voltage=10,current=3,chl="CH1")
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



```



