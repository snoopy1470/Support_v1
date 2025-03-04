import streamlit as st
from utils.auth import login

# Check if user is logged in
if "logged_in" not in st.session_state:
    login()  # Show login page
else:
    st.title("Support Ticket System")
    st.write(f"Welcome, **{st.session_state.user}**!")  # Display username