import logging
import __main__
from pathlib import Path

# serial_connection_log =Path(__main__.__file__).parent / "serial_connection.log"
logging.basicConfig(
    # filename=serial_connection_log,
    format=f"%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.DEBUG,
)
serial_connection_logger = logging.getLogger(__name__)


# serial_write_read_log =Path(__main__.__file__).parent / "serial_write_read.log"
logging.basicConfig(
    #     filename=serial_write_read_log,
    format=f"%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.INFO,
)
serial_write_read_logger = logging.getLogger(__name__)


# serial_write_read_log =Path(__main__.__file__).parent / "serial_write_read.log"
logging.basicConfig(
    #     filename=serial_write_read_log,
    format=f"%(asctime)s %(levelname)s line:%(lineno)d %(message)s",
    level=logging.INFO,
)
device_logger = logging.getLogger(__name__)
