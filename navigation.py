import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("🏦 Bank Marketing System")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            # Create buttons in the sidebar
            if st.sidebar.button("Exploratory Data Analysis"):
                st.sidebar.markdown('<a href="https://github.com/emekaefidi/Bank-Marketing-with-Machine-Learning/blob/master/Bank%20Marketing%20with%20Machine%20Learning.ipynb" target="_blank">Exploratory Data Analysis</a>', unsafe_allow_html=True)

            if st.sidebar.button("Dataset"):
                st.sidebar.markdown('<a href="https://archive.ics.uci.edu/static/public/222/bank+marketing.zip" target="_blank">Dataset</a>', unsafe_allow_html=True)


            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
            
            
            

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")

def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
