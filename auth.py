import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_elements import elements, dashboard, mui
import random, string

def generate_new_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def authenticate_user():
    config_file = "config.yaml"
    with open(config_file) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Sidebar: Add a button to refresh cookie key
    with st.sidebar:
        if st.button("Refresh Cookie Key (Debug)", key="refresh_cookie"):
            new_key = generate_new_key()
            config["cookie"]["key"] = new_key
            with open(config_file, "w") as file:
                yaml.dump(config, file)
            st.sidebar.success(f"Cookie key updated to: {new_key}")
            st.sidebar.info("Please reload the app for the changes to take effect.")
            st.stop()  # Stop execution to allow user to reload the app

    # Initialize the authenticator
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],  # Secret key for the cookie
        config["cookie"]["expiry_days"],
    )

    try:
        authenticator.experimental_guest_login(
            "Login with Google", provider="google", oauth2=config["oauth2"]
        )
    except Exception as e:
        st.error(e)

    preauth_emails = config["pre-authorized"]["emails"]
    authenticated_email = st.session_state["username"]

    return authenticated_email in preauth_emails

