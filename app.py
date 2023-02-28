# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:09:25 2023

@author: mgarcia
"""

#importar las librerias necesarias

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st
import pickle
import pandas as pd

st.markdown('fake.img', nsafe_allow_html=True)
st.title('Stop Fake nwes')

#Leo el archivo pickle
with open('final_model.pkl', 'rb') as f_model:
    regresion = pickle.load(f_model)


def classify(num):
    if num == 0:
        return 'True'
    else:
        return 'False'

def main():
    #titulo
    st.title('¿Estás leyendo un noticia Fake?')
    #titulo de sidebar
    st.sidebar.header('Complete')
    
    
    #funcion para poner los parametros
    def user_input_parameters():
        text = st.text_input('text')
        data = {'text': text}
        features = pd.DataFrame(data, index=[0])
        return features   
    df = user_input_parameters()
    
#Seleciono el modelo
 
    option = ['Regresión Logística']
    model = st.sidebar.selectbox('¿Qué modelo desea utilizar?', option)

    st.subheader('')
    st.subheader(model)
    st.write(df)
    
    if st.button('Correr Modelo'):
        if model == 'Regresión Logística':
            st.succes(classify(regresion.predict(df)))
            
                     
if __name__ == '__main__':
    main()    

