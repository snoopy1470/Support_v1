import streamlit as st
import pandas as pd

st.title("Dashboard")

# Initialize session state for tickets
if "tickets" not in st.session_state:
    st.session_state.tickets = pd.DataFrame(columns=["ID", "Title", "Status", "Priority", "Assignee", "Description"])

# Form to create a new ticket
st.write("### Create New Ticket")
with st.form("new_ticket"):
    title = st.text_input("Title")
    status = st.selectbox("Status", ["Open", "In Progress", "Closed"])
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    assignee = st.text_input("Assignee")
    description = st.text_area("Description")
    if st.form_submit_button("Create Ticket"):
        new_ticket = {
            "ID": len(st.session_state.tickets) + 1,
            "Title": title,
            "Status": status,
            "Priority": priority,
            "Assignee": assignee,
            "Description": description,
        }
        # Use pd.concat() instead of append
        new_ticket_df = pd.DataFrame([new_ticket])
        st.session_state.tickets = pd.concat([st.session_state.tickets, new_ticket_df], ignore_index=True)
        st.success("Ticket created successfully!")

# Display tickets
st.write("### Tickets")
if not st.session_state.tickets.empty:
    for index, ticket in st.session_state.tickets.iterrows():
        with st.expander(f"Ticket #{ticket['ID']}: {ticket['Title']}"):
            st.write(f"**Status:** {ticket['Status']}")
            st.write(f"**Priority:** {ticket['Priority']}")
            st.write(f"**Assignee:** {ticket['Assignee']}")
            st.write(f"**Description:** {ticket['Description']}")
            if st.button(f"Delete Ticket #{ticket['ID']}", key=f"delete_{ticket['ID']}"):
                st.session_state.tickets = st.session_state.tickets.drop(index)
                st.success(f"Ticket #{ticket['ID']} deleted!")
else:
    st.info("No tickets found. Create a new ticket above!")