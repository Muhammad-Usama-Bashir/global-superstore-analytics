import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.preprocessing import clean_data

st.set_page_config(page_title="Sales Dashboard", page_icon="📈", layout="wide")

st.title("📈 Sales & Profit Performance Dashboard")
st.caption("Interactive analysis of sales revenue, profit margins, and key performance metrics.")

# Load and clean data
raw_df = load_data()
df = clean_data(raw_df)

if 'Product_Category' in df.columns and 'Category' not in df.columns:
    df['Category'] = df['Product_Category']
if 'Total_Sale' in df.columns and 'Sales' not in df.columns:
    df['Sales'] = df['Total_Sale']

# User View & Filter Controls in Sidebar
st.sidebar.header("🎛️ Dashboard Controls")
view_option = st.sidebar.radio("Select View Mode", ["Graphs & Tables", "Graphs Only", "Tables Only"])

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Data Filters")
regions = ["All"] + sorted(df['Region'].dropna().unique().tolist()) if 'Region' in df.columns else ["All"]
sel_region = st.sidebar.selectbox("Filter by Region", regions)

category_col = 'Category' if 'Category' in df.columns else None
categories = ["All"] + sorted(df[category_col].dropna().unique().tolist()) if category_col else ["All"]
sel_cat = st.sidebar.selectbox("Filter by Category", categories)

filtered_df = df.copy()
if sel_region != "All" and 'Region' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Region'] == sel_region]
if sel_cat != "All" and category_col:
    filtered_df = filtered_df[filtered_df[category_col] == sel_cat]

# KPIs Section
total_sales = filtered_df['Sales'].sum() if 'Sales' in filtered_df.columns else 0
total_profit = filtered_df['Profit'].sum() if 'Profit' in filtered_df.columns else 0
total_orders = filtered_df['Order_ID'].nunique() if 'Order_ID' in filtered_df.columns else len(filtered_df)

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales Revenue", f"${total_sales:,.2f}")
c2.metric("Total Net Profit", f"${total_profit:,.2f}")
c3.metric("Total Order Count", f"{total_orders:,}")

st.markdown("---")

# Monthly Trend Analysis
if 'Order Date' in filtered_df.columns:
    filtered_df['Year_Month'] = filtered_df['Order Date'].dt.strftime('%Y-%m')
    df_trend = filtered_df.groupby('Year_Month')[['Sales', 'Profit']].sum().reset_index().sort_values('Year_Month')
    
    if view_option in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("📅 Monthly Sales & Profit Trends")
        fig = px.line(df_trend, x='Year_Month', y=['Sales', 'Profit'], markers=True, color_discrete_sequence=['#38bdf8', '#34d399'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
        st.plotly_chart(fig, use_container_width=True)
        
    if view_option in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Monthly Trend Data Table"):
            st.dataframe(df_trend, use_container_width=True)

# Category Breakdown
if category_col and 'Sales' in filtered_df.columns:
    cat_df = filtered_df.groupby(category_col)[['Sales', 'Profit']].sum().reset_index()
    
    if view_option in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("🏷️ Performance by Product Category")
        fig_cat = px.bar(cat_df, x=category_col, y='Sales', color='Profit', color_continuous_scale='Blues', text_auto='.2s')
        fig_cat.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
        st.plotly_chart(fig_cat, use_container_width=True)
        
    if view_option in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Category Breakdown Table"):
            st.dataframe(cat_df, use_container_width=True)