import streamlit as st

st.set_page_config(page_title="Juego de Villanas Disney", page_icon="👑", layout="centered")

st.title("👑 Juego de Villanas de Disney")
st.subheader("¿Cuánto sabes sobre las más icónicas villanas?")

questions = [
    {
        "question": "¿Cuál es el nombre de la villana en 'La Sirenita'?",
        "options": ["Maléfica", "Úrsula", "Cruella de Vil", "Madre Gothel"],
        "answer": "Úrsula"
    },
    {
        "question": "¿Qué villana quiere la piel de 101 dálmatas?",
        "options": ["Cruella de Vil", "Yzma", "Madame Medusa", "Lady Tremaine"],
        "answer": "Cruella de Vil"
    },
    {
        "question": "¿Quién es la malvada madrastra de Blancanieves?",
        "options": ["La Reina Malvada", "Úrsula", "Maléfica", "Gothel"],
        "answer": "La Reina Malvada"
    },
    {
        "question": "¿Qué villana lanza una maldición en 'La Bella Durmiente'?",
        "options": ["Cruella de Vil", "Madre Gothel", "Maléfica", "Yzma"],
        "answer": "Maléfica"
    },
    {
        "question": "¿Cómo se llama la villana de 'Enredados'?",
        "options": ["Gothel", "Maléfica", "Cruella de Vil", "La Reina de Corazones"],
        "answer": "Gothel"
    }
]

score = 0

with st.form("quiz_form"):
    for idx, q in enumerate(questions):
        user_answer = st.radio(f"{idx+1}. {q['question']}", q["options"], key=idx)
        if user_answer == q["answer"]:
            score += 1

    submitted = st.form_submit_button("Enviar respuestas")

if submitted:
    st.write(f"Tu puntuación es: **{score} / {len(questions)}**")

    if score == len(questions):
        st.success("¡Felicidades! ¡Acertaste todas las preguntas! 🎉")
        st.balloons()
        st.markdown("""
        <style>
        @keyframes pizzaRain {
            0% { transform: translateY(-100px) rotate(0deg); opacity: 0; }
            100% { transform: translateY(800px) rotate(360deg); opacity: 1; }
        }
        .pizza {
            position: fixed;
            top: 0;
            font-size: 40px;
            animation: pizzaRain 3s linear infinite;
        }
        </style>
        <div class="pizza">🍕</div>
        <div class="pizza" style="left: 20%;">🍕</div>
        <div class="pizza" style="left: 40%;">🍕</div>
        <div class="pizza" style="left: 60%;">🍕</div>
        <div class="pizza" style="left: 80%;">🍕</div>
        """, unsafe_allow_html=True)
