import pickle
import streamlit as ast
import requests
def fetch_poster(movie_id):
    url= "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data= requests.get(url)
    data= data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendent_movies_name= []
    recommendent_movies_poster= []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommendent_movies_poster.append(fetch_poster(movie_id))
        recommendent_movies_name.append(movies.iloc[i[0]].title)
    return recommendent_movies_name, recommendent_movies_poster

ast.header("Movies Recommendation System Using Maching Learning")
movies = pickle.load(open('artificats/movie_list.pkl','rb'))
similarity = pickle.load(open('artificats/similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie =ast.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)
if ast.button('Show recommendation'):
    recommendent_movies_name, recommendent_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = ast.columns(5)
    with col1:
        ast.text(recommendent_movies_name[0])
        ast.image(recommendent_movies_poster[0])
    with col2:
        ast.text(recommendent_movies_name[1])
        ast.image(recommendent_movies_poster[1])
    with col3:
        ast.text(recommendent_movies_name[2])
        ast.image(recommendent_movies_poster[2])
    with col4:
        ast.text(recommendent_movies_name[3])
        ast.image(recommendent_movies_poster[3])
    with col5:
        ast.text(recommendent_movies_name[4])
        ast.image(recommendent_movies_poster[4])