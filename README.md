# Movie_Recommendation_System
This repository provides a Movie Recommendation system using Content-based filtering and cosine similarity. The system recommends movies similar to a selected movie applying text vectorization and cosine similarity. Movie metadata is fetched using the TMDb API, and the application is deployed with Streamlit for an interactive user interface.

##  Tech Stack Used

- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, NumPy, Scikit-learn, NLTK, Pickle, Requests, Gdown
- **Frontend:** Streamlit  
- **IDE:** Jupyter Notebook  
- **External API:** TMDb API

## Frontend
The frontend of the Movie Recommendation System is built using Streamlit, providing a clean, interactive, and responsive user interface(UI). Users can input a movie name and get top recommended movies instantly.

Here is the Screenshot of the interface:
<img width="1919" height="790" alt="image" src="https://github.com/user-attachments/assets/bd8d2eaf-7f8e-4642-af61-e70c437c9193" />

The application is deployed using Streamlit Community Cloud, allowing real-time interaction through a public web URL.

## Dataset Used
This project uses the **TMDb 5000 Movie Dataset**, which is publicly available on Kaggle.  This dataset was generated from The Movie Database API. This product uses the TMDb API but is not endorsed or certified by TMDb. Their API also provides access to data on many additional movies, actors and actresses, crew members, and TV shows. 
It consists of two main CSV files:
### 1.) tmdb_5000_movies.csv
Contains metadata about movies :
Movie title, Overview, Genres, Keywords, Popularity, Vote average, Vote count, Release date

### 2.) tmdb_5000_credits.csv
Contains information related to the movie cast and crew, including: Cast details (actors), Crew details (director, producers, etc.)
