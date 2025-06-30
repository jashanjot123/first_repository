import logging
import os

def test_loggingdemo():
    logger = logging.getLogger(__name__)
    filehandler=logging.FileHandler(r'/CSS SELECTOR/Logging/logfile.log')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error is occurred")
    logger.critical("Critical issue")
