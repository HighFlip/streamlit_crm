import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_elements import elements, dashboard, mui

def authenticate_user():
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Initialize the authenticator
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],  # Secret key for the cookie
        config["cookie"]["expiry_days"],
    )

    try:
        authenticator.login(max_concurrent_users=2)
    except Exception as e:
        st.error(e)

    return authenticator

