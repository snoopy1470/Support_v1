import streamlit as st

# Hardcoded users (replace with a database or secure authentication later)
USERS = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2",
}

def login():
    st.title("🎫 Support Ticket System")
    st.markdown("---")
    st.write("Please log in to access the support ticket system.")

    # Login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Logged in successfully!")
                st.rerun()  # Refresh the app to show the main page
            else:
                st.error("Invalid username or password. Please try again.")