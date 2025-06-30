import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

NOMBRES = [
    "Alvarez Guerrero, Robinson Javier", "Arrobo Ruíz, Liam Moises", "Bermeo Ramírez, Juan Rodolfo",
    "Betancourth Moncada, Jean Carlos", "Bohorquez Huriado, Steven Antonio", "Cedeño Granda, James Javier",
    "Cedeño Granda, Jose Carlos", "Correa Jimenez, Luis", "Correa Jimenez, Luis Miguel",
    "Espinoza Jumbo, Justin Ariel", "Espinoza Jumbo, Marcus Leonel", "Espinoza Mecias, Eythan Deyaer",
    "Espinoza Mesías, Deynner Javier", "García Bravo, José Eduardo", "Granda Quezada, Xavier Isaac",
    "Guerrero Leon, Jean Paolo", "Jarama Sanmartin, Adrian Ezequiel", "Jaramillo Ortiz, Pablo Alejandro",
    "Jiron Rojas, Sleyter Alexander", "Lapo Ramirez, Jeremy Santiago", "Loayza Romero, Anthony Paul",
    "Manzaba Jama, Jean Carlos", "Matamoros Davila, Jorge Abraham", "Montesinos Ruiz, Eliù Santiago",
    "Ordoñez Orden, Elias Aaron", "Ordóñez Orden, Josue Fernando", "Perez Zhindon, Anthony Steveen",
    "Pilay Otuna, Ariel Antonio", "Pineda Gómez, Wesley Yamir", "Porras Jaya, Edwin Alexander",
    "Reyna Robayo, Benjamin Alfonso", "Rodriguez Briñez, Jonathan Silvino", "Rojas Valdez, Cristopher Josua",
    "Romero Sánchez, Ronald Eduardo", "Vargas Correa, Jorvin Sebastian", "Villamil Cedeño, Jeremy Jerly",
    "Viñan Valdez, Irvin Wladimir"
]

COLUMNAS = [
    "Fecha", "Nombre", "Preparar Santa Cena", "Bendecir Santa Cena", "Repartir Santa Cena", "Levantar Santa Cena",
    "Escuela Dominical (1º/3º)", "Cuórum Aarónico (2º/4º)", "Seminario", "Discurso en la Sacramental",
    "Recomendación del templo activa"
]

def crear_df(fecha):
    f = fecha.strftime("%d/%m/%Y")
    return pd.DataFrame([[f, nombre] + [""] * (len(COLUMNAS) - 2) for nombre in NOMBRES], columns=COLUMNAS)

def exportar_excel(df):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Asignaciones")
    return buffer.getvalue()

st.set_page_config(page_title="Control Sacerdocio Aarónico", layout="wide")
st.title("📋 Control Sacerdocio Aarónico")

if "df" not in st.session_state:
    st.session_state.df = crear_df(datetime.today())

fecha = st.date_input("Fecha de la reunión", datetime.today())
st.session_state.df["Fecha"] = fecha.strftime("%d/%m/%Y")

df_editado = st.data_editor(st.session_state.df, use_container_width=True, num_rows="fixed")
st.session_state.df = df_editado

col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "💾 Descargar Excel",
        data=exportar_excel(df_editado),
        file_name="Control_Sacerdocio.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
with col2:
    if st.button("🔄 Reiniciar tabla"):
        st.session_state.df = crear_df(datetime.today())
        st.experimental_rerun()


