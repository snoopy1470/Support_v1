import streamlit as st
import pandas as pd
import plotly.express as px

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to access this page.")
    st.stop()  # Stop execution if not logged in

st.title("Statistics")


# Check if tickets exist
if "tickets" not in st.session_state or st.session_state.tickets.empty:
    st.warning("No tickets found. Create tickets on the Dashboard!")
else:
    tickets = st.session_state.tickets

    # Ticket status distribution
    st.write("### Ticket Status Distribution")
    status_counts = tickets["Status"].value_counts()
    st.bar_chart(status_counts)

    # Assignee-wise ticket distribution
    st.write("### Assignee-wise Ticket Distribution")
    assignee_counts = tickets["Assignee"].value_counts()
    fig1 = px.pie(assignee_counts, values=assignee_counts, names=assignee_counts.index, title="Tickets by Assignee")
    st.plotly_chart(fig1)

    # Weekly ticket trends
    st.write("### Weekly Ticket Trends")
    tickets["Created_At"] = pd.to_datetime("today")  # Simulate creation date
    weekly_trends = tickets.resample("W", on="Created_At").size()
    fig2 = px.line(weekly_trends, title="Tickets Created Per Week")
    st.plotly_chart(fig2)