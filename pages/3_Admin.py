import streamlit as st
from utils.auth import USERS

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to access this page.")
    st.stop()  # Stop execution if not logged in

st.title("Admin Management")

# Check if the user is an admin
if st.session_state.user == "admin":
    st.write("### User Management")

    # Display current users
    st.write("#### Current Users")
    for username, password in USERS.items():
        st.write(f"- **{username}**")
        if st.button(f"Delete {username}", key=f"delete_{username}"):
            del USERS[username]
            st.success(f"User {username} deleted!")

    # Add new user
    st.write("#### Add New User")
    new_user = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Add User"):
        if new_user in USERS:
            st.error("User already exists!")
        else:
            USERS[new_user] = new_password
            st.success(f"User {new_user} added successfully!")
else:
    st.error("You do not have admin access.")