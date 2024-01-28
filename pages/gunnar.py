import streamlit as st
import pandas as pd
import numpy as np
from langchain_experimental.llm_symbolic_math.base import LLMSymbolicMathChain
from langchain_openai import OpenAI
import streamlit as st


st.title('Gunnar')

st.image('https://variety.com/wp-content/uploads/2021/07/Rick-Astley-Never-Gonna-Give-You-Up.png?w=1024')
st.write("Never gonna give you up")
st.write("Never gonna let you down")
st.write("Never gonna run around and desert you")

llm = OpenAI(temperature=0)
llm_symbolic_math = LLMSymbolicMathChain.from_llm(llm)

st.title("Symbolic Math Chain")

question=st.text_input("Enter your question here")

if st.button("Submit"):
    answer = llm_symbolic_math.run(question)
    st.write(answer)

