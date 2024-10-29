

import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo y el escalador
with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Funci�n de predicci�n
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
    
    return 'S�' if prediction[0] == 1 else 'No'

# Configuraci�n de la app Streamlit
st.title("Predicci�n de Dep�sito a Plazo")

st.write("Ingrese la informaci�n del cliente para predecir si contratar� un dep�sito a plazo.")

# Entradas de usuario
age = st.number_input("Edad", min_value=18, max_value=100, value=30)
balance = st.number_input("Saldo en cuenta", min_value=0, value=1000)
duration = st.number_input("Duraci�n de la �ltima campa�a", min_value=0, value=300)
campaign = st.number_input("N�mero de contactos realizados", min_value=1, value=1)
contact_previ_numeric = st.number_input("N�mero de contactos previos", min_value=0, value=0)
default_numeric = st.selectbox("�Tiene cr�dito en incumplimiento?", ["No", "S�"], index=0)
housing_numeric = st.selectbox("�Tiene pr�stamo de vivienda?", ["No", "S�"], index=0)
loan_numeric = st.selectbox("�Tiene pr�stamo personal?", ["No", "S�"], index=0)
pdays = st.number_input("D�as desde �ltimo contacto", min_value=-1, value=999)

# Convertir selecciones a valores num�ricos
default_numeric = 1 if default_numeric == "S�" else 0
housing_numeric = 1 if housing_numeric == "S�" else 0
loan_numeric = 1 if loan_numeric == "S�" else 0

# Predicci�n
if st.button("Predecir"):
    resultado = predict_deposit(age, balance, duration, campaign, contact_previ_numeric, default_numeric, housing_numeric, loan_numeric, pdays)
    st.write(f"�El cliente contratar� un dep�sito a plazo? {resultado}")

