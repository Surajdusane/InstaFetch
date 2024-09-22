import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to filter the DataFrame based on user inputs
def filter_data(df, min_likes, max_likes, min_comments, max_comments, min_views, max_views, start_date, end_date, sort_by, ascending):
    # Convert 'dates' column to datetime if not already
    df['dates'] = pd.to_datetime(df['dates'], errors='coerce')

    # Filter by likes
    if min_likes is not None:
        df = df[df['likes'] >= min_likes]
    if max_likes is not None:
        df = df[df['likes'] <= max_likes]

    # Filter by comments
    if min_comments is not None:
        df = df[df['comments'] >= min_comments]
    if max_comments is not None:
        df = df[df['comments'] <= max_comments]

    # Filter by views
    if min_views is not None:
        df = df[df['views'] >= min_views]
    if max_views is not None:
        df = df[df['views'] <= max_views]

    # Filter by date range
    if start_date:
        df = df[df['dates'] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df['dates'] <= pd.to_datetime(end_date)]

    # Sort the DataFrame
    if sort_by:
        df = df.sort_values(by=sort_by, ascending=ascending)

    return df

# Streamlit UI
st.set_page_config(page_title="CSV Data Manipulator",layout="wide")

# Toggle button for using generated CSV or uploading CSV
use_generated_csv = st.toggle("Use Generated CSV", value=True)

# Generated CSV Data
if use_generated_csv:
    # Load the generated CSV
    try:
        df = pd.read_csv('instagram_data.csv')  # Make sure this file exists
    except FileNotFoundError:
        st.error("Generated CSV not found. Please check the file.")
else:
    # Upload a CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Uploaded CSV successfully.")

# Display DataFrame
if 'df' in locals():
    st.write("Raw Data:")
    st.dataframe(df)

    # Filter options
    st.sidebar.header("Filters")

    # Likes filters
    min_likes = st.sidebar.number_input("Min Likes", value=int(df['likes'].min()))
    max_likes = st.sidebar.number_input("Max Likes", value=int(df['likes'].max()) if not df['likes'].isnull().all() else 0)

    # Comments filters
    min_comments = st.sidebar.number_input("Min Comments", value=int(df['comments'].min()))
    max_comments = st.sidebar.number_input("Max Comments", value=int(df['comments'].max()) if not df['comments'].isnull().all() else 0)

    # Views filters
    min_views = st.sidebar.number_input("Min Views", value=int(df['views'].min()))
    max_views = st.sidebar.number_input("Max Views", value=int(df['views'].max()) if not df['views'].isnull().all() else 0)

    # Date filters
    last_days = st.sidebar.number_input("Filter Date Range (Last Days)", value=365, min_value=1)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=last_days)

    # Date range filter inputs
    start_date = st.sidebar.date_input("Start Date", start_date)
    end_date = st.sidebar.date_input("End Date", end_date)

    # Sorting options
    sort_by = st.sidebar.selectbox("Sort By", options=['likes', 'comments', 'views', 'dates'], index=0)
    ascending = st.sidebar.checkbox("Ascending Order", value=True)

    # Apply filters
    filtered_df = filter_data(df, min_likes, max_likes, min_comments, max_comments, min_views, max_views, start_date, end_date, sort_by, ascending)

    # Display filtered DataFrame
    st.write("Filtered Data:")
    st.dataframe(filtered_df)

    # Download button for filtered CSV
    csv = filtered_df.to_csv(index=False)
    st.download_button("Download Filtered CSV", data=csv, file_name='filtered_instagram_data.csv', mime='text/csv')
