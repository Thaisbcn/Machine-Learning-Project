
import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo
ruta_modelo = 'random_forest_model.pkl'
ruta_escalador = 'robust_scaler.pkl'

with open(ruta_modelo, 'rb') as modelo_file:
    modelo = pickle.load(modelo_file)

with open(ruta_escalador, 'rb') as escalador_file:
    escalador = pickle.load(escalador_file)

# Título de la aplicación
st.title("Predicción de Depósito")

# Entradas del usuario
age = st.number_input("Edad:", min_value=0, max_value=120, value=30)
balance = st.number_input("Balance:", min_value=-100000.0, max_value=1000000.0, value=1000.0)
duration = st.number_input("Duración:", min_value=0, max_value=5000, value=200)
pdays = st.number_input("Pdays:", min_value=-1, max_value=1000, value=-1)
default_numeric = st.radio("¿Default?", options=[0, 1])
housing_numeric = st.radio("¿Vivienda?", options=[0, 1])
loan_numeric = st.radio("¿Préstamo?", options=[0, 1])
contact_previ_numeric = st.radio("Contacto previo?", options=[0, 1])

# Crear DataFrame a partir de las entradas
data = {
    "age": [age],
    "balance": [balance],
    "duration": [duration],
    "pdays": [pdays],
    "default_numeric": [default_numeric],
    "housing_numeric": [housing_numeric],
    "loan_numeric": [loan_numeric],
    "contact_previ_numeric": [contact_previ_numeric]
}

df = pd.DataFrame(data)

# Escalar los datos
datos_escalados = escalador.transform(df)

# Hacer predicciones
predicciones = modelo.predict(datos_escalados)

# Mostrar la predicción
st.write("Predicción del Depósito:", "Sí" if predicciones[0] == 1 else "No")
