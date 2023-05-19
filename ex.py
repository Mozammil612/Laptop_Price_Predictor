import streamlit as st
import numpy as np
from pickle import load
import pandas as pd

#Loading pretrained classifier from pickle file
model = pickle.load(open('knn_model.pkl', 'rb'))
#file = open("knn_model.pkl",'rb')

#model = pickle.load(file)



# Streamlit web app
st.title("Laptop Price Prediction")

# Display user input fields
st.write('Brand: HP = 5, APPLE = 1, acer = 14, DELL = 3, Lenovo = 7, RedmiBook = 10, MSI = 8, ASUS = 2, Infinix = 6, realme = 15, ALIENWARE = 0, SAMSUNG = 11, Ultimus = 12, Nokia = 9')
Brand = st.int_input('Enter Brand: ')

st.write('Operating System: 64 bit Windows 11 Operating System = 4, 64 bit Windows 10 Operating System = 3, 64 bit DOS Operating System = 2, 32 bit Windows 11 Operating System = 0, 64 bit Chrome Operating System = 1')
OS = st.int_input('Enter Operating System: ')


st.write('Processor:  Intel Core i3 Processor = 13, Intel Core i5 Processor = 14, Intel Core i7 Processor = 15, Intel Core i9 Processor = 16, AMD Ryzen 9 Octa Core Processor = 10, AMD Ryzen 7 Octa Core Processor = 8, AMD Ryzen 5 Hexa Core Processor = 6, AMD Ryzen 3 Dual Core Processor = 2, AMD Ryzen 5 Quad Core Processor = 7, Intel Celeron Dual Core Processor = 11, AMD Ryzen 3 Quad Core Processor = 4, Intel Pentium Quad Core Processor = 17, Intel Celeron Quad Core Processor = 12, Intel Pentium Silver Processor = 18, AMD Athlon Dual Core Processor = 0, AMD Ryzen 5 Dual Core Processor = 5, AMD Ryzen 7 Quad Core Processor = 9, AMD Dual Core Processor = 1, AMD Ryzen 3 Hexa Core Processor = 3')
Processor = st.int_input('Enter Processor in numbers: ')


st.write('RAM:  8 GB DDR4 RAM = 15, 16 GB DDR4 RAM = 1, 16 GB DDR5 RAM = 2, 4 GB DDR4 RAM = 12, 8 GB LPDDR4X RAM = 17,  16 GB LPDDR4X RAM = 5 , 32 GB DDR5 RAM = 9, 16 GB LPDDR5 RAM = 6 , 4 GB LPDDR4 RAM = 13, 16 GB Unified Memory RAM = 7, 8 GB Unified Memory RAM = 18, 4 GB LPDDR4X RAM = 14, 8 GB DDR5 RAM = 16, 32 GB DDR4 RAM = 8, 32 GB Unified Memory RAM = 11, 16 GB LPDDR4 RAM = 4, 128 GB SSD for Reduced Boot Up Time and in Game LoadingUpgradable SSD Upto 512 GB and RAM8 GB DDR4 RAM = 0,  32 GB LPDDR4X RAM = 10, 16 GB LPDDR3 RAM = 3')
RAM = st.int_input('Enter the RAM: ')
                                                                                      


st.write('Storage: 512 GB SSD = 9, 1 TB SSD = 3 , 256 GB SSD = 8, 1 TB HDD256 GB SSD = 1 , 1 TB HDD = 0, 2 TB SSD = 6, 128 GB SSD = 4, 1 TB HDD512 GB SSD = 2 , 128 GB SSD1 TB HDD128 GB SSD = 5, 256 GB HDD256 GB SSD = 7')
Storage = st.int_input('Enter the Storage: ')       
        
btn_click = st.button('Predict')

if btn_click == True:
    if Brand and OS and Processor and RAM and Storage:
        querry = [[Brand, OS, Processor, RAM, Storage ]]
        pred = model.predict(querry)
        st.success(pred)
    else:
        st.error("Enter the Values Properly")














