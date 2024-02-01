import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #Menambahkan deskripsi
    st.write('This page was created by Nakia Melvana')

    #Membuat title
    st.title('Diabetes Detection')
    #Menambahkan deskripsi
    st.write('This page can be utilized for predicting Diabetes on a patient')

    #Menambahkan gambar
    image = Image.open('diabetes.jpg')
    st.image(image, caption = 'Diabetes Detection')

    #Membuat garis
    st.markdown('----')

    #Membuat title
    st.write('## Dataset')

    #Masukkan pandas dataframe
    #Show dataframe
    df = pd.read_csv('diabetes_data.csv')
    st.dataframe(df)

    #Membuat garis
    st.markdown('----')

    #Membuat title
    st.write('## Data Description')
    st.write('- `Age`: 13-level age category')
    st.write("- `Sex`: patient's gender (1: male; 0: female)")
    st.write('- `HighChol`: 0 = no high cholesterol 1 = high cholesterol')
    st.write('- `CholCheck`: 0 = no cholesterol check in 5 years 1 = yes cholesterol check in 5 years')
    st.write('- `BMI`: Body Mass Index')
    st.write('- `Smoker`: Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no 1 = yes')
    st.write('- `HeartDiseaseorAttack`: coronary heart disease (CHD) or myocardial infarction (MI) 0 = no 1 = yes')
    st.write('- `PhysActivity`: physical activity in past 30 days - not including job 0 = no 1 = yes')
    st.write('- `Fruits`: Consume Fruit 1 or more times per day 0 = no 1 = yes')
    st.write('- `Veggies`: Consume Vegetables 1 or more times per day 0 = no 1 = yes')
    st.write('- `HvyAlcoholConsump`: (adult men >=14 drinks per week and adult women>=7 drinks per week) 0 = no 1 = yes')
    st.write('- `GenHlth`: Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor')
    st.write('- `MentHlth`: days of poor mental health scale 1-30 days')
    st.write('- `PhysHlth`: physical illness or injury days in past 30 days scale 1-30)')
    st.write('- `DiffWalk`: Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes')
    st.write('- `Stroke`: you ever had a stroke. 0 = no, 1 = yes')
    st.write('- `HighBP`: 0 = no high, BP 1 = high BP')
    st.write('- `Diabetes`: 0 = no diabetes, 1 = diabetes')


    #Membuat bar plot
    st.write('#### Age Distribution')
    fig = plt.figure(figsize=(15,8))
  # plot kolom diabetes dengan menggunakan countplot
    sns.countplot(x='Diabetes', data=df, color='magenta')
    # set judul
    plt.title('Diabetes Distribution')
    # set x label
    plt.xlabel('Diabetes')
    # set y label
    plt.ylabel('Frequency')
    st.pyplot(fig)


    # Membuat correlation plot
    st.write('#### Correlation Bar Plot')
    fig = plt.figure(figsize=(15,10))
    df.drop('Diabetes', axis=1).corrwith(df.Diabetes).plot(kind='bar', grid=True, title="Correlation with Diabetes",color="magenta")
    st.pyplot(fig)

    # Membuat countplot
    st.write('#### Physical Activity vs Diabetes')
    fig = plt.figure(figsize=(15,10))
    sns.countplot(data=df, x='PhysActivity', hue='Diabetes', palette = ['pink','Magenta'])
    # set judul
    plt.title('Physical Activity on Diabetes')
    # set x label
    plt.xlabel('PhysActivity')
    # set y label
    plt.ylabel('Frequency')
    st.pyplot(fig)

    # Membuat countplot
    st.write('#### High Blood Pressure vs Diabetes')
    fig = plt.figure(figsize=(15,10))
    # Plot menggunakan countplot
    sns.countplot(data=df, x='HighBP', hue='Diabetes', palette = ['pink','Magenta'])
    # set judul
    plt.title('Blood Pressure on Diabetes')
    # set x label
    plt.xlabel('High Blood Pressure')
    # set y label
    plt.ylabel('Frequency')
    st.pyplot(fig)


if __name__ == '__main__':
    run()
