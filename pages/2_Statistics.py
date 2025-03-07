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

    # Key Metrics
    st.write("### Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Tickets", len(tickets))
    with col2:
        st.metric("Open Tickets", len(tickets[tickets["Status"] == "Open"]))
    with col3:
        st.metric("In Progress Tickets", len(tickets[tickets["Status"] == "In Progress"]))
    with col4:
        st.metric("Closed Tickets", len(tickets[tickets["Status"] == "Closed"]))

    # Ticket Status Distribution
    st.write("### Ticket Status Distribution")
    status_counts = tickets["Status"].value_counts()
    fig1 = px.bar(status_counts, x=status_counts.index, y=status_counts.values, labels={"x": "Status", "y": "Count"})
    st.plotly_chart(fig1)

    # Assignee-wise Distribution
    st.write("### Assignee-wise Ticket Distribution")
    if tickets["Assignee"].nunique() > 0:  # Check if there are assignees
        assignee_counts = tickets["Assignee"].value_counts()
        fig2 = px.pie(assignee_counts, values=assignee_counts.values, names=assignee_counts.index, title="Tickets by Assignee")
        st.plotly_chart(fig2)
    else:
        st.info("No assignees found. Assign tickets on the Dashboard!")

    # Weekly Ticket Trends
    st.write("### Weekly Ticket Trends")
    tickets["Created_At"] = pd.to_datetime("today")  # Simulate creation date for demonstration
    weekly_trends = tickets.resample("W", on="Created_At").size()
    fig3 = px.line(weekly_trends, title="Tickets Created Per Week", labels={"value": "Number of Tickets", "index": "Week"})
    st.plotly_chart(fig3)