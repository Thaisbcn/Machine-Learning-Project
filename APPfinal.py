#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:/Users/thais/Documents/00_MACHINE_LEARNING/


# In[3]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import RobustScaler


# In[7]:


# Cargar el modelo y el escalador guardados
with open('random_forest_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Función para predecir y mostrar resultados
def predict_and_display(input_data):
    # Escalar las características de entrada usando el escalador cargado
    input_scaled = scaler.transform(input_data)

    # Realizar predicción
    y_pred = rf_model.predict(input_scaled)
    y_prob = rf_model.predict_proba(input_scaled)[:, 1]  # Probabilidad de la clase positiva

    # Mostrar resultados
    st.write(f"Predicción: {'Sí' if y_pred[0] == 1 else 'No'}")
    st.write(f"Probabilidad de 'Sí': {y_prob[0]:.2f}")

# Interfaz de usuario de Streamlit
st.title("Predicción de Depósito Bancario")

st.sidebar.header("Configuración de Entrada")

# Cargar datos procesados (puedes cambiar esta ruta si lo deseas)
banc_transformed = pd.read_csv('banc_transformed.csv')

# Mostrar las primeras filas del DataFrame para entender las variables
st.write("Primeras filas del dataset:")
st.write(banc_transformed.head())

# Ingresar los datos de todas las columnas
st.sidebar.header("Ingrese los datos del cliente")

# Variables numéricas
edad = st.sidebar.slider('Edad', min_value=18, max_value=100, value=18)
saldo = st.sidebar.slider('Saldo en cuenta', min_value=0, max_value=100000, value=0)
duracion = st.sidebar.slider('Duración de la llamada (minutos)', min_value=0, max_value=1000, value=0)
pdays = st.sidebar.slider('Días desde el último contacto', min_value=-1, max_value=1000, value=30)

# Variables categóricas (usar selectbox para las variables categóricas)
default = st.sidebar.selectbox('¿Tiene morosidad?', ['No', 'Sí'])
housing = st.sidebar.selectbox('¿Tiene hipoteca?', ['No', 'Sí'])
loan = st.sidebar.selectbox('¿Tiene crédito personal?', ['No', 'Sí'])
contact_prev = st.sidebar.selectbox('¿Fue contactado anteriormente?', ['No', 'Sí'])

# Estado civil (se puede usar multiple selectbox para las tres opciones)
marital = st.sidebar.selectbox('Estado Civil', ['Divorciado', 'Casado', 'Soltero'])

# Nivel educativo (también con selectbox para las tres opciones)
education = st.sidebar.selectbox('Nivel Educativo', ['Primario', 'Secundario', 'Terciario'])

# Convertir las respuestas categóricas a formato numérico
default_numeric = 1 if default == 'Sí' else 0
housing_numeric = 1 if housing == 'Sí' else 0
loan_numeric = 1 if loan == 'Sí' else 0
contact_prev_numeric = 1 if contact_prev == 'Sí' else 0

# Convertir las categorías de estado civil y nivel educativo en variables binarias
marital_divorced = 1 if marital == 'Divorciado' else 0
marital_married = 1 if marital == 'Casado' else 0
marital_single = 1 if marital == 'Soltero' else 0

education_primary = 1 if education == 'Primario' else 0
education_secondary = 1 if education == 'Secundario' else 0
education_tertiary = 1 if education == 'Terciario' else 0 
education_unknown = 1 if education == 'Desconocido' else 0 

# Crear el DataFrame de entrada per a la predicció
input_data = pd.DataFrame({
    'age': [edad],
    'balance': [saldo],
    'duration': [duracion],
    'pdays': [pdays],
    'default_numeric': [default_numeric],
    'housing_numeric': [housing_numeric],
    'loan_numeric': [loan_numeric],
    'contact_previ_numeric': [contact_prev_numeric],
    'marital_divorced': [marital_divorced],
    'marital_married': [marital_married],
    'marital_single': [marital_single],
    'education_primary': [education_primary],
    'education_secondary': [education_secondary],
    'education_tertiary': [education_tertiary],
    'education_unknown': [education_unknown]
})

input_data = input_data[scaler.feature_names_in_]

input_scaled = scaler.transform(input_data)


# In[8]:


jupyter nbconvert --to script APPfinal.ipynb

