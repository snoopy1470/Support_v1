# utils/auth.py
import streamlit as st

# Hardcoded users (replace with a database or secure authentication later)
USERS = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2",
}

def login():
    st.title("Support Ticket System")
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")