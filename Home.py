import streamlit as st

st.set_page_config(
    page_title="Insta Fetch",
    
)

st.title("Insta Fetch ")
st.sidebar.success("Select the page above")
sessio_id = ""

st.header('Enter Your Session Id')
input = st.text_input('Session Id',value="")
if st.button("Set Session ID"):
    st.session_state['session_id'] = input
    st.success(f"Session id set to: {st.session_state['session_id']}")


st.sidebar.success("Session ID: " + str(st.session_state.get("session_id", ""))[:15] + "...")