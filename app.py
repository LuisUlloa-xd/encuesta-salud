
import streamlit as st

st.set_page_config(page_title="Encuesta de Salud Escolar", page_icon="🩺", layout="centered")

st.title("🩺 Encuesta de Salud Escolar")
st.write("Responde las siguientes preguntas con **Sí** o **No** para obtener un diagnóstico y recomendaciones.")

preguntas = [
    "¿Tienes fiebre?",
    "¿Sientes dolor de cabeza frecuente?",
    "¿Tienes tos persistente?",
    "¿Tienes dificultad para respirar?",
    "¿Sientes dolor muscular o articular?",
    "¿Te sientes muy cansado o fatigado?",
    "¿Has perdido el apetito?",
    "¿Tienes dolor de garganta?",
    "¿Tienes congestión nasal?",
    "¿Tienes dolor abdominal?",
    "¿Has tenido diarrea recientemente?",
    "¿Has tenido vómitos?",
    "¿Has notado erupciones en la piel?",
    "¿Tienes dolor en los oídos?",
    "¿Tienes visión borrosa?",
    "¿Tienes mareos frecuentes?",
    "¿Has perdido peso sin razón aparente?",
    "¿Has tenido dificultad para dormir?",
    "¿Tienes sangrado nasal frecuente?",
    "¿Tienes hinchazón en alguna parte del cuerpo?",
    "¿Sientes palpitaciones o dolor en el pecho?",
    "¿Has tenido desmayos?",
    "¿Sufres de ansiedad o estrés excesivo?"
]

respuestas = []
for pregunta in preguntas:
    respuesta = st.radio(pregunta, ["No", "Sí"], horizontal=True)
    respuestas.append(respuesta)

if st.button("📋 Obtener diagnóstico"):
    si_count = respuestas.count("Sí")
    
    if si_count == 0:
        diagnostico = "No presentas síntomas relevantes. Sigue cuidando tu salud con buena alimentación y ejercicio."
        recomendacion = "Mantén una dieta equilibrada, duerme bien y realiza actividad física diaria."
    elif si_count <= 5:
        diagnostico = "Presentas síntomas leves."
        recomendacion = "Bebe suficiente agua, descansa y vigila si los síntomas empeoran."
    elif si_count <= 10:
        diagnostico = "Tienes varios síntomas, podrías estar cursando una enfermedad común como gripe o resfriado."
        recomendacion = "Acude a un centro de salud para un chequeo y evita automedicarte."
    elif si_count <= 15:
        diagnostico = "Tus síntomas indican una posible enfermedad moderada."
        recomendacion = "Busca atención médica lo antes posible."
    else:
        diagnostico = "Los síntomas son graves. Es urgente acudir a un centro de salud inmediatamente."
        recomendacion = "No retrases la consulta médica y sigue las indicaciones de un profesional."
    
    st.subheader("🩺 Diagnóstico")
    st.write(diagnostico)
    st.subheader("💡 Recomendación")
    st.write(recomendacion)
