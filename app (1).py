import streamlit as st
import libreria_funciones as lf

st.title("Paradigma de la Programacion")

st.sidebar.image("logo.jpeg")

st.sidebar.title("Parametros")

capital = st.number_input("Ingrese el capital", value=1000)
tasa_anual  = st.number_input("Ingrese la tasa anual", value =0-15)
dias_mora  = st.number_input("Ingrese dias", value= 30)

resultado = lf.calcular_interes_mora(capital,tasa_anual, dias_mora)

st.write("Elaborado Por: Luis Gavino ")
