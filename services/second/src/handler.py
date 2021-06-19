from lib import logger as log
from lib import mapper

logger = log.get_logger()


def handler(event, _):
    logger.info('Hello from second lambda')
