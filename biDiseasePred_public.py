# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:35:32 2024

@author: Alqama
"""

# import necessary libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading models


dia_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))



# sidebar for navigation
 
with st.sidebar:
    
    selected = option_menu('Bi Diseaese Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity','heart'],
                           default_index=0)
    
    
#diabetes prediction page
if (selected == 'Diabetes Prediction'):
      
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('number of pregnancies')

    with col2: 
        Glucose = st.text_input('Glucose level')
      
    with col3: 
        BloodPressure = st.text_input('Blood Pressure Value')
      
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2: 
        Insulin = st.text_input('Insulin level')
      
    with col3: 
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
      
    with col2: 
        Age = st.text_input('Age of the person')
    
 
    # code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = dia_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    
    st.success(diab_diagnosis)
      
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2: 
        sex = st.text_input('Gender')
          
    with col3: 
        cp = st.text_input('Chest Pain')
          
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
            
    with col2: 
        chol = st.text_input('Serum Cholestorol in mg/dl')
          
    with col3: 
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results ')
          
    with col2: 
        thalach = st.text_input('Max heart rate achieved')
            
    with col3: 
        exang = st.text_input('Exercise Included Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2: 
        slope = st.text_input('Sope of the Peak Exerciese ST segment')
          
    with col3: 
        ca = st.text_input('Major vessels colored by flouroscopy')
          
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    #code for prediction   
    heart_diagnosis = ''
     
    # creating a button for prediction
     
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
         
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is diabetic'
        else:
            heart_diagnosis = 'The person is not diabetic'
     
    st.success(heart_diagnosis)