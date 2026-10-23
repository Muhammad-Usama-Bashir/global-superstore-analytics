import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans raw dataset, handles dates, and engineers required features
    according to assignment specifications.
    """
    df_cleaned = df.drop_duplicates().copy()
    
    # 1. Order ID se Year extract karna (e.g., CA-2011-... -> 2011)
    if 'Order ID' in df_cleaned.columns:
        df_cleaned['Extracted_Year'] = df_cleaned['Order ID'].astype(str).str.extract(r'-(\d{4})-')
        df_cleaned['Extracted_Year'] = pd.to_numeric(df_cleaned['Extracted_Year'], errors='coerce')
    
    # Timeline rebuild karna
    if 'Extracted_Year' in df_cleaned.columns:
        df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Extracted_Year'].astype(str) + '-01-01', errors='coerce')
    elif 'Order Date' in df_cleaned.columns:
        df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Order Date'], errors='coerce')
        
    # ---------------------------------------------------------
    # 2. FEATURE ENGINEERING (Task 3 Requirements)
    # ---------------------------------------------------------
    
    # Temporal Features
    if 'Order Date' in df_cleaned.columns:
        df_cleaned['Order_Year'] = df_cleaned['Order Date'].dt.year
        df_cleaned['Order_Month'] = df_cleaned['Order Date'].dt.month
        df_cleaned['Month_Name'] = df_cleaned['Order Date'].dt.strftime('%B')
        df_cleaned['Quarter'] = df_cleaned['Order Date'].dt.quarter
        df_cleaned['Day_Name'] = df_cleaned['Order Date'].dt.strftime('%A')

    # Financial & Calculated Features
    if 'Profit' in df_cleaned.columns and 'Sales' in df_cleaned.columns:
        # Profit Margin (handling division by zero error)
        df_cleaned['Profit_Margin'] = np.where(
            df_cleaned['Sales'] > 0, 
            (df_cleaned['Profit'] / df_cleaned['Sales']) * 100, 
            0
        )
        
    # Discount & Revenue estimation features agar columns mojood hon
    if 'Unit_Price' in df_cleaned.columns and 'Quantity' in df_cleaned.columns:
        df_cleaned['Revenue_Before_Discount'] = df_cleaned['Unit_Price'] * df_cleaned['Quantity']
        if 'Discount' in df_cleaned.columns:
            df_cleaned['Discount_Amount'] = df_cleaned['Revenue_Before_Discount'] * df_cleaned['Discount']
            
    # Delivery Status Feature (misal ke tor par agar Delivery_Days column ho)
    if 'Delivery_Days' in df_cleaned.columns:
        df_cleaned['Delivery_Status'] = df_cleaned['Delivery_Days'].apply(
            lambda x: 'Delayed' if x > 5 else 'On Time'
        )

    return df_cleaned