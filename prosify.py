import streamlit as st
import markovify

text = open("ulysses.txt", "r").read()

# Build the model.
text_model = markovify.Text(text)

user_input = int(st.text_input("Type in the number of Markov-generated sentences you'd like. (Max 100)"))

if type(user_input) == int:
    if user_input <= 100:
        for i in range(user_input):
            st.write(text_model.make_sentence())