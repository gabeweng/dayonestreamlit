import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Wikipedia Searcher')

language_code = 'en'
search_query = st.text_input('Search Query', 'Capital of France')
number_of_results = st.number_input('Number of results', 1, 10, 1)

headers = {
  # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
  'User-Agent': 'DayOneStreamlit'
}

base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
url = base_url + language_code + endpoint
parameters = {'q': search_query, 'limit': number_of_results}
if st.button('Search'):
    response = requests.get(url, headers=headers, params=parameters)
    response_data = response.json()
    st.write(response_data)
    # st.write(response_data['pages'][0]['description'])
    for i in (response_data['pages']):
        st.header(i['title'])
        st.image("https:" + i['thumbnail']['url'], width=200)
        st.write(i['description'])
        st.markdown(i['excerpt'], unsafe_allow_html=True)

st.image('https://th.bing.com/th/id/OIP.h1ZcvEisR9OnGTNLAOuKaQHaFj?rs=1&pid=ImgDetMain')