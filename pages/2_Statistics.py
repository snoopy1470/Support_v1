import streamlit as st
import pandas as pd
import plotly.express as px

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