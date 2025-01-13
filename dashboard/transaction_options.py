import json
import streamlit as st

from streamlit_elements import mui, sync, lazy
from .dashboard import Dashboard


class TransactionOptions(Dashboard.Item):
    TRANSACTION_TYPES = ["SELL", "BUY"]
    PAYMENT_METHODS = ["CASH", "DEBIT", "CREDIT"]

    def __call__(self):
        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.ShoppingCart()
                mui.Typography("Transaction Form")

            with mui.Box(
                sx={
                    "display": "flex",
                    "flexDirection": "column",
                    "gap": "20px",  # Space between fields
                    "alignItems": "center",  # Center align all elements
                    "justifyContent": "center",
                    "padding": "15px",
                }
            ):
                # Dropdown for Transaction Type
                mui.FormControl(
                    mui.InputLabel("Transaction Type"),
                    mui.Select(
                        [mui.MenuItem(option, key=option, value=option) for option in self.TRANSACTION_TYPES],
                        onChange=lazy(sync("transaction_type")),
                        fullWidth=True,
                    ),
                    sx={"width": "350px"},  # Add minimum width to dropdown
                )

                # Dropdown for Payment Method
                mui.FormControl(
                    mui.InputLabel("Payment Method"),
                    mui.Select(
                        [mui.MenuItem(option, key=option, value=option) for option in self.PAYMENT_METHODS],
                        onChange=lazy(sync("payment_method")),
                        fullWidth=True,
                    ),
                    sx={"width": "350px"},  # Add minimum width to dropdown
                )


                # Text Box for Amount
                mui.TextField(
                    label="Amount",
                    placeholder="Enter amount",
                    onChange=sync("amount"),
                    type="number",
                    sx={"width": "350px"},  # Add minimum width
                )
