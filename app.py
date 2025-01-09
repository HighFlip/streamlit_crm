import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Styling for containers */
    .stColumn {
        border: 1px solid #ccc;
        padding: 16px;
        border-radius: 8px;
        background-color: rgb(14, 17, 23);
        margin-bottom: 16px;
    }
    /* Styling for metrics */
    .metric-container {
        background-color: #eef6ff;
        border: 1px solid #bbe1fa;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Dummy data for the CRM
customers = [
    {"name": "Alice", "email": "alice@example.com", "spend": 1200},
    {"name": "Bob", "email": "bob@example.com", "spend": 850},
    {"name": "Charlie", "email": "charlie@example.com", "spend": 500},
    {"name": "Diana", "email": "diana@example.com", "spend": 1500},
]
customers_df = pd.DataFrame(customers)

# Sidebar for navigation
st.sidebar.title("CRM Dashboard")
st.sidebar.info("Navigate through different sections")

# Main dashboard title
st.title("CRM Dashboard")

# Dashboard Layout
st.header("Overview")

col1, col2 = st.columns(2)

# Pie Chart in the first column
with col1:
    st.subheader("Customer Spend Distribution")
    pie_chart = px.pie(customers_df, names="name", values="spend", title="Spend by Customer")
    st.plotly_chart(pie_chart, use_container_width=True)

# Customer List in the second column
with col2:
    st.subheader("Customer List")
    st.dataframe(customers_df, use_container_width=True)

# Second row with additional displays
st.header("Additional Insights")

# Create three columns
col3, col4, col5 = st.columns(3)

# Summary statistics in column 3
with col3:
    st.subheader("Total Customers")
    st.metric(label="Customers", value=len(customers))

# Most spending customer in column 4
with col4:
    top_customer = customers_df.loc[customers_df["spend"].idxmax()]
    st.subheader("Top Customer")
    st.write(f"**{top_customer['name']}**")
    st.write(f"Email: {top_customer['email']}")
    st.write(f"Spend: ${top_customer['spend']}")

# Recent activity log in column 5
with col5:
    st.subheader("Recent Activity")
    recent_activity = [
        {"activity": "Added new customer: Alice", "timestamp": "2025-01-01 10:30"},
        {"activity": "Updated customer: Bob", "timestamp": "2025-01-03 14:20"},
        {"activity": "Deleted customer: Charlie", "timestamp": "2025-01-05 09:50"},
    ]
    activity_df = pd.DataFrame(recent_activity)
    st.table(activity_df)


# Footer
st.write("Powered by Streamlit | Your CRM Dashboard")
