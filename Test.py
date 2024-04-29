# -*- coding: utf-8 -*-
"""
Created on Wed May 28 10:28:49 2023

@author: Alok Jha
"""

# -*- coding: utf-8 -*-
import pickle
import numpy as np
#import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

p_model = pickle.load(open('C:/Users/iibm/Desktop/Project Python/pa.sav','rb') )



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Expert System for Prediction',
                          
                          [ 'Transformer Health Prediction',],
                          icons=['robot',], 
                          default_index=0)
    

   
# Transformer Health Prediction

if (selected == 'Transformer Health Prediction'):
    
    # page title
    st.title('Transformer Health Prediction using ML')
   
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Hydrogen = st.text_input('Hydrogen Level') #or st.df.iloc                                                                                                                                                                                                       [0][0]
        
    with col2:
        Oxigen = st.text_input('Oxigen Level') #or st.df[1][1]
    
    with col3:
        Nitrogen = st.text_input('Nitrogen Level') #or st.df[1][2]
    
    with col1:
        Methane = st.text_input('Mathane Level') #or st.df[1][3]
    
    with col2:
        CO = st.text_input('CO Level') #or st.df[1][4]
    
    with col3:
        CO2 = st.text_input('CO2 value') #or st.df[1][5]
    
    with col1:
        Ethylene = st.text_input('Ethylene Level') #or st.df[1][6]
    
    with col2:
        Ethane= st.text_input('Ethane Level') #or st.df[1][7]
    
    with col3:
        Acethylene = st.text_input('Acethylene Level') #or st.df[1][8]
        
    with col1:
        DBDS = st.text_input('DBDS Level') #or st.df[1][9]
    
    with col2:
        PF= st.text_input('Power factor Value') #or st.df[1][10]
    
    with col3:
        IV= st.text_input('Interfacial V') #or st.df[1][11]
    
    with col1:
        DR= st.text_input('Dielectric rigidity Value') #or st.df[1][12]
    
    with col2:
        WC= st.text_input('Water content')   #or st.df[1][13]
    
    # File uploader widget
   # uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "csv"], accept_multiple_files=False)
   # df= pd.read_csv(uploaded_file)
    #st.dataframe(df)
    
    
    
    
    
    # code for Prediction
    prediction = ''

    if st.button('Transformer Health Result'):
        # Convert input values to appropriate numeric types
        input_values = [
            float(Hydrogen), float(Oxigen), float(Nitrogen), float(Methane),
            float(CO), float(CO2), float(Ethylene), float(Ethane), float(Acethylene),
            float(DBDS), float(PF), float(IV), float(DR), float(WC)
        ]
        
        # Perform the prediction using the converted input
        prediction = p_model.predict(np.asarray([input_values]))
        
        if prediction[0] == 4:
            st.write('Very Good Condition')
            st.write('No maintenance')
        elif prediction[0] == 3:
            st.write('Good Condition')
            st.write('Normal maintenance')
        elif prediction[0] == 2:
            st.write('Fair')
            st.write('Increase diagnostic testing, possible remedial work or replacement needed depending on criticality')
        elif prediction[0] == 1:
            st.write('Poor')
            st.write('Start planning process to replace or rebuild considering risk and consequence of failure')
        else:
            st.write('Poor')
            st.write('Immediately assess risk, replace or rebuild based on assessment')
    
    st.success(prediction)


    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


