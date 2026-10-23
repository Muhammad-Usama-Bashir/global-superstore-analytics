import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.preprocessing import clean_data

st.set_page_config(page_title="Customer Analysis", page_icon="👥", layout="wide")

st.title("👥 Customer Segmentation & Delivery Performance")
st.caption("Inspect top-performing customers, purchasing patterns, and shipping efficiency.")

raw_df = load_data()
df = clean_data(raw_df)

# Sidebar View Controls
st.sidebar.header("🎛️ Analysis Controls")
view_mode = st.sidebar.radio("View Mode", ["Graphs & Tables", "Graphs Only", "Tables Only"], key="cust_view")

cust_col = 'Customer_Name' if 'Customer_Name' in df.columns else ('Customer Name' if 'Customer Name' in df.columns else None)

if cust_col:
    top_cust = df.groupby(cust_col)[['Sales', 'Profit']].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)
    
    if view_mode in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("🏆 Top 10 Customers by Sales Revenue")
        fig_cust = px.bar(top_cust, x=cust_col, y='Sales', color='Profit', color_continuous_scale='Blues', text_auto='.2s')
        fig_cust.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
        st.plotly_chart(fig_cust, use_container_width=True)
        
    if view_mode in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Top Customers Data Table"):
            st.dataframe(top_cust, use_container_width=True)

if 'Delivery_Status' in df.columns:
    st.markdown("---")
    deliv_counts = df['Delivery_Status'].value_counts().reset_index()
    deliv_counts.columns = ['Delivery_Status', 'Order Count']
    
    if view_mode in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("📦 Delivery Status & Shipping Efficiency")
        fig_deliv = px.pie(deliv_counts, names='Delivery_Status', values='Order Count', hole=0.4, color_discrete_sequence=['#34d399', '#f87171', '#38bdf8'])
        fig_deliv.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
        st.plotly_chart(fig_deliv, use_container_width=True)
        
    if view_mode in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Delivery Status Data Table"):
            st.dataframe(deliv_counts, use_container_width=True)