import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Get PK ID",
)

def get_users(username, sessionid):
    url = f"https://www.instagram.com/web/search/topsearch/?query={username}"
    
    session = requests.Session()
    session.cookies.set('sessionid', sessionid)

    response = session.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "users" in data and len(data["users"]) > 0:
            return data["users"]  # Return all user data
        else:
            return None  # No users found
    else:
        st.error(f"Error fetching data: {response.status_code} - {response.text}")
        return None

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = ''
if 'pk_id' not in st.session_state:
    st.session_state['pk_id'] = None

st.title("Instagram User Search")

# Input field for session ID
session_id = st.session_state['session_id'] 

username = st.text_input("Enter Instagram username:")

if st.button("Search"):
    if session_id and username:
        users = get_users(username, session_id)
        
        if users:
            # Prepare data for the table
            user_data = []
            for user_info in users:
                user = user_info["user"]
                pk_id = user["pk"]
                user_name = user["username"]
                
                user_data.append({"Username": user_name, "PK ID": pk_id})

            # Create a DataFrame and display it
            user_df = pd.DataFrame(user_data)
            st.table(user_df)

            for user_info in users:
                user = user_info["user"]  # Reference the current user
                button = st.link_button(user["username"], user["profile_pic_url"]) 

        else:
            st.warning("No users found.")
    else:
        st.warning("Please enter both session ID and username.")