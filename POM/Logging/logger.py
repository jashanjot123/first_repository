import logging


def get_logger():
    logger = logging.getLogger(__name__)
    filehandler=logging.FileHandler(r'C:\Users\HP\PycharmProjects\PythonProject1\Selenium_Python\POM\Logging\logfile.log')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger