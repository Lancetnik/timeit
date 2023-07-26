import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(fname)-22s %(time).10f - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger()
