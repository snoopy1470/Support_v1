import streamlit as st
import pandas as pd

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to access this page.")
    st.stop()  # Stop execution if not logged in

st.title("Dashboard gang")


# Initialize session state for tickets
if "tickets" not in st.session_state:
    st.session_state.tickets = pd.DataFrame(columns=["ID", "Title", "Status", "Priority", "Assignee", "Description"])

# Function to apply color coding based on status
def get_status_color(status):
    if status == "Open":
        return "🔴 Open"  # Red circle emoji
    elif status == "In Progress":
        return "🔵 In Progress"  # Blue circle emoji
    elif status == "Closed":
        return "🟢 Closed"  # Green circle emoji
    else:
        return "⚪ Unknown"  # White circle emoji

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
        new_ticket_df = pd.DataFrame([new_ticket])
        st.session_state.tickets = pd.concat([st.session_state.tickets, new_ticket_df], ignore_index=True)
        st.success("Ticket created successfully!")

# Display tickets
st.write("### Tickets")
if not st.session_state.tickets.empty:
    for index, ticket in st.session_state.tickets.iterrows():
        with st.expander(f"Ticket #{ticket['ID']}: {ticket['Title']}"):
            # Display ticket details with emojis for status
            st.write(f"**Status:** {get_status_color(ticket['Status'])}")
            st.write(f"**Priority:** {ticket['Priority']}")
            st.write(f"**Assignee:** {ticket['Assignee']}")
            st.write(f"**Description:** {ticket['Description']}")

            # Edit and Delete buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Edit Ticket #{ticket['ID']}", key=f"edit_{ticket['ID']}"):
                    st.session_state.edit_ticket_id = ticket['ID']  # Store the ticket ID being edited
            with col2:
                if st.button(f"Delete Ticket #{ticket['ID']}", key=f"delete_{ticket['ID']}"):
                    st.session_state.tickets = st.session_state.tickets.drop(index)
                    st.success(f"Ticket #{ticket['ID']} deleted!")
                    st.rerun()

            # Edit form (only shown if the edit button is clicked)
            if "edit_ticket_id" in st.session_state and st.session_state.edit_ticket_id == ticket['ID']:
                with st.form(f"edit_form_{ticket['ID']}"):
                    new_title = st.text_input("Title", value=ticket['Title'])
                    new_status = st.selectbox("Status", ["Open", "In Progress", "Closed"], index=["Open", "In Progress", "Closed"].index(ticket['Status']))
                    new_priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(ticket['Priority']))
                    new_assignee = st.text_input("Assignee", value=ticket['Assignee'])
                    new_description = st.text_area("Description", value=ticket['Description'])
                    if st.form_submit_button("Save Changes"):
                        st.session_state.tickets.at[index, "Title"] = new_title
                        st.session_state.tickets.at[index, "Status"] = new_status
                        st.session_state.tickets.at[index, "Priority"] = new_priority
                        st.session_state.tickets.at[index, "Assignee"] = new_assignee
                        st.session_state.tickets.at[index, "Description"] = new_description
                        st.success(f"Ticket #{ticket['ID']} updated successfully!")
                        del st.session_state.edit_ticket_id  # Clear the edit state
                        st.rerun()
else:
    st.info("No tickets found. Create a new ticket above!")

    