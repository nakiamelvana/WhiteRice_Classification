import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


# Load Models
model_ann = load_model('model_InceptionV3.h5')

# mendefinisikan fungsi untuk prediksi
def predict_image(img):
    # resize image untuk match dengan model's expected input shape
    img = img.resize((224, 224))

    # Convert gambar numpy array
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # Normalisasi gambar
    x /= 255.0

    # prediksi probabilitas kelas
    classes = model_ann.predict(x)

    # Map predicted probabilities ke setiap kelas
    predicted_class = np.argmax(classes)
    threshold = 0.5  # Define the threshold

    if classes[0, predicted_class] < threshold:
        return 'Prediction: Unknown'
    else:
        class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
        predicted_class_name = class_names[predicted_class]
        return f'Prediction: {predicted_class_name} with confidence {classes[0, predicted_class]}'
    

# Membuat fungsi run() untuk di panggi di file lain
def run():
    st .title("White Rice Variety Classification")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Load image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # membuat prediksi
        result = predict_image(image)
        st.write(result)

if __name__ == '__main__':
   run()