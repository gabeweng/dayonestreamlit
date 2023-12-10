import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



df = pd.read_csv("spotify_songs.csv")
df.rename(columns={'track_popularity': 'popularity'}, inplace=True)



df = df.dropna(subset=['popularity','danceability', 'track_name'])


st.title('Spotify')


st.write(df)



# Create interactive dot plot using Plotly Express
fig = px.scatter(df,
                 x='danceability',
                 y='popularity',
                 color='playlist_subgenre',
                 hover_data=['track_name', 'playlist_name', 'track_artist'],
                 labels={'danceability': 'Danceability', 'track_name': 'Track Name', 'playlist_name': 'Playlist Name', 'track_artist': 'Artist', 'popularity': 'Popularity', 'playlist_subgenre': 'Playlist SubGenre'},
                 title='Interactive Dot Plot of Worst Rated Movies')

# Display the plot using Streamlit
st.plotly_chart(fig)

