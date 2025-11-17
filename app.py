from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# --- Load Data ---
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Recommendation Function ---
def recommend_movies(movie_name):
    movie_name = movie_name.lower().strip()
    movie_list = movies['title'].str.lower().tolist()

    print(f"Searching for: {movie_name}")

    # Find matching movie
    matches = [i for i, title in enumerate(movie_list) if movie_name in title]
    if not matches:
        print("No match found.")
        return ["No match found. Try another movie."]

    idx = matches[0]
    print(f"Found movie at index: {idx} -> {movies.iloc[idx].title}")

    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended = []
    for i in distances[1:6]:  # skip the first (same movie)
        title = movies.iloc[i[0]].title
        recommended.append(title)
        print("Recommended:", title)

    return recommended

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    movie_name = ""
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        recommendations = recommend_movies(movie_name)
    return render_template('index.html', recommendations=recommendations, movie_name=movie_name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
#flask app.py