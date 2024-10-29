
import pickle
import pandas as pd
import streamlit as st

# Cargar el modelo de Random Forest
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Cargar el escalador
with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Título de la aplicación
st.title("Predicción de Depósitos en el Banco")

# Entradas del usuario
age = st.number_input("Edad", min_value=18, max_value=100, value=30)
balance = st.number_input("Saldo", min_value=-100000, max_value=1000000, value=0)
duration = st.number_input("Duración de la llamada", min_value=0, max_value=1000, value=10)
campaign = st.number_input("Número de contactos realizados", min_value=0, max_value=100, value=1)
pdays = st.number_input("Número de días desde la última llamada", min_value=-1, max_value=1000, value=-1)
default_numeric = st.selectbox("¿Tiene crédito por defecto?", options=[0, 1])
housing_numeric = st.selectbox("¿Tiene préstamo hipotecario?", options=[0, 1])
loan_numeric = st.selectbox("¿Tiene préstamo personal?", options=[0, 1])
contact_previ_numeric = st.number_input("Número de contactos previos", min_value=0, max_value=100, value=0)

# Al hacer clic en el botón de predicción
if st.button("Predecir"):
    # Crear un DataFrame con las entradas del usuario
    input_data = pd.DataFrame({
        'age': [age],
        'balance': [balance],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'default_numeric': [default_numeric],
        'housing_numeric': [housing_numeric],
        'loan_numeric': [loan_numeric],
        'contact_previ_numeric': [contact_previ_numeric],
    })

    # Escalar las entradas
    input_scaled = scaler.transform(input_data)

    # Hacer la predicción
    prediction = model.predict(input_scaled)

    # Mostrar el resultado
    if prediction[0] == 1:
        st.success("El cliente probablemente hará un depósito.")
    else:
        st.warning("El cliente probablemente no hará un depósito.")
