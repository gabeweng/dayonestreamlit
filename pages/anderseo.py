import streamlit as st
import pandas as pd
import numpy as np

st.title('Anderson')
st.image('https://cdn.vox-cdn.com/thumbor/HFdhANVIrxsJzT5cv9U5n2cH5tk=/0x0:960x540/1200x800/filters:focal(404x194:556x346)/cdn.vox-cdn.com/uploads/chorus_image/image/70931916/p16_01_m.0.jpg')
df = pd.read_csv("pokemon.csv")

pokemon1 = st.text_input("Pokemon One", value="", placeholder="Enter first Pokémon name")
pokemon2 = st.text_input("Pokemon Two", value="", placeholder="Enter second Pokémon name")

if st.button('Show Comparison'):
    if pokemon1 and pokemon2:
        pokemon1_data = df[df['name'].str.lower() == pokemon1.lower()]
        pokemon2_data = df[df['name'].str.lower() == pokemon2.lower()]
        if not pokemon1_data.empty and not pokemon2_data.empty:
            pokemon1_total = pokemon1_data['total'].iloc[0]
            pokemon2_total = pokemon2_data['total'].iloc[0]
            delta = pokemon1_total - pokemon2_total
            delta_str = str(delta)
            st.metric(f"{pokemon1} vs {pokemon2}", 
                      f"{pokemon1_total} vs {pokemon2_total}", 
                      delta_str)
        else:
            st.error("One or both Pokémon not found. Please check the names and try again.")
    else:
        st.error("Please enter the names of both Pokémon.")