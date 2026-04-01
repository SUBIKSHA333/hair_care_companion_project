import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import matplotlib.pyplot as plt

# ✅ Page Config + Styling
st.set_page_config(page_title="AI Hair Care System", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Import Orchestrator
from agents.orchestrator import HairCareOrchestrator 

# Create folder if not exists
if not os.path.exists("hair_images"):
    os.makedirs("hair_images")

# Initialize orchestrator
orchestrator = HairCareOrchestrator()

# --- TITLE ---
st.title("💇‍♀️ AI Hair Care Dashboard")
st.write("Analyze your hair health using AI agents")

# --- USER NAME ---
user_name = st.text_input("Enter your name", value="Subiksha")

# --- INPUTS (COLUMNS UI) ---
st.header("📊 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 15, 60, 25)
    gender = st.selectbox("Gender", ["F", "M"])
    sleep = st.slider("Sleep (hours/day)", 4, 10, 7)
    stress = st.slider("Stress Level", 1, 10, 5)

with col2:
    wash_freq = st.slider("Hair Wash Frequency", 1, 7, 3)
    shampoo_type = st.selectbox("Shampoo Type", ["Herbal", "Chemical"])
    diet_quality = st.selectbox("Diet Quality", ["Poor", "Average", "Good", "Excellent"])
    water_type = st.selectbox("Water Type", ["Hard", "Soft"])

# Convert input
user_dict = {
    "age": age,
    "gender": gender,
    "sleep": sleep,
    "stress": stress,
    "wash_freq": wash_freq,
    "shampoo_type": shampoo_type,
    "diet_quality": diet_quality,
    "water_type": water_type
}

# --- PREDICTION ---
if st.button("Predict Hair Fall Risk"):
    result = orchestrator.run(user_dict)

    risk = result["risk"]

    st.markdown("### 🧠 Prediction Result")
    st.metric(label="Hair Fall Risk", value=risk)

    # Save history
    history = pd.DataFrame({
        "Name": [user_name],
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Risk": [risk]
    })

    if not os.path.exists("hair_history.csv"):
        history.to_csv("hair_history.csv", index=False)
    else:
        history.to_csv("hair_history.csv", mode='a', index=False, header=False)

    # Recommendations
    rec = result["recommendations"]

    st.markdown("### 🧴 Recommendations")

    c1, c2, c3 = st.columns(3)
    c1.metric("Shampoo", rec['shampoo'])
    c2.metric("Oil", rec['oil'])
    c3.metric("Tips", rec['tips'])

# --- IMAGE UPLOAD ---
st.markdown("---")
st.header("📷 Hair Density Detection")

uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    result = orchestrator.run(user_dict, image=image)

    st.image(image, caption="Uploaded Image")
    st.success(f"Density: {result['density']} ({result['density_ratio']:.2f})")

    filename = f"{user_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    path = os.path.join("hair_images", filename)
    image.save(path)

# --- CHATBOT ---
st.markdown("---")
st.header("💬 Hair Doctor Chatbot")

query = st.text_input("Enter your hair problem")

if st.button("Get Advice"):
    result = orchestrator.run(user_dict, query=query)
    st.success(result["chatbot_response"])

# --- HISTORY ---
st.markdown("---")
st.header("📊 History")

if os.path.exists("hair_history.csv"):
    data = pd.read_csv("hair_history.csv")
    user_data = data[data["Name"] == user_name]

    if not user_data.empty:
        st.dataframe(user_data.tail(5))
    else:
        st.info("No history found.")
else:
    st.info("No history available.")

# --- DASHBOARD ---
st.markdown("---")
st.header("📊 Hair Health Dashboard")

if os.path.exists("hair_history.csv"):
    data = pd.read_csv("hair_history.csv")
    user_data = data[data["Name"] == user_name]

    if not user_data.empty:

        risk_counts = user_data["Risk"].value_counts()

        col1, col2 = st.columns(2)

        # BAR CHART
        with col1:
            st.subheader("📊 Risk Distribution")
            fig1, ax1 = plt.subplots()
            ax1.bar(risk_counts.index, risk_counts.values)
            st.pyplot(fig1)

        # PIE CHART
        with col2:
            st.subheader("🥧 Risk Percentage")
            fig2, ax2 = plt.subplots()
            ax2.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%')
            st.pyplot(fig2)

    else:
        st.info("No data for dashboard yet.")
else:
    st.info("No history file found.")


# python -m streamlit run hair_fall_predictor_app.py  run using this  