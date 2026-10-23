import streamlit as st

st.set_page_config(
    page_title="Global Superstore Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional UI Styling (Clean, Modern & Eye-Friendly)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #111827 100%);
        color: #f1f5f9;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 25px;
    }
    .card {
        background-color: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .card h3, .card h4 {
        color: #38bdf8;
    }
</style>
""", unsafe_allow_html=True)

# Custom Sidebar Title for Navigation
st.sidebar.markdown("### 📌 Navigation Menu")
st.sidebar.caption("Select a page below to explore analytics:")

st.markdown('<p class="main-header">📊 Global Superstore Analytics Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Professional Business Intelligence, Exploratory Data Analysis & Machine Learning Forecasting</p>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>🎯 Executive Summary & Business Problem</h3>
    <p>Welcome to the Global Superstore Analytics platform. This system is designed to help retail executives and data analysts track sales performance, evaluate regional profitability, inspect customer behavior, and predict future order outcomes using robust Machine Learning models.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📋 Core Project Modules</h4>
        <ul>
            <li><b>Dataset Explorer:</b> Inspect raw data, missing values, and engineered features.</li>
            <li><b>Sales Dashboard:</b> Track KPIs, revenue trends, and category breakdowns.</li>
            <li><b>Regional Analysis:</b> Analyze geographical performance and profit margins.</li>
            <li><b>Customer Analysis:</b> Review customer segments and delivery efficiency.</li>
            <li><b>Profit Prediction:</b> Forecast order profit using Machine Learning algorithms.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>👨‍💻 Academic & Technical Info</h4>
        <p><b>Course Domain:</b> AI & Data Science / Python & Machine Learning</p>
        <p><b>Tech Stack:</b> Python, Streamlit, Pandas, Plotly, Scikit-Learn</p>
        <p><b>Pipeline Status:</b> Fully Modular & Operational ✅</p>
    </div>
    """, unsafe_allow_html=True)

st.info("👈 Use the sidebar menu on the left to navigate seamlessly through different analytical sections.")