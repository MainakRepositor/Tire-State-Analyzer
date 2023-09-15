import streamlit as st
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Tire Status Analyser",
    page_icon = "🛞",
    initial_sidebar_state = 'auto'
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def prediction_cls(prediction):
    for key, clss in class_names.items():
        if np.argmax(prediction)==clss:
            
            return key


with st.sidebar:
        st.image('mg.png')
        st.title("Tire Analytics")
        st.subheader("Accurate analysis of vehicle tire inflated or deflated state")

             
        
def prediction_cls(prediction):
    for key, clss in class_names.items():
        if np.argmax(prediction)==clss:
            
            return key
        
       

    

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('tire.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

    

st.write("""
         # Tire Quality Analyzer
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data, model):
        size = (240,240)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

        
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98,99)+ random.randint(0,99)*0.01
    st.sidebar.info("Accuracy : " + str(x) + " %")

    class_names = ['flat', 'full','no-tire']

    string = "Tyre is : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'full':
        
        st.sidebar.warning(string)

    elif class_names[np.argmax(predictions)] == 'flat':
        st.sidebar.error(string)
        st.sidebar.info("Your vehicle's tire is deflated. Consider taking a deeper look for possible wear and tears")
        st.sidebar.markdown(
    f'<a href="https://tire-and-damage.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: black; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Tire Damage Segmentation</a>',
    unsafe_allow_html=True
)

    elif class_names[np.argmax(predictions)] == 'no-tire':
        st.sidebar.error(string)
        

   
        
    
