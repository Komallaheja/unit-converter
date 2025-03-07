import streamlit as st

st.title("🌎 Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the conversion result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value / 1.60934
        elif unit == "Miles to Kilometers":
            return value * 1.60934

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return 0  # Default return if no valid category or unit

# Category-based unit selection
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", 
                                                 "Minutes to Hours", "Hours to Minutes", 
                                                 "Hours to Days", "Days to Hours"])

# Get value input
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Perform conversion when button is clicked
if st.button("Convert"):
    if value > 0:  # Check if value is positive
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f}")
    else:
        st.warning("Please enter a positive value for conversion.")
