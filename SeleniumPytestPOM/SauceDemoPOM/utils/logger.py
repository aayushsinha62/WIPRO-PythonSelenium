import logging

def get_logger():
    logger = logging.getLogger("SauceDemoLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("execution.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger