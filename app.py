import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮")

st.title("🧮 Resuelve la ecuación de primer grado")

# Generar una ecuación aleatoria ax + b = c
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.x = random.randint(-10, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b
    st.session_state.intento = ""

# Mostrar la ecuación
a = st.session_state.a
b = st.session_state.b
c = st.session_state.c

# Mostrar ecuación en formato ax + b = c
ecuacion = f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}"
st.markdown(f"### ¿Cuál es el valor de `x` en la ecuación?")
st.latex(ecuacion)

# Campo para ingresar la respuesta (solo enteros)
respuesta = st.text_input("Tu respuesta (solo enteros):", value=st.session_state.intento)

# Botón para verificar
if st.button("Verificar"):
    try:
        respuesta_entero = int(respuesta)
        st.session_state.intento = respuesta_entero
        if respuesta_entero == st.session_state.x:
            st.success("¡Correcto! 🎉")
            st.balloons()
        else:
            st.error("❌ Incorrecto. Intenta de nuevo.")
    except ValueError:
        st.warning("⚠️ Por favor, ingresa un número entero.")

# Botón para generar otra ecuación
if st.button("Nueva ecuación"):
    for key in ["a", "b", "x", "c", "intento"]:
        st.session_state.pop(key, None)
    st.experimental_rerun()
