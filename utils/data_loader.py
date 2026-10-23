import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/dataset.csv")
    return df

if __name__ == "__main__":
    df = load_data()
    print("--- Dataset Shape (Rows, Columns) ---")
    print(df.shape)
    
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    print("\n--- Missing Values Check ---")
    print(df.isnull().sum())