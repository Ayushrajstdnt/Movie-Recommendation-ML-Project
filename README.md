# movie-recommender-system-tmdb-dataset
🎬 Movie Recommender System
A content-based movie recommendation system built with Machine Learning and deployed using Streamlit. The system analyzes movie metadata including genres, keywords, cast, and crew to suggest the most similar movies to the one you select.
🔗 Live Demo
Click here to view the live app — [https://your-app-link.streamlit.app](https://movie-recommendation-ml-project-ayush.streamlit.app/)
🚀 Features

Content-based filtering using cosine similarity
Real-time movie poster fetching via TMDB API
Netflix-style dark UI with smooth animations
Search and select from 5000+ movies
Instantly get top 5 similar movie recommendations

🛠️ Tech Stack

Python — Core programming language
Pandas and NumPy — Data cleaning and processing
Scikit-learn — Vectorization and cosine similarity
Streamlit — Web application framework
TMDB API — Fetching real-time movie posters
Git and GitHub — Version control and hosting

⚙️ How It Works

Movie metadata such as genres, keywords, cast, and crew is merged into a single tags column
Text data is vectorized using CountVectorizer with 5000 features
Cosine similarity is calculated between all movie vectors
When a movie is selected the top 5 most similar movies are returned
Movie posters are fetched in real time using the TMDB API

🧠 Machine Learning Details

Algorithm — Content-Based Filtering
Vectorization — Bag of Words using CountVectorizer
Similarity Metric — Cosine Similarity
Dataset — TMDB 5000 Movie Dataset from Kaggle
Total Movies — 4803

📌 What I Learned

Building a complete end-to-end machine learning project
Working with real-world movie datasets and cleaning messy data
Implementing NLP techniques like bag of words and cosine similarity
Integrating third-party REST APIs into a Python application
Deploying a machine learning model as a live web application
