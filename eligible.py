import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from io import BytesIO
import requests



with open('pipe1.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.title('Marriage Eligibility Predictor')
image_url = "https://clipground.com/images/the-wedding-png-2.png"  # Replace with your image URL
try:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    st.image(image,  use_column_width=True)
except Exception as e:
    st.error(f"Error loading image: {str(e)}")



name = st.text_input('Enter your name')
age = st.number_input('Enter your age (5yrs-100yrs)', min_value=5, max_value=100, value=25)
gender = st.radio('Select your gender', ['Male', 'Female'])
country = st.selectbox('Select your country', ['India', 'South Korea', 'US', 'Germany', 'China', 'Japan'])


user_data = pd.DataFrame({
    'AGE': [age],
    'GENDER': [gender.upper()],
    'COUNTRY': [country.upper()]
})


if st.button('Predict Eligibility'):
    try:
       
        prediction = pipeline.predict(user_data)
        
        
        st.subheader('Prediction Result')
        if prediction[0] == 'YES':
            st.success(f'{name} is eligible!')
        else:
            st.error(f'{name} is not eligible.')

        
    
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
       
        st.write("Please try a different input or contact support for assistance.")