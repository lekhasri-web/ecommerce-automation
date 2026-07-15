import logging

# logger function is used to logging the actions to debug it after sometime
def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

