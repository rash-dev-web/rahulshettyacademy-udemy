import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("file.log")

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.setLevel(logging.CRITICAL)
    logger.debug("debug...")
    logger.info("info...")
    logger.warning("warning...")
    logger.error("error...")
    logger.critical("critical...")
    print("test")
