
import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# T�tulo de la aplicaci�n
st.title("Predicci�n de Dep�sito a Plazo (clasificaci�n supervisada)")

# Entrada de datos del usuario
age = st.number_input('Edad', min_value=18)
balance = st.number_input('Saldo', min_value=0)
duration = st.number_input('Duraci�n total de las llamadas en minutos', min_value=0)
pdays = st.number_input("D�as que han pasado desde el �ltimo contacto", min_value=0, value=0)
default_numeric = st.selectbox("�Tiene morosidad?", ["No", "S�"], index=0)
housing_numeric = st.selectbox("�Tiene hipoteca?", ["No", "S�"], index=0)
loan_numeric = st.selectbox("�Tiene pr�stamo personal?", ["No", "S�"], index=0)
contact_previ_numeric = st.number_input('N� de veces contactado', min_value=0)

# Convertir selecciones a valores num�ricos
default_numeric = 1 if default_numeric == "S�" else 0
housing_numeric = 1 if housing_numeric == "S�" else 0
loan_numeric = 1 if loan_numeric == "S�" else 0

# Crear un DataFrame amb les entrades
user_data = pd.DataFrame({
    'age': [age],
    'balance': [balance],
    'duration': [duration],
    'pdays': [pdays],
    'default_numeric': [default_numeric],
    'housing_numeric': [housing_numeric],
    'loan_numeric': [loan_numeric],
    'contact_previ_numeric': [contact_previ_numeric],
})

# Estandarizar las entradas
user_data_standardized = scaler.transform(user_data)

# Realizar la predicci�n
prediction = model.predict(user_data_standardized)

# Mostrar la predicci�n
st.write(f'Predicci�n de si realizar� un dep�sito bancario: {"S�" if prediction[0] == 1 else "No"}')
