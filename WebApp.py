# Multiple Models in a Web app
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading models
DibetiesModel = pickle.load(open("C:/Users/BALAJI/Desktop/sohith/Multiple_Disease_Pediction_WebApp/DiabetesModel.sav",'rb'))
HeartModel =  pickle.load(open("C:/Users/BALAJI/Desktop/sohith/Multiple_Disease_Pediction_WebApp/HeartModel.sav",'rb'))
ParkinsonsModel =  pickle.load(open("C:/Users/BALAJI/Desktop/sohith/Multiple_Disease_Pediction_WebApp/ParkinsonsModel.sav",'rb'))

#creating side menu 
with st.sidebar :
    selected = option_menu(
        # menu head
        "Multplie Dieseas Models", 
        # menu options
        ['Dibeties Prediction','Heart disease Prediction','Parkinsons Prediction' ],
        # icons
        icons=['activity','heart','person'],
        default_index=0)
    

# creating pages

# dibeties page
if (selected == 'Dibeties Prediction'):
    #title of the page
    st.title("Dibeties Prediction using ML")
    
    #columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Pregnancies")
    with col2 : 
        Glucose = st.text_input("Glucose")        
    with col3:
        BloodPressure = st.text_input("BloodPressure")
    with col1:
        SkinThickness = st.text_input("SkinThickness")
    with col2 : 
        Insulin = st.text_input("Insulin")        
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Age")
        
    #output
    result = ''
    
    if(st.button("predict")):
        inputs = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        data = np.asarray(inputs).reshape(1,-1)
        prediction = DibetiesModel.predict(data)
        if(prediction[0] == 0):
            result = 'The person is diabetic'
        else:
            result = 'The person is not diabetic'
        
    st.success(result)


# Heart page
if (selected == 'Heart disease Prediction'):
    #title of the page
    st.title("Heart Disease Prediction using ML")
    
    #columns
    col1, col2, col3, col4 = st.columns(4)
    


    with col1:
        age = st.text_input("age")
        
    with col2 : 
        sex = st.text_input("sex")      
        
    with col3:
        cp = st.text_input("cp")
    
    with col4 : 
        trestbps = st.text_input("trestbps")  
        
    with col1:
        chol = st.text_input("chol")
        
    with col2:
        fbs = st.text_input('fbs')
        
    with col3 : 
        restecg = st.text_input("restecg")        
        
    with col4:
        thalach = st.text_input("thalach")
    
    with col1:
        exang = st.text_input("exang")
    
    with col2:
        oldpeak = st.text_input("oldpeak")
    
    with col3 : 
       slope = st.text_input("slope")        
       
    with col4:
       ca = st.text_input("ca")
   
    with col1:
       thal = st.text_input("thal")
   

       
        
    #output
    result = ''
    
    if(st.button("predict")):
        inputs = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        inputs = [float(item) for item in inputs]
        data = np.asarray(inputs).reshape(1,-1)
        prediction = HeartModel.predict(data)
        if(prediction[0] == 0):
            result = 'The person is diabetic'
        else:
            result = 'The person is not diabetic'
        
    st.success(result)
    
    

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
        parkinsons_prediction = ParkinsonsModel.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)




















           