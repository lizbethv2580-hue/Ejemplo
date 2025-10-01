import streamlit as st

st.set_page_config(page_title="Quiz de Villanas Disney", layout="centered")

# Título
st.title("👑 Quiz de Villanas Disney")
st.subheader("¿Puedes acertar las 5 preguntas? ¡Si lo haces, te lloverán pizzas! 🍕")

# Preguntas y respuestas correctas
preguntas = {
    "¿Cuál es el nombre de la villana en '101 dálmatas'?": "Cruella de Vil",
    "¿Quién envenena a Blancanieves?": "La Reina Malvada",
    "¿Qué villana se transforma en dragón en 'La Bella Durmiente'?": "Maléfica",
    "¿Cuál es la villana en 'La Sirenita'?": "Úrsula",
    "¿Quién encierra a Rapunzel en una torre?": "Madre Gothel"
}

respuestas_usuario = {}
correctas = 0

with st.form("quiz_form"):
    for pregunta, respuesta_correcta in preguntas.items():
        respuesta = st.text_input(pregunta)
        respuestas_usuario[pregunta] = respuesta

    enviado = st.form_submit_button("Enviar respuestas")

# Validación
if enviado:
    for pregunta, respuesta_correcta in preguntas.items():
        if respuestas_usuario[pregunta].strip().lower() == respuesta_correcta.lower():
            correctas += 1

    st.write(f"✅ Respuestas correctas: **{correctas} / 5**")

    if correctas == 5:
        st.success("🎉 ¡Perfecto! ¡Te mereces una lluvia de pizzas! 🍕")
        st.image("pizza_rain.gif", caption="¡Felicidades!", use_column_width=True)
    else:
        st.warning("😢 No acertaste todas... ¡Intenta de nuevo!")
