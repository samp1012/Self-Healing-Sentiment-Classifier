import logging

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs.txt")
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
