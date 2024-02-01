import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load semua files yang dibutuhkan
with open('list_num_cols.txt', 'r') as file_1:
  list_num_cols = json.load(file_1)
with open('list_cat_cols.txt', 'r') as file_2:
  list_cat_cols = json.load(file_2)
with open('model_xgb.pkl', 'rb') as file_3:
  model_xgb = pickle.load(file_3)

# Membuat fungsi run() untuk di panggi di file lain
def run():
    with st.form('Diabetes Detection'):
        st.write ('# Background')
        #field Age
        Age = st.slider('Age', 1, 13, 10, help= ' **1** = 18-24 | **2** = 25-29 | **3** = 30-34 | **4** = 35-39 | **5** = 40-44 | **6** = 45-49 | **7** = 50-54 | **8** = 55-59 | **9** = 60-64 | **10** = 65-69 | **11** = 70-74 | **12** = 75-79 | **13** = 80 or older')
        #Field Sex
        Sex = st.selectbox('Sex',('Female', 'Male'))


        # Membuat pembatas
        st.markdown('----')
        # Membuat keterangan 
        st.write('# Health Check')
        # st.write('### Information')
        # st.write('**Pay** : -2 = No Transaction, -1 = Pay Duly, 1-8 = Payment Delay 1-9 Month')

        #Field HighChol
        HighChol = st.selectbox('High Cholesterol (0 = No, 1 = Yes)', (0, 1))
        CholCheck = st.selectbox('Cholesterol Check in 5 years (0 = No, 1 = Yes)', (0, 1))
        BMI = st.number_input('Body Mass Index(BMI)', min_value= 12, max_value= 98, value = 26)
        Smoker = st.selectbox('Smoked at least 100 cigarettes? (0 = No, 1 = Yes)',(0, 1))
        HeartDiseaseorAttack = st.selectbox('Heart Disease or Attack (0 = No, 1 = Yes)',(0, 1), help= 'coronary heart disease (CHD) or myocardial infarction (MI)')
        PhysActivity = st.selectbox('Physical Activity in past 30 days - not including job? (0 = No, 1 = Yes)',(0, 1), help=  'physical activity in past 30 days - not including job')
        Fruits = st.selectbox('Consume Fruit 1 or more times per day? (0 = No, 1 = Yes)',(0, 1))
        Veggies = st.selectbox('Consume Vegetables 1 or more times per day? (0 = No, 1 = Yes)', (0, 1))
        HvyAlcoholConsump = st.selectbox('Heavy Alcohol Consumption? (0 = No, 1 = Yes)',(0, 1),help='adult men >=14 drinks per week and adult women>=7 drinks per week')
        GenHlth = st.selectbox('Would you say that in general your health is: scale 1-5', (1,2,3,4,5))
        MentHlth = st.slider('days of poor mental health scale 1-30 days', 1,30,0)
        PhysHlth = st.slider('physical illness or injury days in past 30 days scale 1-30', 1,30,0)
        DiffWalk = st.selectbox('Do you have serious difficulty walking or climbing stairs? (0 = No, 1 = Yes)',(0, 1))
        Stroke = st.selectbox('you ever had a stroke? (0 = No, 1 = Yes)', (0, 1))
        HighBP = st.selectbox('High Blood Preassure? (0 = No, 1 = Yes)',(0, 1))

        #membuat submit button
        submitted = st.form_submit_button('Predict')

    #Inference
    data_inf = {
      'Age' : Age, 
      'Sex': Sex, 
      'HighChol' : HighChol, 
      'CholCheck' : CholCheck, 
      'BMI' : BMI, 
      'Smoker' : Smoker,
      'HeartDiseaseorAttack' : HeartDiseaseorAttack, 
      'PhysActivity' : PhysActivity, 
      'Fruits' : Fruits, 
      'Veggies' : Veggies,
      'HvyAlcoholConsump': HvyAlcoholConsump, 
      'GenHlth' : GenHlth, 
      'MentHlth': MentHlth, 
      'PhysHlth' : PhysHlth, 
      'DiffWalk' : DiffWalk,
      'Stroke' : Stroke, 
      'HighBP' : HighBP

    }

    # Menampilkan dataframe data inference
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    #Logic ketika predict button ditekan
    if submitted:
        #predict using linear reg model
        y_pred_inf = model_xgb.predict(data_inf)
        
        st.write('## Diabetes? = ', str(int(y_pred_inf)))
        st.write('### 0 = No, 1 = Yes')

if __name__ == '__main__':
   run()