import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.set_page_config(
    page_title="Heart Failure Prediction"
    )

st.title('Heart Failure Prediction App: 🫀')

age = st.text_input("Age:",placeholder = "Enter the Age:")
anaemia = st.text_input("Anaemia:",placeholder = "Yes = 1 , No = 0")
creatinine_phosphokinase = st.text_input("Creatinine Phosphokinase:",placeholder = "(100,220,300,400,1010 etc..)")

diabetes = st.text_input("Diabetes:",placeholder = "Yes = 1 , No = 0")

ejection_fraction = st.text_input("Ejection Fraction:",placeholder = "(20,30,...,55)")

high_blood_pressure = st.text_input("High Blood Pressure:",placeholder = "Yes = 1 , No = 0")
platelets = st.text_input("Platelets:",placeholder = "Enter platelets level:")
serum_creatinine = st.text_input("Serum Creatinine:",placeholder="Typical range b/w 0.74 to 1.35")
serum_sodium = st.text_input("Sodium level:",placeholder = "Enter sodium level in blood:")
sex = st.text_input("Gender:",placeholder = "Male = 1 , Female = 0")
smoking = st.text_input("Smoking:",placeholder = "Yes = 1 , No = 0")
time = st.text_input("Time:",placeholder = "Enter the time:")

if st.button("Predict"):
    try:
        model = pickle.load(open('model.pkl', 'rb'))
        input_values = np.array([[age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
        result = model.predict(input_values)
        
        if result == 1:
            st.warning("Patient is likely to have heart failure",icon="⚠️")
        else:
            st.success("Patient is not likely to have heart failure")
    except ValueError:
        st.warning("Please enter the values",icon="⚠️")
        