import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6708be64dd4d1568e1529c0126bc075b&language=en-US".format(movie_id)
    data = requests.get(url).json()

    poster_path=data['poster_path']
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    index=movies[ movies['title']==movie ].index[0]
    scores=similarity[index]
    movies_list= list( enumerate(scores) )
    movies_list= sorted( movies_list, key=lambda x: x[1], reverse=True )

    recommended_movies= []
    recommended_movies_posters=[]
    for i in movies_list[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

        movie_id=movies.iloc[i[0]].movie_id #To get posters from API
        recommended_movies_posters.append( fetch_poster(movie_id) )

    return recommended_movies,recommended_movies_posters


movies=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

#Text
st.title("Movie Recommendation System")

#Widget
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values,
)

#Button
if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)

    #Lay out your app--> Columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

