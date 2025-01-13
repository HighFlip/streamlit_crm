import json
import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from streamlit_elements import dashboard as st_dashboard
from types import SimpleNamespace

from auth import authenticate_user

from dashboard.transaction_options import TransactionOptions
from dashboard.dashboard import Dashboard
from dashboard.editor import Editor
from dashboard.card import Card
from dashboard.datagrid import DataGrid
from dashboard.radar import Radar
from dashboard.pie import Pie
from dashboard.player import Player


def main():
    authenticated = authenticate_user()

    # Initialize session state variables if not already set
    if "transaction_type" not in st.session_state:
        st.session_state.transaction_type = ""
    if "payment_method" not in st.session_state:
        st.session_state.payment_method = ""
    if "amount" not in st.session_state:
        st.session_state.amount = ""

    if st.session_state["authentication_status"] is None:
        st.warning('Please Login using your designated google account.')
    elif authenticated is False:
        st.error("User not permitted")
        st.stop()
    elif st.session_state["authentication_status"]:
        st.sidebar.success(f"Welcome, {st.session_state['name']}!")

        # Removed because of the use of guest login through google
        # authenticator.logout("Logout", "sidebar")

        st.write(
            """
            💼 Streamlit CRM &nbsp; [![GitHub][github_badge]][github_link]
            =====================

            [github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
            [github_link]: https://github.com/HighFlip/streamlit_crm
            """
        )
        st.write("Debugging Session State:")
        st.write("Transaction Type:", st.session_state.get("transaction_type", ""))
        st.write("Payment Method:", st.session_state.get("payment_method", ""))
        st.write("Amount:", st.session_state.get("amount", ""))
        # st.title("")

        if "w" not in state:
            board = Dashboard()
            w = SimpleNamespace(
                dashboard=board,
                data_grid=DataGrid(board, 0, 0, 6, 10, minW=4, minH=10),
                transaction_options=TransactionOptions(board, 8, 0, 6, 5, minW=3, minH=4),
                card2=Card(board, 8, 5, 6, 5, minW=3, minH=4),
            )
            state.w = w

        else:
            w = state.w

        with elements("demo"):
            event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

            with w.dashboard(rowHeight=57):
                w.data_grid("")

                w.transaction_options()
                w.card2("Card 2")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
