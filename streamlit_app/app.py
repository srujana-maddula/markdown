import streamlit as st
import pandas as pd
import numpy as np

# Custom CSS to change slider red color to green and button to green
'''st.markdown("""
    <style>
    .stSlider div[data-baseweb="slider"] div[data-testid] div {
        background: green !important;
    }
    .stButton button {
        background-color: green !important;
        color: white !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)'''

# Page title
st.title("📊 Customer KPIs")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name", "Guest")
rows = st.sidebar.slider("Number of data rows", 5, 50, 10)

# Generate random dataset
data = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=["Metric A", "Metric B", "Metric C"]
)

# Show table
st.subheader("🔢 Data Table")
st.dataframe(data)

# Show chart
st.subheader("📈 Data Chart")
st.line_chart(data)

# Button
if st.button("Click Me"):
    st.success("Button clicked successfully! 🎉")
else:
    ValueError("Button not clicked yet")

# Select box
choice = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: **{choice}**")

# Checkbox
if st.checkbox("Show extra content"):
    st.write("Here’s some extra content 🎉")
else:
    ValueError("Checkbox is not selected")




