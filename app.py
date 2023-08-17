import streamlit as st
import pandas as pd
import pickle

# Load the saved SVM model
with open('diabetes_model.pkl', 'rb') as model_file:
    svm_model = pickle.load(model_file)

# Streamlit app title and description
st.title('Diabetes Prediction App')

# Add an image for visual appeal
st.image('diabetes.jpg  ', use_column_width=True)

st.write('**Enter Patient Details:**')

# Input form for all features
age = st.number_input('Age (0 to 120)', min_value=0, max_value=120, value=30, step=1)
pregnancies = st.number_input('Number of Pregnancies (0 to 20)', min_value=0, max_value=20, value=1, step=1)
glucose = st.number_input('Glucose Level (0 to 200)', min_value=0.0, max_value=200.0, value=100.0, step=1.0)
blood_pressure = st.number_input('Blood Pressure (0 to 150)', min_value=0.0, max_value=150.0, value=70.0, step=1.0)
bmi = st.number_input('BMI (0 to 60)', min_value=0.0, max_value=60.0, value=25.0, step=1.0)
skin_thickness = st.number_input('Skin Thickness (0 to 20)', min_value=0.0, value=20.0, step=1.0)
insulin = st.number_input('Insulin Level (0 to 79)', min_value=0.0, value=79.0, step=1.0)
dpf = st.number_input('Diabetes Pedigree Function (0 to 0.4)', min_value=0.0, value=0.4, step=0.01)

if st.button('Predict', use_container_width= True):
    # Create a DataFrame with user input
    user_input = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    # Make a prediction using the SVM model
    prediction = svm_model.predict(user_input)

    # Display the prediction result with dynamic messages
    result_message = "**The person is predicted to have diabetes. 😔**" if prediction[0] == 1 else "**The person is predicted to be diabetes-free. 🤩**"
    st.success(result_message)
