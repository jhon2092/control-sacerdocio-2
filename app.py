import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- Protección por contraseña ---
st.title("🔐 Control Sacerdocio - Acceso restringido")
PASSWORD = "sacerdocio2025"
password_input = st.text_input("Ingresa la contraseña:", type="password")
if password_input != PASSWORD:
    st.warning("🔒 Acceso denegado. Ingresa la contraseña correcta.")
    st.stop()

# --- Aplicación principal ---
st.title("📋 Control de Asignaciones - Sacerdocio Aarónico")

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

# Columnas de tipo "visto"
columnas_check = [
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

# Crear DataFrame inicial con checkboxes en False
hoy = datetime.today().strftime('%d/%m/%Y')
data = []
for nombre in nombres:
    fila = {
        "Fecha": hoy,
        "Nombre": nombre
    }
    for col in columnas_check:
        fila[col] = False
    data.append(fila)

df = pd.DataFrame(data)

# Editor con casillas
st.subheader("✅ Marca los campos completados")
df_editado = st.data_editor(df, use_container_width=True)

# Botón de descarga
def descargar_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Control")
    return output.getvalue()

excel_data = descargar_excel(df_editado)
st.download_button("💾 Descargar Excel", data=excel_data, file_name="Control_Santa_Cena.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
