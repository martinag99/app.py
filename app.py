# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:06:22 2023

@author: mgarcia
"""


import streamlit as st
import pickle
import pandas as pd


"Trabajamos a partir del dataset de noticias falsas y verdades."
"Predecimos si una noticia es fake a través de las palabras que contiene en su titulo"


modelo = 'C:/Users/mgarcia/Downloads/TP final/final_model.pkl'



with open(modelo, 'rb') as f_model:
    regresion = pickle.load(f_model)

#funcion para clasificar
def classify(num):
    if num == 0:
        return 'True'
    else:
        
        return 'False'

def main():
    #titulo
    st.title('Titulo de la naticia')
    #titulo de sidebar
    st.sidebar.header('Completar')
    
    

    #funcion para poner los parametros
    def user_input_parameters():
        titulo_noticia = st.text_input("Noticia")
        data = {"Noticia": titulo_noticia}
        features = pd.DataFrame(data, index=[0])
        return features   
    df = user_input_parameters()
    
    #escoger el modelo preferido
    option = ['Regresión Logística']
    model = st.sidebar.selectbox('Escoja el modelo a utilizar', option)

    st.subheader('Modelo Seleccionado')
    st.subheader(model)
    st.write(df)

    if st.button('Procesar'):
        if model == 'Regresión Logística':
            st.success(classify(regresion.predict(df)))


if __name__ == '__main__':
    main()    
    