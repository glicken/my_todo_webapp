import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title('Todo App')
st.subheader('Enter your todo:')
st.write('Add Todo')
st.checkbox('Add Todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    

st.text_input('Enter a Todo:', placeholder='Add Todo', on_change=add_todo,
              key='new_todo')

st.session_state 
