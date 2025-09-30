# app.py
import streamlit as st
import todo

st.title("📝 To-Do List App")

# Load tasks
tasks = todo.load_tasks()

# Input box
new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task.strip() != "":
        todo.add_task(new_task)
        st.success(f"✅ Task added: {new_task}")
        st.rerun()

    else:
        st.warning("⚠️ Task cannot be empty")

# Display tasks
st.subheader("📋 Your Tasks")
if tasks:
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([3,1])
        col1.write(f"{i+1}. {task}")
        if col2.button("🗑️ Remove", key=i):
            removed = todo.remove_task(i)
            st.success(f"Removed: {removed}")
            st.rerun()

else:
    st.info("No tasks found! Add one above ☝️")
