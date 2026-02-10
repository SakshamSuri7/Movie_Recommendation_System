# Movie_Recommendation_System
This repository provides a Movie Recommendation system using Content-based filtering and cosine similarity. The system recommends movies similar to a selected movie applying text vectorization and cosine similarity. Movie metadata is fetched using the TMDb API, and the application is deployed with Streamlit for an interactive user interface.

##  Tech Stack Used

- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, NumPy, Scikit-learn, NLTK, Pickle, Requests
- **Frontend:** Streamlit  
- **IDE:** Jupyter Notebook  
- **External API:** TMDb API

## Dataset Used

This project uses the **TMDb 5000 Movie Dataset**, which is publicly available on Kaggle.  
It consists of two main CSV files:

### 1.) tmdb_5000_movies.csv
Contains metadata about movies, including:
- Movie title
- Overview
- Genres
- Keywords
- Popularity
- Vote average
- Vote count
- Release date

### 2.) tmdb_5000_credits.csv
Contains information related to the movie cast and crew, including:
- Cast details (actors)
- Crew details (director, producers, etc.)
