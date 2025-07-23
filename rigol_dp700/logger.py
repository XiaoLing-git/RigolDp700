import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.INFO,
)
# logger for serial_connection.py
# default level is INFO,
# if you want more detail ,try set it in main.py like below
# serial_connection_logger.setLevel(logging.DEBUG)
serial_connection_logger = logging.getLogger(__name__)


logging.basicConfig(
    format="%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.INFO,
)
# logger for serial_write_read.py
# default level is INFO,
# if you want more detail ,try set it in main.py like below
# serial_write_read_logger.setLevel(logging.DEBUG)
serial_write_read_logger = logging.getLogger(__name__)


logging.basicConfig(
    format="%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.INFO,
)

# logger for driver.py
# default level is INFO,
# if you want more detail ,try set it in main.py like below
# device_logger.setLevel(logging.DEBUG)
device_logger = logging.getLogger(__name__)
