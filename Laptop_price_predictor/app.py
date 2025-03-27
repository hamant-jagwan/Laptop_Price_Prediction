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

# Ram
type = st.selectbox('Ram(in GB)', [2,4,6,8,16,24,32,64])

# Weight
weight = st.number_input('Weight of the Laptop')

# touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','1340x2160',
                                                '3200x1800','2880x1800','2560x1600','2560x1440',
                                                '2304x1440',])

# Cpu
cpu = st.selectbox('CPU', df['Cpu_brand'].unique())

# HDD
hdd = st.selectbox('HDD(in GB)', [0,8,128, 255, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0,8,128, 255, 512, 1024, 2048])

gpu = st.selectbox('GPU', df['Gpu_brand'].unique())

os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    pass