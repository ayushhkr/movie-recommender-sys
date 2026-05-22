import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
    PORT = int(os.environ.get("PORT", "5000"))
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    MOVIE_DATA_PATH = BASE_DIR / "movie_list.pkl"
    SIMILARITY_DATA_PATH = BASE_DIR / "similarity.pkl"
    RECOMMENDATION_LIMIT = int(os.environ.get("RECOMMENDATION_LIMIT", "5"))
    SAMPLE_MOVIES = (
        "Avatar",
        "Inception",
        "The Dark Knight",
        "Interstellar",
        "The Avengers",
    )
