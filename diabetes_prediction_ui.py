import pandas as pd
import streamlit as st
import pickle

def load_knn_model():
    filename = "finalized_model_random.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


st.set_page_config(layout="wide")

st.write("""
## Diabetes prediction
""")

st.markdown("""
This app predicts Diabetes using KNN model!
* **Python libraries:** streamlit
* **Data source:** [diabetes-dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset).
""")

st.sidebar.write("""
### User Input Features
""")
knn_model = load_knn_model()

name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.slider("Enter your age", min_value = 0, max_value = 100, value = 24)
pregnancies = st.sidebar.text_input("Number of pregnancies in the past:")
glucose = st.sidebar.text_input("Enter your glucose level:")
blood_pressure = st.sidebar.text_input("Enter your blood pressure:")
skin_thickness = st.sidebar.text_input("Enter your skin thickness:")
insulin = st.sidebar.text_input("Enter your insulin level:")
bmi = st.sidebar.text_input("Enter your bmi:")
diabetes_pedigree_fn = st.sidebar.text_input("DiabetesPedigreeFunction:")

predict_btn = st.sidebar.button("Predict") 

test_data1 = pd.DataFrame({
    "Pregnancies": [5]
    , "Glucose": [88.0]
    , "BloodPressure": [66.0]
    , "SkinThickness": [21.0]
    , "Insulin": [23.0]
    , "BMI": [24.4]
    , "DiabetesPedigreeFunction": [0.342]
    , "Age": [30]
})

test_data = pd.DataFrame({
    "Pregnancies": [int(pregnancies) if len(pregnancies) else 0]
    , "Glucose": [float(glucose) if len(glucose) else 0]
    , "BloodPressure": [float(blood_pressure) if len(blood_pressure) else 0]
    , "SkinThickness": [int(skin_thickness if len(skin_thickness) else 0)]
    , "Insulin": [int(insulin) if len(insulin) else 0]
    , "BMI": [float(bmi) if len(bmi) else 0]
    , "DiabetesPedigreeFunction": [float(diabetes_pedigree_fn) if len(diabetes_pedigree_fn) else 0]
    , "Age": [int(age)]
})
if predict_btn:
    st.write(""" Test data: """)
    st.write(test_data)
    pred = knn_model.predict(test_data)
    st.write(""" Prediction result: """)
    st.write(pred)
    if pred is not None and len(pred)>0 and pred[0] == 1:
        st.write("There are high chances of diabetes")
    else:
        st.write("There are no signs of diabetes")