from flask import Blueprint, current_app, jsonify, render_template, request

from .recommender import RecommendationResult


main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    movie_name = _get_requested_movie_name()
    engine = current_app.extensions.get("recommender_engine")
    app_ready = engine is not None

    if movie_name or not app_ready:
        result, _status_code = _run_recommendation(movie_name)
    else:
        result = RecommendationResult(query="")

    return render_template(
        "index.html",
        movie_name=movie_name,
        result=result,
        sample_movies=current_app.config["SAMPLE_MOVIES"],
        app_ready=app_ready,
    )


@main_bp.route("/api/recommendations", methods=["GET"])
def api_recommendations():
    movie_name = request.args.get("movie", "")
    result, status_code = _run_recommendation(movie_name)
    payload = result.to_dict()
    payload["status"] = "ok" if status_code == 200 else "error"
    return jsonify(payload), status_code


@main_bp.route("/health", methods=["GET"])
def healthcheck():
    engine = current_app.extensions.get("recommender_engine")
    error = current_app.extensions.get("recommender_error")
    movie_count = len(engine.movies) if engine is not None else 0
    status = "ok" if engine is not None else "degraded"
    return jsonify(
        {
            "status": status,
            "movie_count": movie_count,
            "error": error,
        }
    ), 200 if engine is not None else 503


def _get_requested_movie_name():
    if request.method == "POST":
        return request.form.get("movie_name", "").strip()
    return request.args.get("movie", "").strip()


def _run_recommendation(movie_name):
    engine = current_app.extensions.get("recommender_engine")
    if engine is None:
        error = current_app.extensions.get("recommender_error") or (
            "The recommendation engine is temporarily unavailable."
        )
        return RecommendationResult(query=movie_name, error=error), 503

    result = engine.recommend(
        movie_name=movie_name,
        limit=current_app.config["RECOMMENDATION_LIMIT"],
    )

    if result.selected_title:
        current_app.logger.info(
            "Generated %s recommendations for '%s'.",
            len(result.recommendations),
            result.selected_title,
        )

    if result.error and not movie_name:
        return result, 400
    if result.error and not result.suggestions:
        return result, 404
    return result, 200
