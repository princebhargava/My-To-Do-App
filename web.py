import streamlit as st
import functions

todos = functions.get_todos()
st.title("My To-Do App")
st.subheader("This my To-do app.")

st.write("This app is used to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter a new to-do.......")