import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Choose Page : ', ('Dashboard', 'Prediction'))

if page == 'Dashboard' : 
    eda.run()
else:
    prediction.run()