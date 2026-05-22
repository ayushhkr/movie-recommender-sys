from pathlib import Path
import pickle

import pandas as pd


class DataLoadError(RuntimeError):
    """Raised when the model artifacts cannot be loaded safely."""


def load_movie_data(movie_path, similarity_path):
    movie_path = Path(movie_path)
    similarity_path = Path(similarity_path)

    if not movie_path.exists():
        raise DataLoadError(f"Movie data file was not found: {movie_path}")
    if not similarity_path.exists():
        raise DataLoadError(f"Similarity data file was not found: {similarity_path}")

    with movie_path.open("rb") as movie_file:
        movies = pickle.load(movie_file)

    with similarity_path.open("rb") as similarity_file:
        similarity = pickle.load(similarity_file)

    if not isinstance(movies, pd.DataFrame):
        raise DataLoadError("Movie data must be a pandas DataFrame.")
    if "title" not in movies.columns:
        raise DataLoadError("Movie data must include a 'title' column.")

    similarity_size = getattr(similarity, "shape", [len(similarity)])[0]
    if len(movies) != similarity_size:
        raise DataLoadError(
            "Movie data and similarity matrix are out of sync. Regenerate the model artifacts."
        )

    return movies, similarity
