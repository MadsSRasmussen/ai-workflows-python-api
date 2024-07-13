import logging

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)