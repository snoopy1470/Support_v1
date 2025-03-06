import streamlit as st
from utils.auth import login

# Set page configuration
st.set_page_config(page_title="Support Ticket System", page_icon="🎫", layout="wide")

# Check if user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show login page if not logged in
if not st.session_state.logged_in:
    login()
else:
    st.title("Support Ticket System")
    st.write(f"Welcome, **{st.session_state.user}**!")  # Display username

    # Logout button in the sidebar
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.success("Logged out successfully!")
        st.rerun()  # Refresh the app to show the login page