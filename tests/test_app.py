import unittest

import pandas as pd

from movie_recommender import create_app
from movie_recommender.recommender import RecommendationResult


class FakeEngine:
    def __init__(self):
        self.movies = pd.DataFrame({"title": ["Avatar", "Titanic"]})

    def recommend(self, movie_name, limit=5):
        if not movie_name:
            return RecommendationResult(
                query="",
                error="Enter a movie title to get recommendations.",
            )

        if movie_name.lower() == "avatar":
            return RecommendationResult(
                query=movie_name,
                selected_title="Avatar",
                recommendations=["Titanic", "Aliens"][:limit],
            )

        return RecommendationResult(
            query=movie_name,
            error="No movie matched that title. Try one of the sample searches below.",
        )


class FlaskAppTests(unittest.TestCase):
    def test_home_page_renders_without_error_before_search(self):
        app = create_app({"TESTING": True, "RECOMMENDER_ENGINE": FakeEngine()})
        client = app.test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        page = response.get_data(as_text=True)
        self.assertIn("Movie Recommender System", page)
        self.assertIn("Results appear here after a search.", page)

    def test_api_recommendations_returns_json_payload(self):
        app = create_app({"TESTING": True, "RECOMMENDER_ENGINE": FakeEngine()})
        client = app.test_client()

        response = client.get("/api/recommendations?movie=Avatar")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["selected_title"], "Avatar")
        self.assertEqual(payload["recommendations"], ["Titanic", "Aliens"])
        self.assertEqual(payload["status"], "ok")

    def test_healthcheck_reports_degraded_state_when_data_is_missing(self):
        app = create_app(
            {
                "TESTING": True,
                "MOVIE_DATA_PATH": "missing-movies.pkl",
                "SIMILARITY_DATA_PATH": "missing-similarity.pkl",
            }
        )
        client = app.test_client()

        response = client.get("/health")

        self.assertEqual(response.status_code, 503)
        payload = response.get_json()
        self.assertEqual(payload["status"], "degraded")
        self.assertIn("Movie data file was not found", payload["error"])


if __name__ == "__main__":
    unittest.main()
