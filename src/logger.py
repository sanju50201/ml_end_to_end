import logging
from pathlib import Path
from datetime import datetime


def configure_logging():
    """
    Configure the Logging settings for the application
    """

    LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    # log paths
    logs_path = Path.cwd() / "logs"
    logs_path.mkdir(parents=True, exist_ok=True)

    LOG_FILE_PATH = logs_path / LOG_FILE

    # configure the logging settings

    logging.basicConfig(filename=LOG_FILE_PATH,
                        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
