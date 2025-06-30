import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- Configuración de acceso ---
st.title("🔐 Control Sacerdocio - Acceso restringido")

PASSWORD = "sacerdocio2025"  # Cambia esto por una contraseña segura

# Campo de contraseña
password_input = st.text_input("Ingresa la contraseña:", type="password")

if password_input != PASSWORD:
    st.warning("🔒 Acceso denegado. Ingresa la contraseña correcta.")
    st.stop()  # Detiene la app aquí si la contraseña no es correcta

# --- App principal ---
st.title("📋 Control de Asignaciones - Sacerdocio Aarónico")

# Lista de nombres
nombres = [
    "Alvarez Guerrero, Robinson Javier",
    "Arrobo Ruíz, Liam Moises",
    "Bermeo Ramírez, Juan Rodolfo",
    "Betancourth Moncada, Jean Carlos",
    "Bohorquez Huriado, Steven Antonio",
    "Cedeño Granda, James Javier",
    "Cedeño Granda, Jose Carlos",
    "Correa Jimenez, Luis",
    "Correa Jimenez, Luis Miguel",
    "Espinoza Jumbo, Justin Ariel",
    "Espinoza Jumbo, Marcus Leonel",
    "Espinoza Mecias, Eythan Deyaer",
    "Espinoza Mesías, Deynner Javier",
    "García Bravo, José Eduardo",
    "Granda Quezada, Xavier Isaac",
    "Guerrero Leon, Jean Paolo",
    "Jarama Sanmartin, Adrian Ezequiel",
    "Jaramillo Ortiz, Pablo Alejandro",
    "Jiron Rojas, Sleyter Alexander",
    "Lapo Ramirez, Jeremy Santiago",
    "Loayza Romero, Anthony Paul",
    "Manzaba Jama, Jean Carlos",
    "Matamoros Davila, Jorge Abraham",
    "Montesinos Ruiz, Eliù Santiago",
    "Ordoñez Orden, Elias Aaron",
    "Ordóñez Orden, Josue Fernando",
    "Perez Zhindon, Anthony Steveen",
    "Pilay Otuna, Ariel Antonio",
    "Pineda Gómez, Wesley Yamir",
    "Porras Jaya, Edwin Alexander",
    "Reyna Robayo, Benjamin Alfonso",
    "Rodriguez Briñez, Jonathan Silvino",
    "Rojas Valdez, Cristopher Josua",
    "Romero Sánchez, Ronald Eduardo",
    "Vargas Correa, Jorvin Sebastian",
    "Villamil Cedeño, Jeremy Jerly",
    "Viñan Valdez, Irvin Wladimir"
]

# Columnas
columnas = [
    "Fecha",
    "Nombre",
    "Preparar Santa Cena",
    "Bendecir Santa Cena",
    "Repartir Santa Cena",
    "Levantar Santa Cena",
    "Escuela Dominical (1º/3º)",
    "Cuórum Aarónico (2º/4º)",
    "Seminario",
    "Discurso en la Sacramental",
    "Recomendación del templo activa"
]

# Crear DataFrame
hoy = datetime.today().strftime('%d/%m/%Y')
df = pd.DataFrame([[hoy, nombre] + [""] * (len(columnas) - 2) for nombre in nombres], columns=columnas)

# Mostrar editable
st.subheader("📄 Lista de Asignaciones (editable)")
df_editado = st.data_editor(df, num_rows="fixed")

# Botón de descarga
def descargar_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Control")
    return output.getvalue()

excel_data = descargar_excel(df_editado)
st.download_button("💾 Descargar Excel", data=excel_data, file_name="Control_Santa_Cena.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

