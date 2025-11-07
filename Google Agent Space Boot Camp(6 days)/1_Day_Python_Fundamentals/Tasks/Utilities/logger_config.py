# app/utils/logger_config.py
import logging
from pathlib import Path

def setup_logger():
    log_path = Path(r"C:\GCP\GenAILearnings\Google Agent Space Boot Camp(6 days)\1_Day_Python_Fundamentals\data\logs")
    log_path.mkdir(parents=True, exist_ok=True)

    log_file = log_path / "fastapi_logger.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        filemode="a"
    )

    logger = logging.getLogger("FastAPI Logger")
    return logger
