import streamlit as st
import libreria_funciones as lf

st.title("Paradigma de la Programacion")

st.sidebar.image("logo.jpeg")

st.sidebar.title("Parametros")

capital = st.number_input("Ingrese el capital")
tasa_anual  = st.number_input("Ingrese la tasa anual")
dias_mora  = st.number_input("Ingrese dias")


st.write("Elaborado Por: Luis Gavino ")
