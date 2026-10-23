import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.preprocessing import clean_data

st.set_page_config(page_title="Regional Analysis", page_icon="🌍", layout="wide")

st.title("🌍 Regional & Product Deep-Dive Analysis")
st.caption("Geographical performance breakdown across regions, markets, and sub-categories.")

raw_df = load_data()
df = clean_data(raw_df)

# Sidebar View Controls
st.sidebar.header("🎛️ Analysis Controls")
view_mode = st.sidebar.radio("View Mode", ["Graphs & Tables", "Graphs Only", "Tables Only"], key="reg_view")

if 'Region' in df.columns:
    reg_df = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
    
    if view_mode in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("📊 Regional Sales Share & Net Profit")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Sales Share by Region")
            fig_pie = px.pie(reg_df, names='Region', values='Sales', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
            fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col2:
            st.markdown("##### Profit by Region")
            fig_bar = px.bar(reg_df, x='Region', y='Profit', color='Profit', color_continuous_scale='Greens')
            fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
            st.plotly_chart(fig_bar, use_container_width=True)
            
    if view_mode in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Regional Performance Data Table"):
            st.dataframe(reg_df, use_container_width=True)

if 'Sub-Category' in df.columns:
    st.markdown("---")
    sub_cat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index().sort_values(by='Sales', ascending=False)
    
    if view_mode in ["Graphs & Tables", "Graphs Only"]:
        st.subheader("📦 Sub-Category Performance Analysis")
        fig_sub = px.bar(sub_cat, x='Sub-Category', y='Sales', color='Profit', color_continuous_scale='Viridis', text_auto='.2s')
        fig_sub.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f1f5f9')
        st.plotly_chart(fig_sub, use_container_width=True)
        
    if view_mode in ["Graphs & Tables", "Tables Only"]:
        with st.expander("📊 View Sub-Category Data Table"):
            st.dataframe(sub_cat, use_container_width=True)