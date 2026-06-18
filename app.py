import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("house_price_model.pkl")


# Title
st.title("🏠 House Price Prediction")

# Description
st.write("Predict house prices using Machine Learning.")

# Area
area = st.number_input(
    "📏 Enter Area (Square Feet)",
    min_value=1000,
    max_value=20000,
    value=5000,
    step=100
)

# Bedrooms
bedrooms = st.number_input(
    "🛏 Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

# Bathrooms
bathrooms = st.number_input(
    "🚿 Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

# Stories
stories = st.number_input(
    "🏢 Stories",
    min_value=1,
    max_value=5,
    value=2
)

# Parking
parking = st.number_input(
    "🚗 Parking",
    min_value=0,
    max_value=5,
    value=1
)

area = int(area)
bedrooms = int(bedrooms)
bathrooms = int(bathrooms)
stories = int(stories)
parking = int(parking)


furnishing = st.selectbox(
    "🛋 Furnishing Status",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)

mainroad = st.radio(
    "Main Road?",
    ["Yes", "No"]
)

guestroom = st.radio(
    "🛏 Guest Room?",
    ["Yes", "No"]
)

basement = st.radio(
    "🏠 Basement?",
    ["Yes", "No"]
)

hotwaterheating = st.radio(
    "🔥 Hot Water Heating?",
    ["Yes", "No"]
)

airconditioning = st.radio(
    "❄ Air Conditioning?",
    ["Yes", "No"]
)

prefarea = st.radio(
    "🌳 Preferred Area?",
    ["Yes", "No"]
)

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0


st.divider()

st.subheader("📋 Current Inputs")

st.write(f"📏 Area : {area}")
st.write(f"🛏 Bedrooms : {bedrooms}")
st.write(f"🚿 Bathrooms : {bathrooms}")
st.write(f"🏢 Stories : {stories}")
st.write(f"🚗 Parking : {parking}")

st.write(f"🛋 Furnishing : {furnishing}")

st.write(f"🛣 Main Road : {mainroad}")
st.write(f"🛏 Guest Room : {guestroom}")
st.write(f"🏠 Basement : {basement}")
st.write(f"🔥 Hot Water Heating : {hotwaterheating}")
st.write(f"❄ Air Conditioning : {airconditioning}")
st.write(f"🌳 Preferred Area : {prefarea}")

semi_furnished = 0
unfurnished = 0

if furnishing == "Semi-Furnished":
    semi_furnished = 1

elif furnishing == "Unfurnished":
    unfurnished = 1

input_data = pd.DataFrame({
    "area":[area],
    "bedrooms":[bedrooms],
    "bathrooms":[bathrooms],
    "stories":[stories],
    "mainroad":[mainroad],
    "guestroom":[guestroom],
    "basement":[basement],
    "hotwaterheating":[hotwaterheating],
    "airconditioning":[airconditioning],
    "parking":[parking],
    "prefarea":[prefarea],
    "furnishingstatus_semi-furnished":[semi_furnished],
    "furnishingstatus_unfurnished":[unfurnished]
})

if st.button("🏠 Predict House Price", use_container_width=True):

    with st.spinner("🔄 Predicting House Price..."):
        prediction = model.predict(input_data)

    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    st.success("✅ Prediction Completed!")

    st.write("---")

    st.metric(
        label="🏠 Estimated House Price",
        value=f"₹ {prediction[0]:,.2f}"
    )

    st.balloons()