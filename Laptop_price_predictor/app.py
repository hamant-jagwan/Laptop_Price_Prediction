import streamlit as st
import pickle

# import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
st.title('Laptop Predictor')

# Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'IPS',
#        'ppi', 'Cpu_brand', 'HDD', 'SSD', 'Gpu_brand', 'os'],
#       dtype='object')

# brand

company = st.selectbox('Brand', df['Company'].unique())

# type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())
