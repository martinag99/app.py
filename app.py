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

#Leo el archivo pickle
with open('final_model.pkl', 'rb') as f_model:
    regresion = pickle.load(f_model)


classify = st.text_input('Input your sentence here:') 
  
    
def main():
    #titulo
    st.title('¿Tu noticia es Fake?')
    #titulo de sidebar
    st.sidebar.header('Complete:')
    
    
    #funcion para poner los parametros
    def user_input_parameters():
        titulo_noticia = st.sidebar.slider('Titulo')
        data = {'titulo_noticia': titulo_noticia}
        features = pd.DataFrame(data, index=[0])
        return features   
    df = user_input_parameters()
    
#Seleciono el modelo
 
    option = ['Regresión Logística']
    model = st.sidebar.selectbox('¿Qué modelo utilizará?', option)
    st.subheader('Parametros')
    st.subheader(model)
    st.write(df)
    
    if st.button('Correr'):
        if model == 'Regresión Logística':
            st.succes(classify(log_reg.predict(df)))
    
    




if __name__ == '__main__':
    main()    

