# Movie Recommender System

Movie Recommender System is a Flask web app that recommends similar films from a precomputed similarity matrix. The project started as a machine learning demo and has been upgraded to better reflect software engineering skills: modular backend code, validation, logging, automated tests, a health endpoint, and a simple JSON API.

Live demo: https://movie-recommender-sys-zabp.onrender.com

## Why this project is useful in a portfolio

- It shows end-to-end ownership: data artifacts, backend logic, web UI, and deployment.
- It demonstrates production-minded basics: app factory pattern, service layer, health check, and CI.
- It keeps the machine learning piece understandable instead of hiding the app behind a notebook.

## Features

- Search for a movie title and get five similar recommendations.
- Handle exact matches, partial matches, and no-match scenarios gracefully.
- Browse a cleaner interface with sample searches and suggestion links.
- Use a JSON endpoint at `/api/recommendations?movie=Avatar`.
- Monitor service health at `/health`.

## Project structure

```text
movie-recommender-sym/
|-- app.py
|-- movie_recommender/
|   |-- __init__.py
|   |-- config.py
|   |-- data_loader.py
|   |-- recommender.py
|   |-- routes.py
|   |-- static/
|   |   `-- style.css
|   `-- templates/
|       `-- index.html
|-- tests/
|   |-- test_app.py
|   `-- test_recommender.py
|-- .github/workflows/ci.yml
|-- movie_list.pkl
|-- similarity.pkl
|-- requirements.txt
`-- README.md
```

## Local setup

### Prerequisites

- Python 3.11+
- Git LFS

### Install and run

```bash
git clone https://github.com/ayushhkr/movie-recommender-sys.git
cd movie-recommender-sys
git lfs install
git lfs pull
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Testing

Run the full test suite with:

```bash
python -m unittest discover -s tests
```

The GitHub Actions workflow in `.github/workflows/ci.yml` runs the same command on each push and pull request.

## Model artifacts

- `movie_list.pkl` stores the processed movie metadata.
- `similarity.pkl` stores the precomputed similarity matrix used at request time.
- `movie-recommend .ipynb` contains the earlier experimentation workflow and can be turned into a dedicated training script later.

## Engineering improvements made

- Refactored the original single-file Flask app into a package.
- Added a recommendation service and a safer data loading layer.
- Removed `print()` debugging in favor of application logging.
- Added API and health endpoints for easier testing and deployment checks.
- Moved styling into a dedicated static file and improved the UI states.
- Added automated tests for both the recommendation logic and Flask routes.
- Added CI to run the tests automatically.

## Deployment

This app is compatible with the existing `Procfile` and can still be deployed with:

```bash
gunicorn app:app
```

Current deployed app:

https://movie-recommender-sys-zabp.onrender.com

## Next improvements

- Convert the notebook into a reproducible training script.
- Add metadata such as posters, genres, and release year to each recommendation.
- Add caching or faster lookup structures if the dataset grows.
