import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Professional Sales Data Dashboard")
st.markdown("Upload your CSV file to visualize your business data instantly.")

# 2. Sidebar for File Upload
st.sidebar.header("Configuration")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # 3. Load Data
    df = pd.read_csv(uploaded_file)
    
    # 4. Display Summary Metrics
    st.subheader("Key Performance Indicators (KPI)")
    col1, col2, col3 = st.columns(3)
    
    total_sales = df['Sales'].sum()
    avg_sales = df['Sales'].mean()
    total_items = len(df)
    
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Average Sales", f"${avg_sales:,.2f}")
    col3.metric("Total Orders", total_items)

    # 5. Interactive Chart
    st.subheader("Sales Analysis by Category")
    fig = px.bar(df, x='Category', y='Sales', color='Category', title="Sales Distribution")
    st.plotly_chart(fig, use_container_width=True)

    # 6. Data Table
    st.subheader("Raw Data Preview")
    st.dataframe(df)

else:
    st.info("Waiting for CSV file upload. Please upload a file from the sidebar.")