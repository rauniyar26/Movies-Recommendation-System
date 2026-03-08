import streamlit as st
import pickle
import pandas as pd

# page layout
st.set_page_config(page_title="Movie Recommender", layout="wide")

# load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# title
st.markdown(
    "<h1 style='text-align: center;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)

st.write("")

# movie dropdown
selected_movie_name = st.selectbox(
    "Select a movie",
    movies["title"].values
)

# recommend button
if st.button("Recommend Movies 🍿"):

    recommendations = recommend(selected_movie_name)

    st.subheader("Top 5 Recommended Movies")

    # create 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.success(recommendations[0])

    with col2:
        st.success(recommendations[1])

    with col3:
        st.success(recommendations[2])

    with col4:
        st.success(recommendations[3])

    with col5:
        st.success(recommendations[4])