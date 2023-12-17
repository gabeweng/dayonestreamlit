import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Wikipedia Searcher')

wikis = pd.read_html('https://meta.wikimedia.org/wiki/List_of_Wikipedias')[0]

wikis['Display'] = wikis['Language'].str.cat(wikis['Language (local)'], sep=" - ")
language = st.selectbox('Language', wikis['Display'].values)
language_code = wikis[wikis['Display'] == language]['Wiki'].values[0]

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
        if i['thumbnail'] != None:
          st.image("https:" + i['thumbnail']['url'], width=200)
        if i['description'] != None:
          st.write(i['description'])
        st.markdown(i['excerpt'], unsafe_allow_html=True)

st.image('https://th.bing.com/th/id/OIP.h1ZcvEisR9OnGTNLAOuKaQHaFj?rs=1&pid=ImgDetMain')