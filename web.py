import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App.")
st.subheader("This my To-do app.")

st.write("This app is used to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Enter a new to-do.......",
              on_change=add_todo,key="new_todo")
st.session_state
