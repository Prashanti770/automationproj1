import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.txt",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger