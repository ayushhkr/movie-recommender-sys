import unittest

import numpy as np
import pandas as pd

from movie_recommender.recommender import RecommendationEngine


def build_engine():
    movies = pd.DataFrame(
        {
            "title": [
                "Avatar",
                "Avatar: The Way of Water",
                "Titanic",
                "Aliens",
                "The Abyss",
            ]
        }
    )
    similarity = np.array(
        [
            [1.0, 0.92, 0.74, 0.62, 0.54],
            [0.92, 1.0, 0.55, 0.50, 0.49],
            [0.74, 0.55, 1.0, 0.41, 0.31],
            [0.62, 0.50, 0.41, 1.0, 0.67],
            [0.54, 0.49, 0.31, 0.67, 1.0],
        ]
    )
    return RecommendationEngine(movies=movies, similarity=similarity)


class RecommendationEngineTests(unittest.TestCase):
    def test_recommend_exact_match_returns_ranked_titles(self):
        engine = build_engine()

        result = engine.recommend("Avatar", limit=3)

        self.assertEqual(result.selected_title, "Avatar")
        self.assertEqual(
            result.recommendations,
            ["Avatar: The Way of Water", "Titanic", "Aliens"],
        )
        self.assertIsNone(result.error)

    def test_recommend_partial_match_with_multiple_results_returns_suggestions(self):
        engine = build_engine()

        result = engine.recommend("ava", limit=3)

        self.assertIsNone(result.selected_title)
        self.assertEqual(result.recommendations, [])
        self.assertEqual(
            result.suggestions,
            ["Avatar", "Avatar: The Way of Water"],
        )
        self.assertEqual(
            result.error,
            "Multiple matches found. Pick one of these exact titles.",
        )

    def test_recommend_empty_query_returns_validation_error(self):
        engine = build_engine()

        result = engine.recommend("", limit=3)

        self.assertEqual(
            result.error,
            "Enter a movie title to get recommendations.",
        )


if __name__ == "__main__":
    unittest.main()
