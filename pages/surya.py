import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('Surya')
st.text("somethings")

df = pd.read_csv("Connecut census data - Sheet1 (1).csv")
df = df.iloc[3:]
print(df.columns.values)
yay = px.scatter(df,x="Population",y="Total",hover_data=["Town","Vacant"],title='Population V. Total Housing')
st.plotly_chart(yay)