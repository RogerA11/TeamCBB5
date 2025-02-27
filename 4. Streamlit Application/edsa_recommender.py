"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from PIL import Image

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Solution Overview","Exploratory Data Analysis","About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Menu", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.image('resources/imgs/project_blackbox.jpeg',use_column_width=True)
        st.write("## Solutions Overview")
        st.write("In today’s technology driven world, recommender systems are socially and \
        economically critical to ensure that individuals can make optimised choices \
        surrounding the content they engage with on a daily basis. One application where \
        this is especially true is movie recommendations; where intelligent algorithms can \
        help viewers find great titles from tens of thousands of options.")
        st.write("Recommender Systems are a type of information filtering system as they \
        improve the quality of search results and provides items that are more relevant to \
        the search item or are related to the search history of the user.")
        st.write("Let's view a breakdown of these recommender systems as applied in **Project \
        Blackbox** as providing an accurate and robust solutions to this challenge has immense \
        economic potential, with consumers of the system being personalised recommendations - \
        generating platform affinity for the streaming services which best facilitates their \
        audience's viewing.")
        st.image('resources/imgs/Recommender_systems.png',use_column_width=True)

    if page_selection == "Exploratory Data Analysis":
        # 1st block
        st.image('resources/imgs/project_blackbox.jpeg',use_column_width=True)
        st.title("Exploratory Data Analysis")
        st.write('The three major features included in our Recommender System Algorithm: \
          \n  - Movie Year Release\n  - Movie Genre\n - Movie Director')
        st.write('Displayed below you can view their respective visualization insights as well \
          as a brief explanation thereof')

        # 2nd block
        st.write("### Movie Year Release")
        st.image('resources/imgs/yearly_released_movies_1.png',use_column_width=True)
        st.write('Most of the movies in our dataset has been released thoughout the 1990s. \
          Looking at the graph, the count starts becoming more dense with respect to movies released in our current century. \
          This is good. It means the distribution of movies with respect to timeline, is relatively even')

        # 3rd block
        st.write("### Movie Genre")
        st.image('resources/imgs/movie_genre_distribution.png',use_column_width=True)
        st.write('Genres play an important role in movie recommender systems. \
          Drama movies are maximum in number as compared to Film-Noir and Documentary movies.')

        # 4th block
        st.write("### Movie Director")
        st.image('resources/imgs/popular_movie_directors.png',use_column_width=True)
        st.write('The top 10 directors of movies in our dataset. Directors play an important \
          role in narrowing down preferences when it comes to recommender systems. The top 4 directors have \
          a dense amount of movies that have been reviewed.')


    if page_selection == "About Us":
        st.title("Meet the Data Science Team")
        st.image('resources/imgs/project_blackbox.jpeg',use_column_width=True)
        njabulo = Image.open('resources/imgs/Njabulo.jpg')
        joshan = Image.open('resources/imgs/Josh.jpg')
        roger = Image.open('resources/imgs/Roger.jpg')
        william = Image.open('resources/imgs/William.jpg')
        gabrielle = Image.open('resources/imgs/Gabrielle.jpg')
        wade = Image.open('resources/imgs/Wade.jpg')
        c1,c2,c3 = st.columns(3)
        with c1:
            st.image(njabulo, caption="Njabulo Mkhwanazi (Business Analyst)",use_column_width='always')
            st.image(joshan, caption="Joshan Dooki (ML Engineer)",use_column_width='always')
        with c2:
            st.write()
            st.image(roger,caption="Roger Arendse (Data Scientist)",use_column_width='always')
            st.image(william,caption="William Hlatshwayo (Developer)",use_column_width='always')
        with c3:
            st.write()
            st.image(gabrielle,caption="Gabrielle Peria (Statistician)",use_column_width='always')
            st.image(wade, caption="Wade Jacobs (Security Specialist)",use_column_width='always')



        # local_css('resources/pages/html_style.css')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
