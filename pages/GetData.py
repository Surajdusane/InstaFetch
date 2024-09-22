import streamlit as st
import requests
import json
import csv
import datetime
import pandas as pd 
import time  
import random

st.set_page_config(
    page_title="Get Data",
    
)

# Function to convert Unix timestamp to a readable string
def convert_unix_timestamp(timestamp):
    dt_object = datetime.datetime.utcfromtimestamp(timestamp)
    return dt_object.strftime('%Y-%m-%d %H:%M:%S')

# Function to get Instagram data
def get_instagram_data(user_id, session, query_hash):
    all_posts = []
    end_cursor = None
    has_next_page = True

    while has_next_page:
        variables = f'{{"id":"{user_id}","first":12,"after":"{end_cursor}"}}' if end_cursor else f'{{"id":"{user_id}","first":12}}'
        url = f"https://www.instagram.com/graphql/query/?query_hash={query_hash}&variables={variables}"

        # Delay to avoid hitting rate limits
        sleep_time = random.randint(2,6)
        print(sleep_time)
        time.sleep(sleep_time) 
        response = session.get(url)
        
        # Respect Instagram's rate limit
        if response.status_code != 200:
            st.error("Error fetching data. Please try again later.")
            break

        data = response.json()

        if 'data' not in data or 'user' not in data['data']:
            st.error("Error fetching data:", data)
            break

        posts = data['data']['user']['edge_owner_to_timeline_media']['edges']
        all_posts.extend(posts)

        page_info = data['data']['user']['edge_owner_to_timeline_media']['page_info']
        end_cursor = page_info['end_cursor']
        has_next_page = page_info['has_next_page']

    return all_posts

# Streamlit app layout
st.title("Instagram Data Fetcher")

# Button to fetch data
if st.button("Fetch Data"):
    session_id = st.session_state['session_id']
    session = requests.Session()
    session.cookies.set('sessionid', session_id)

    user_id = st.session_state["pk_id"]

    if user_id == "No users found.":
        st.error("User not found. Please check the username.")
    else:
        st.success(f"User ID: {user_id}")
        
        query_hash = "472f257a40c653c64c666ce877d59d2b"
        data = get_instagram_data(user_id, session, query_hash)

        if data:
            st.write(f"Fetched {len(data)} posts.")
            # Convert to CSV
            csv_data = []
            for post in data:
                media_id = str(post["node"]["id"])
                shortcode = post["node"]["shortcode"]
                link = f"https://www.instagram.com/p/{shortcode}"
                likes = post["node"]["edge_media_preview_like"]["count"]
                comments = post["node"]["edge_media_to_comment"]["count"]
                views = post["node"].get("video_view_count", 0) if post["node"]["is_video"] else 0
                date = convert_unix_timestamp(int(post["node"]["taken_at_timestamp"]))

                csv_data.append({
                    'media_id': str(media_id),
                    'shortcode': shortcode,
                    'link': link,
                    'likes': likes,
                    'comments': comments,
                    'views': views,
                    'dates': date
                })
            
            user_df = pd.DataFrame(csv_data)
            st.table(user_df)

            # Provide download link for CSV
            csv_file = "instagram_data.csv"
            with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['media_id', 'shortcode', 'link', 'likes', 'comments', 'views', 'dates']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)

            st.download_button("Download CSV", data=open(csv_file, 'rb'), file_name=csv_file, mime='text/csv')

