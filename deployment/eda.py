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
    st.title('White Rice Variety Classification')
    #Menambahkan deskripsi
    st.write('This page can be utilized for classify white rice variety')

    # Menambahkan gambar
    image = Image.open('ipsala.jpg')
    st.image(image, caption='Ipsala White Rice Variety', use_column_width=True)

    #Membuat garis
    st.markdown('----')

    #Membuat title
    st.write('## Dataset')

    #Masukkan pandas dataframe
    #Show dataframe
    df = pd.read_csv('RiceDataset.csv')
    st.dataframe(df)

    #Membuat garis
    st.markdown('----')

    #Membuat title
    st.write('## Rice Image Dataset')
    st.write('DATASET: https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset/data')
   
    
    st.write('## Highlihgts:')
    st.write('- Arborio, Basmati, Ipsala, Jasmine and Karacadag rice varieties were used.')
    st.write('- The dataset has 7.5K images including 1.5K pieces from each rice variety.')
    st.write('- The dataset trained using transfer learning InceptionV3')

    st.write("## Citation:")
    st.write('Koklu, M., Cinar, I., & Taspinar, Y. S. (2021). Classification of rice varieties with deep learning methods. Computers and Electronics in Agriculture, 187, 106285. https://doi.org/10.1016/j.compag.2021.106285')
    st.write('Cinar, I., & Koklu, M. (2021). Determination of Effective and Specific Physical Features of Rice Varieties by Computer Vision In Exterior Quality Inspection. Selcuk Journal of Agriculture and Food Sciences, 35(3), 229-243. https://doi.org/10.15316/SJAFS.2021.252')
    st.write('Cinar, I., & Koklu, M. (2022). Identification of Rice Varieties Using Machine Learning Algorithms. Journal of Agricultural Sciences https://doi.org/10.15832/ankutbd.862482')
    st.write('Cinar, I., & Koklu, M. (2019). Classification of Rice Varieties Using Artificial Intelligence Methods. International Journal of Intelligent Systems and Applications in Engineering, 7(3), 188-194. https://doi.org/10.18201/ijisae.2019355381')


if __name__ == '__main__':
    run()
