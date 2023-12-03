import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


def convert_duration(duration):
    print(duration)
    duration = duration.replace('m','')
    hr,min = duration.split('h ')
    min = int(min)
    hr = int(hr)
    return hr*60 + min
df = pd.read_csv("lowest_ranked_movies_data.csv")

# st.write(df)


df = df.dropna(subset=['duration'])

df['duration_minutes'] = df['duration'].apply(convert_duration)

st.title('Movies')


st.write(df)

# Sidebar for filtering data
min_duration = st.sidebar.slider('Minimum Duration (minutes)', min_value=0, max_value=df['duration_minutes'].max(), value=0)
max_duration = st.sidebar.slider('Maximum Duration (minutes)', min_value=min_duration, max_value=df['duration_minutes'].max(), value=df['duration_minutes'].max())
min_rating = st.sidebar.slider('Minimum Rating', min_value=df['rating'].min(), max_value=df['rating'].max(), value=df['rating'].min())
max_rating = st.sidebar.slider('Maximum Rating', min_value=min_rating, max_value=df['rating'].max(), value=df['rating'].max())

filtered_df = df[(df['duration_minutes'] >= min_duration) & (df['duration_minutes'] <= max_duration) & (df['rating'] >= min_rating) & (df['rating'] <= max_rating)]

# Create interactive dot plot using Plotly Express
fig = px.scatter(filtered_df,
                 x='duration_minutes',
                 y='rating',
                 color='certification',
                 color_discrete_map={
                "Not Rated": "gray",
                "G": "green",
                "PG": "green",
                "PG-13": "blue",
                "R": "red",
                "TV-MA": "black"},
                 hover_data=['name', 'year', 'genre'],
                 labels={'duration_minutes': 'Duration (minutes)', 'rating': 'Rating', 'genre': 'Genres'},
                 title='Interactive Dot Plot of Worst Rated Movies')

# Display the plot using Streamlit
st.plotly_chart(fig)

