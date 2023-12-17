import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_csv("Hot 100 Audio Features.csv")
df.rename(columns={'Performer': 'Songs'}, inplace=True)



df = df.dropna(subset=['Performer','Songs', 'spotify_genre'])


st.title('top100')


st.write(df)





