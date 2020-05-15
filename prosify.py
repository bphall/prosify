import streamlit as st
import markovify
import numpy as np

text = open("ulysses.txt", "r").read()

# Build the model.
text_model = markovify.Text(text)

number = st.selectbox("Type in the number of Markov-generated sentences you'd like:",
                             np.arange(1, 21, 1))

for i in range(number):
    st.write(text_model.make_sentence())
