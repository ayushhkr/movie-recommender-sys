import logging

from flask import Flask

from .config import Config
from .data_loader import DataLoadError, load_movie_data
from .recommender import RecommendationEngine
from .routes import main_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    _configure_logging(app)
    _register_recommender(app)
    app.register_blueprint(main_bp)
    return app


def _configure_logging(app):
    level_name = str(app.config.get("LOG_LEVEL", "INFO")).upper()
    level = getattr(logging, level_name, logging.INFO)
    app.logger.setLevel(level)


def _register_recommender(app):
    app.extensions["recommender_error"] = None

    if app.config.get("RECOMMENDER_ENGINE") is not None:
        app.extensions["recommender_engine"] = app.config["RECOMMENDER_ENGINE"]
        return

    try:
        movies, similarity = load_movie_data(
            app.config["MOVIE_DATA_PATH"],
            app.config["SIMILARITY_DATA_PATH"],
        )
        app.extensions["recommender_engine"] = RecommendationEngine(
            movies=movies,
            similarity=similarity,
        )
        app.logger.info("Loaded %s movies into the recommendation engine.", len(movies))
    except DataLoadError as exc:
        app.extensions["recommender_engine"] = None
        app.extensions["recommender_error"] = str(exc)
        app.logger.error("Recommendation engine could not be loaded: %s", exc)
