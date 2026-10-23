import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.preprocessing import clean_data

st.set_page_config(page_title="Dataset Explorer", page_icon="📁", layout="wide")

st.title("📁 Dataset Pipeline & Explorer")
st.caption("Inspect raw data ingestion, feature engineering steps, and the final cleaned dataset.")

# Load and Clean Data
raw_df = load_data()
cleaned_df = clean_data(raw_df)

# User View Options
view_tab = st.radio(
    "🔍 Select Data View Mode",
    ["Cleaned Dataset (Processed)", "Raw Dataset (Original)", "Dataset Structure & Summary"],
    horizontal=True
)

st.markdown("---")

if view_tab == "Cleaned Dataset (Processed)":
    st.subheader("🟢 Cleaned Data with Engineered Features")
    st.write(f"**Total Rows:** {len(cleaned_df):,} | **Total Columns:** {len(cleaned_df.columns)}")
    st.caption("Scroll horizontally and vertically to inspect the processed dataset.")
    st.dataframe(cleaned_df, use_container_width=True, height=500)

elif view_tab == "Raw Dataset (Original)":
    st.subheader("🔴 Raw Dataset (Before Preprocessing)")
    st.write(f"**Total Rows:** {len(raw_df):,} | **Total Columns:** {len(raw_df.columns)}")
    st.caption("Original uploaded data before cleaning and missing value imputation.")
    st.dataframe(raw_df, use_container_width=True, height=500)

else:
    st.subheader("📊 Column Data Types & Missing Values Report")
    summary_df = pd.DataFrame({
        'Column Name': cleaned_df.columns,
        'Non-Null Count': cleaned_df.notnull().sum().values,
        'Null Count': cleaned_df.isnull().sum().values,
        'Data Type': cleaned_df.dtypes.astype(str).values
    })
    st.dataframe(summary_df, use_container_width=True, height=400)