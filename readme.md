Sure! Here’s a detailed instruction guide formatted for a Streamlit page:

```markdown
# InstaFetch Tool Instructions: Session ID and Data Generation

Welcome to the InstaFetch Tool! This guide will walk you through the process of obtaining a session ID, using it to generate profile data, and filtering the data. 

## Step 1: Obtaining Your Session ID

To interact with Instagram's API, you need a session ID. Follow these steps to obtain it:

1. **Log in to Instagram**:
   - Open your web browser and log in to your Instagram account.

2. **Open Developer Tools**:
   - Right-click on the page and select "Inspect" (or press `Ctrl+Shift+I` on Windows/Linux or `Cmd+Option+I` on macOS).

3. **Navigate to the Application Tab**:
   - In Developer Tools, go to the "Application" tab.

4. **Locate the Cookies**:
   - In the left sidebar, expand the "Cookies" section and select `https://www.instagram.com`.

5. **Find the Session ID**:
   - Look for the cookie named `sessionid`. 
   - Copy the value of this cookie; this is your session ID.
For more information, visit [How to get Instagram session ID?](https://wpautomatic.com/how-to-get-instagram-session-id/).

## Step 2: Setting Your Session ID in the InstaFetch Tool

1. **Open the InstaFetch Streamlit App**:
   - Run the following command in your terminal if you haven’t already:

   ```bash
   streamlit run app.py
   ```

2. **Enter Your Session ID**:
   - In the Streamlit app, find the input box for the session ID.
   - Paste the copied session ID into the input field.

3. **Click the "Set Session ID" Button**:
   - Press the button to set your session ID. You should see a confirmation message indicating that your session ID has been successfully set.

## Step 3: Generating a Profile ID

1. **Navigate to the Profile ID Generator**:
   - Look for the section in the app labeled “Profile ID Generator.”

2. **Enter the Username**:
   - Type the Instagram username of the profile you want to analyze.

3. **Click the "Generate Profile ID" Button**:
   - Press the button to generate the profile ID.

4. **Recheck to View Profile Picture**:
   - After generating the profile ID, the tool will display the profile picture of the entered username. Click the button to view the profile picture.

5. **Copy the Profile ID**:
   - Once the profile ID is displayed, copy it to your clipboard.

## Step 4: Returning to the Home Page

1. **Go Back to the Home Page**:
   - Click on the “Home” button or navigate back to the main interface of the Streamlit app.

## Step 5: Generating and Filtering Data

1. **Paste the Profile ID**:
   - In the appropriate input field, paste the profile ID you copied earlier.

2. **Click the "Generate Data" Button**:
   - Press the button to generate the data associated with the profile ID.

3. **Filter Data**:
   - Use the filtering options available in the app to analyze specific aspects of the fetched data (e.g., engagement metrics, post types, etc.).

## Conclusion

You have now successfully obtained a session ID, generated a profile ID, and filtered data using the InstaFetch Tool! If you have any questions or need further assistance, please refer to the documentation or reach out via the GitHub repository.

Happy fetching! 🚀
```

You can copy and paste this into your Streamlit app or Markdown file!