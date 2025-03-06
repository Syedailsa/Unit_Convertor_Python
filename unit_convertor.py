# import streamlit as st

# def unit_convertor(value, unit_from, unit_to):

#     convertions = {
#         "Meter_Kilometer": 0.001,
#         "Kilometer_Meter": 1000,
#         "Gram_Kilogram": 0.001,
#         "Kilogram_Gram": 1000
#     }

#     key = f"{unit_from}_{unit_to}"

#     if key in convertions:
#         convertion = convertions[key]
#         return value * convertion
#     else: 
#         return "Conversion not supported"
    
# st.title("Unit Convertor")

# value = st.number_input("Enter value:")

# unit_from = st.selectbox("Convert from: ", ["Meter", "Kilometer", "Gram", "Kilogram"])

# unit_to = st.selectbox("Convert to: ", ["Meter", "Kilometer", "Gram", "Kilogram"])

# if st.button("Convert"):
#     result = unit_convertor(value, unit_from, unit_to)
#     st.write(f"The Result is : {result}")

import streamlit as st

def unit_convertor(value, unit_from, unit_to):
    # Dictionary of conversions
    conversions = {
        # Length conversions
        "Meter_Kilometer": 0.001,
        "Kilometer_Meter": 1000,
        "Meter_Centimeter": 100,
        "Centimeter_Meter": 0.01,
        "Kilometer_Centimeter": 100000,
        "Centimeter_Kilometer": 0.00001,
        
        # Weight conversions
        "Gram_Kilogram": 0.001,
        "Kilogram_Gram": 1000,
        "Gram_Milligram": 1000,
        "Milligram_Gram": 0.001,
        "Kilogram_Milligram": 1000000,
        "Milligram_Kilogram": 0.000001,
        
        # Temperature conversions (example: Celsius to Fahrenheit)
        "Celsius_Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit_Celsius": lambda x: (x - 32) * 5/9,
    }

    # Create the key for the conversion
    key = f"{unit_from}_{unit_to}"

    # Check if the conversion exists
    if key in conversions:
        conversion = conversions[key]
        # Handle lambda functions for temperature conversions
        if callable(conversion):
            return conversion(value)
        else:
            return value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI
st.title("Unit Converter")

# Input: Value to convert
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Input: Convert from
unit_from = st.selectbox("Convert from:", ["Meter", "Kilometer", "Centimeter", "Gram", "Kilogram", "Milligram", "Celsius", "Fahrenheit"])

# Input: Convert to
unit_to = st.selectbox("Convert to:", ["Meter", "Kilometer", "Centimeter", "Gram", "Kilogram", "Milligram", "Celsius", "Fahrenheit"])

# Convert button
if st.button("Convert"):
    if unit_from == unit_to:
        st.warning("Please select different units for conversion.")
    else:
        result = unit_convertor(value, unit_from, unit_to)
        if result == "Conversion not supported":
            st.error("Conversion not supported for the selected units.")
        else:
            st.success(f"The result is: **{result:.4f}**")