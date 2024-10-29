

import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo y el escalador
with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Función de predicción
def predict_deposit(age, balance, duration, campaign, contact_previ_numeric, default_numeric=0, housing_numeric=0, loan_numeric=0, pdays=999):
    input_data = pd.DataFrame({
        'age': [age],
        'balance': [balance],
        'duration': [duration],
        'campaign': [campaign],
        'contact_previ_numeric': [contact_previ_numeric],
        'default_numeric': [default_numeric],
        'housing_numeric': [housing_numeric],
        'loan_numeric': [loan_numeric],
        'pdays': [pdays]
    })
    
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    
    return 'Sí' if prediction[0] == 1 else 'No'

# Configuración de la app Streamlit
st.title("Predicción de Depósito a Plazo")

st.write("Ingrese la información del cliente para predecir si contratará un depósito a plazo.")

# Entradas de usuario
age = st.number_input("Edad", min_value=18, max_value=100, value=30)
balance = st.number_input("Saldo en cuenta", min_value=0, value=1000)
duration = st.number_input("Duración de la última campaña", min_value=0, value=300)
campaign = st.number_input("Número de contactos realizados", min_value=1, value=1)
contact_previ_numeric = st.number_input("Número de contactos previos", min_value=0, value=0)
default_numeric = st.selectbox("¿Tiene crédito en incumplimiento?", ["No", "Sí"], index=0)
housing_numeric = st.selectbox("¿Tiene préstamo de vivienda?", ["No", "Sí"], index=0)
loan_numeric = st.selectbox("¿Tiene préstamo personal?", ["No", "Sí"], index=0)
pdays = st.number_input("Días desde último contacto", min_value=-1, value=999)

# Convertir selecciones a valores numéricos
default_numeric = 1 if default_numeric == "Sí" else 0
housing_numeric = 1 if housing_numeric == "Sí" else 0
loan_numeric = 1 if loan_numeric == "Sí" else 0

# Predicción
if st.button("Predecir"):
    resultado = predict_deposit(age, balance, duration, campaign, contact_previ_numeric, default_numeric, housing_numeric, loan_numeric, pdays)
    st.write(f"¿El cliente contratará un depósito a plazo? {resultado}")

