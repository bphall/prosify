import streamlit as st
import markovify
import numpy as np


text = open("ulysses.txt", "r").read()

# Build the model
text_model = markovify.Text(text)

st.title('Markov Prose Generator for Ulysses, by James Joyce')
number = st.selectbox("Select the number of sentences you'd like:",
                      np.arange(1, 101, 1))

for i in range(number):
    st.write(text_model.make_sentence())
