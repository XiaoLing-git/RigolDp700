import logging
from pathlib import Path

logging.basicConfig(
    format=f"%(asctime)s line:%(lineno)d %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
