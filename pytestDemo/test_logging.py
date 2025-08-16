import logging

class Logging():
    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logFile.log')
        fileformat = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(fileformat)
        # logger.setLevel(logging.ERROR)
        logger.addHandler(fileHandler)

        # logger.debug("This is a debug log")
        # logger.info("Info log")
        # logger.warning("Warning log")
        # logger.error("Error log")
        # logger.critical("Critical log")

        return logger
