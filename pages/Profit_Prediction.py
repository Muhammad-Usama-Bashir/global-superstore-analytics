import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from utils.data_loader import load_data
from utils.preprocessing import clean_data

st.set_page_config(page_title="Profit Prediction", page_icon="💡", layout="wide")

st.title("💡 Smart Profit Prediction & Order Analyzer")
st.caption("Predict expected order profit using a trained Machine Learning model serialized in the models/ directory.")

# Load and clean data
raw_df = load_data()
df = clean_data(raw_df)

model_dir = "models"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "profit_model.pkl")

model_df = df.dropna(subset=['Sales', 'Discount', 'Quantity', 'Profit'])

if len(model_df) > 10:
    X = model_df[['Sales', 'Discount', 'Quantity']]
    y = model_df['Profit']
    
    # Train or Load Model
    if not os.path.exists(model_path):
        with st.spinner("Training Random Forest Regressor and saving to models/ folder..."):
            rf_predictor = RandomForestRegressor(n_estimators=100, random_state=42)
            rf_predictor.fit(X, y)
            joblib.dump(rf_predictor, model_path)
    else:
        rf_predictor = joblib.load(model_path)
        
    st.markdown("### 📝 Enter New Order Parameters")
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            input_sales = st.number_input("Sales Amount ($)", min_value=1.0, max_value=50000.0, value=300.0)
        with col2:
            input_discount = st.slider("Discount Rate", min_value=0.0, max_value=0.8, value=0.15, step=0.05)
        with col3:
            input_qty = st.number_input("Quantity", min_value=1, max_value=50, value=4)
            
        submit_btn = st.form_submit_button("Predict Profit 🚀")
        
    if submit_btn:
        input_data = pd.DataFrame([[input_sales, input_discount, input_qty]], columns=['Sales', 'Discount', 'Quantity'])
        predicted_profit = rf_predictor.predict(input_data)[0]
        
        st.markdown("---")
        st.subheader("📊 Model Prediction Results")
        
        res1, res2, res3 = st.columns(3)
        res1.metric("Predicted Profit", f"${predicted_profit:,.2f}")
        
        profit_margin_pct = (predicted_profit / input_sales) * 100 if input_sales > 0 else 0
        res2.metric("Estimated Profit Margin", f"{profit_margin_pct:.2f}%")
        
        if predicted_profit < 0:
            res3.error("⚠️ Risk Warning: This order configuration will result in a NET LOSS!")
        elif profit_margin_pct < 10:
            res3.warning("⚡ Low Profit Margin Category")
        else:
            res3.success("🌟 Healthy Profit Category")
else:
    st.warning("Insufficient clean data available to train the prediction model.")