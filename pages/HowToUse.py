import streamlit as st

# Title and Introduction
st.title("InstaFetch Tool Instructions: Session ID and Data Generation")
st.markdown("Welcome to the InstaFetch Tool! This guide will walk you through the process of obtaining a session ID, using it to generate profile data, and filtering the data.  ")

## Step 1: Obtaining Your Session ID

with st.expander("Step 1: Obtaining Your Session ID"):
  st.subheader("To interact with Instagram's API, you need a session ID. Follow these steps to obtain it:")

  steps = [
    "**Log in to Instagram**: Open your web browser and log in to your Instagram account.",
    "**Open Developer Tools**: Right-click on the page and select 'Inspect' (or press `Ctrl+Shift+I` on Windows/Linux or `Cmd+Option+I` on macOS).",
    "**Navigate to the Application Tab**: In Developer Tools, go to the 'Application' tab.",
    "**Locate the Cookies**: In the left sidebar, expand the 'Cookies' section and select `https://www.instagram.com`.",
    "**Find the Session ID**: Look for the cookie named `sessionid`. Copy the value of this cookie; this is your session ID. For more information, visit [How to get Instagram session ID?](https://wpautomatic.com/how-to-get-instagram-session-id/).",
  ]

  for step in steps:
    st.markdown(f"- {step}")

## Step 2: Setting Your Session ID in the InstaFetch Tool

with st.expander("Step 2: Setting Your Session ID in the InstaFetch Tool"):
  st.subheader("Once you have your session ID, follow these steps to set it in the app:")

  set_steps = [
    "**Open the InstaFetch Streamlit App**: Run the following command in your terminal if you haven't already:  `bash streamlit run app.py(skip if you are using web vesion)`",
    "**Enter Your Session ID**: In the Streamlit app Home Page, find the input box for the session ID.",
    "**Paste the copied session ID**: Paste the copied session ID into the input field.",
    "**Click the 'Set Session ID' Button**: Press the button to set your session ID. You should see a confirmation message indicating that your session ID has been successfully set."
  ]

  for step in set_steps:
    st.markdown(f"- {step}")

## Step 3: Generating a Profile ID

with st.expander("Step 3: Generating a Profile ID"):
  st.subheader("Here's how to generate the profile ID of the account you want to analyze:")

  profile_steps = [
    "**Navigate to the PK ID Page**: Look for the section in the app labeled 'Profile ID Generator'.",
    "**Enter the Username**: Type the Instagram username of the profile you want to analyze.",
    "**Click the Button**: Press the button to generate the profile ID.",
    "**Recheck to View Profile Picture (Optional)**: After generating the profile ID, the tool will display the profile picture of the entered username. Click the button to view the profile picture.",
    "**Copy the Profile ID**: Once the profile ID is displayed, copy it to your clipboard."
  ]

  for step in profile_steps:
    st.markdown(f"- {step}")

## Step 4: Returning to the Home Page
with st.expander("Step 4: Returning to the Home Page"):
    st.markdown("Past PK ID in input box and set Pk ID")

## Step 5: Generating and Filtering Data

with st.expander("Step 5: Generating and Filtering Data"):
  st.subheader("Here's how to use the profile ID to fetch and filter data:")

  data_steps = [
    "**Navigate to the Get Data Page**",
    "**Click the 'Fetch Data' Button**: Press the button to generate the data associated with the profile ID.",
    "**Filter Data**: Use the filtering options available on the Manipulation Page to analyze specific aspects of the fetched data (e.g., engagement metrics, post types, etc.)."
  ]

  for step in data_steps:
    st.markdown(f"- {step}")    