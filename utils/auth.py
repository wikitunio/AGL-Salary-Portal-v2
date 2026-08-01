import streamlit as st
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def check_password():
    """Password protection for the dashboard."""

    def password_entered():
        if st.session_state["password"] == st.secrets["DASHBOARD_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown(
            "<h2 style='text-align:center;'>🔒 Secure Login</h2>",
            unsafe_allow_html=True,
        )
        st.text_input(
            "Enter Dashboard Password",
            type="password",
            on_change=password_entered,
            key="password",
        )
        return False

    elif not st.session_state["password_correct"]:
        st.markdown(
            "<h2 style='text-align:center;'>🔒 Secure Login</h2>",
            unsafe_allow_html=True,
        )
        st.text_input(
            "Enter Dashboard Password",
            type="password",
            on_change=password_entered,
            key="password",
        )
        st.error("😕 Password incorrect")
        return False

    return True


def authenticate_gmail():
    """Authenticate with Gmail API."""

    creds = Credentials(
        token=None,
        refresh_token=st.secrets["GMAIL_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=st.secrets["GMAIL_CLIENT_ID"],
        client_secret=st.secrets["GMAIL_CLIENT_SECRET"],
    )

    return build("gmail", "v1", credentials=creds)
