from lib import logger as log
from lib import mapper
import numpy as np

logger = log.get_logger()


def handler(event, _):
    data = np.arange(15)
    logger.info('Hello from first lambda')
