# 🎬 Movie Recommendation System

A Flask-based web application that recommends movies based on similarity matching using machine learning. Enter a movie title and get 5 similar movie recommendations instantly.

🌐 **Live Demo**: [https://movie-recommender-sys-zabp.onrender.com](https://movie-recommender-sys-zabp.onrender.com)

## 📋 Features

- **Intelligent Recommendations**: Uses cosine similarity to find movies with similar features
- **Simple Interface**: Clean, user-friendly web interface
- **Fast Processing**: Leverages pre-computed similarity matrices for instant results
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Flask 3.0.3
- **Machine Learning**: scikit-learn 1.5.2
- **Data Processing**: pandas 2.2.3, numpy 2.1.3
- **Production Server**: Gunicorn 23.0.0
- **Python Version**: 3.11.9

## 📁 Project Structure

```
movie-recommender-system/
├── app.py                 # Main Flask application
├── movie_list.pkl         # Preprocessed movie dataset
├── similarity.pkl         # Precomputed similarity matrix (176 MB)
├── templates/
│   └── index.html        # Frontend template
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version specification
└── .gitignore            # Git ignore rules
```

## 🚀 Local Setup & Installation

### Prerequisites
- Python 3.11.9 or higher
- Git
- Git LFS (for large model files)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayushhkr/movie-recommender-sys.git
   cd movie-recommender-sys
   ```

2. **Install Git LFS** (if not already installed)
   ```bash
   git lfs install
   git lfs pull
   ```

3. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv myenv
   myenv\Scripts\activate

   # On macOS/Linux
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   # Development mode
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🌐 Deployment

### Deploy to Render

1. **Fork/Push this repository to GitHub**

2. **Sign up/Login to [Render](https://render.com)**

3. **Create a new Web Service**
   - Connect your GitHub repository
   - Select the `movie-recommender-sys` repository

4. **Configure the service**
   - **Name**: `movie-recommender-system`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Choose based on your needs (Free tier available)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically install Git LFS and download the model files
   - Your app will be live at: `https://your-app-name.onrender.com`

### Deploy to Heroku

1. **Install Heroku CLI**

2. **Login and create app**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Install Heroku Git LFS buildpack**
   ```bash
   heroku buildpacks:add https://github.com/raxod502/heroku-buildpack-git-lfs
   heroku buildpacks:add heroku/python
   ```

4. **Deploy**
   ```bash
   git push heroku main
   heroku open
   ```

## 🎯 How It Works

1. **User Input**: Enter a movie title in the search box
2. **Matching**: The system finds the closest match in the database
3. **Similarity Calculation**: Uses pre-computed cosine similarity scores
4. **Recommendations**: Returns top 5 most similar movies
5. **Display**: Shows recommendations in a clean, formatted list

## 🔧 Configuration

### Environment Variables

The app uses the following environment variables (optional):

- `PORT`: Server port (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (default: disabled for production)

Set via Render dashboard or `.env` file locally:
```bash
PORT=5000
FLASK_DEBUG=0
```

## 📊 Model Information

- **movie_list.pkl**: Contains movie metadata and titles (~11 MB)
- **similarity.pkl**: Precomputed cosine similarity matrix (~176 MB)
- Both files are tracked using Git LFS for efficient version control

## 🧪 Testing Locally

```bash
# Activate virtual environment
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # macOS/Linux

# Run the app
python app.py

# Test in browser
# Navigate to http://localhost:5000
# Try searching: "Avatar", "Inception", "The Dark Knight"
```

## 🐛 Troubleshooting

### Git LFS Issues
```bash
# Reinstall Git LFS
git lfs install --force

# Pull LFS files
git lfs pull
```

### Missing Dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Port Already in Use
```bash
# Change port in app.py or set environment variable
set PORT=8000  # Windows
export PORT=8000  # macOS/Linux
```

### Model Files Not Found
Ensure Git LFS pulled the files:
```bash
git lfs ls-files
# Should show: movie_list.pkl and similarity.pkl
```

## 📝 Development

To modify the recommendation algorithm:

1. Update the similarity computation in your data preprocessing script
2. Regenerate `similarity.pkl`
3. Test locally with `python app.py`
4. Commit and push changes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Ayush Kumar**
- GitHub: [@ayushhkr](https://github.com/ayushhkr)
- Repository: [movie-recommender-sys](https://github.com/ayushhkr/movie-recommender-sys)
- Live App: [https://movie-recommender-sys-zabp.onrender.com](https://movie-recommender-sys-zabp.onrender.com)

## 🙏 Acknowledgments

- Movie dataset sourced from [TMDB/IMDb]
- Built with Flask and scikit-learn
- Deployed on Render

---

⭐ Star this repo if you found it helpful!
