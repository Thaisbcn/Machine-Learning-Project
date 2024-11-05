

# Cargar el modelo y el escalador
with open('robust_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Función de predicción
def predict_deposit(age, balance, duration, contact_previ_numeric, default_numeric=0, housing_numeric=0, loan_numeric=0, pdays=999,
                    marital_divorced=0, marital_married=0, marital_single=0, 
                    education_primary=0, education_secondary=0, education_tertiary=0, education_unknown=0):
    input_data = pd.DataFrame({
        'age': [age],
        'balance': [balance],
        'duration': [duration],
        'contact_previ_numeric': [contact_previ_numeric],
        'default_numeric': [default_numeric],
        'housing_numeric': [housing_numeric],
        'loan_numeric': [loan_numeric],
        'pdays': [pdays],
        'marital_divorced': [marital_divorced],
        'marital_married': [marital_married],
        'marital_single': [marital_single],
        'education_primary': [education_primary],
        'education_secondary': [education_secondary],
        'education_tertiary': [education_tertiary],
        'education_unknown': [education_unknown]
    })
    
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    
    return 'Sí' if prediction[0] == 1 else 'No'

# Configuración de la app Streamlit
st.title("Predicción de Depósito a Plazo")

st.write("Ingrese la información del cliente para predecir si contratará un depósito a plazo.")

# Entradas de usuario
age = st.number_input("Edad", min_value=18, max_value=100, value=18)
balance = st.number_input("Saldo en cuenta", min_value=0, value=100000)
duration = st.number_input("Duración total de las llamadas", min_value=0, value=300)
contact_previ_numeric = st.number_input("Número de contactos previos", min_value=0, value=0)
default_numeric = st.selectbox("¿Tiene morosidad?", ["No", "Sí"], index=0)
housing_numeric = st.selectbox("¿Tiene hipoteca?", ["No", "Sí"], index=0)
loan_numeric = st.selectbox("¿Tiene préstamo personal?", ["No", "Sí"], index=0)
pdays = st.number_input("Días desde último contacto", min_value=-1, value=365)

# Entradas para estado civil
marital_status = st.selectbox("Estado Civil", ["Divorciado", "Casado", "Soltero"], index=2)

# Entradas para educación
education_status = st.selectbox("Nivel de Educación", ["Primaria", "Secundaria", "Terciaria", "Desconocido"], index=3)

# Convertir selecciones a valores numéricos
default_numeric = 1 if default_numeric == "Sí" else 0
housing_numeric = 1 if housing_numeric == "Sí" else 0
loan_numeric = 1 if loan_numeric == "Sí" else 0

# Asignar directamente las columnas dummy basadas en las selecciones
marital_divorced = 1 if marital_status == "Divorciado" else 0
marital_married = 1 if marital_status == "Casado" else 0
marital_single = 1 if marital_status == "Soltero" else 0

education_primary = 1 if education_status == "Primaria" else 0
education_secondary = 1 if education_status == "Secundaria" else 0
education_tertiary = 1 if education_status == "Terciaria" else 0
education_unknown = 1 if education_status == "Desconocido" else 0

# Predicción
if st.button("Predecir"):
    resultado = predict_deposit(age, balance, duration, contact_previ_numeric, default_numeric, housing_numeric, loan_numeric, pdays,
                                 marital_divorced, marital_married, marital_single,
                                 education_primary, education_secondary, education_tertiary, education_unknown)
    st.write(f"¿El cliente contratará un depósito a plazo? {resultado}")

