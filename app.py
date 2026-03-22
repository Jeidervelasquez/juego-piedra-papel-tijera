import streamlit as st
import random

# Configuración básica de la página (Valor extra: Interfaz mejorada)
st.set_page_config(page_title="Piedra, Papel o Tijera", page_icon="🎮", layout="centered")

# Estilos y título
st.title("🎮 Piedra, Papel o Tijera")
st.write("¡Desafía a la computadora y demuestra quién manda!")

# Inicializar el sistema de puntajes en el session_state (Valor extra: Funcionalidad adicional)
if 'puntaje_usuario' not in st.session_state:
    st.session_state.puntaje_usuario = 0
if 'puntaje_pc' not in st.session_state:
    st.session_state.puntaje_pc = 0

opciones = ["Piedra 🪨", "Papel 📄", "Tijera ✂️"]

st.write("---")
st.subheader("Selecciona tu jugada:")

# Crear columnas para los botones de elección (Valor extra: Mejor distribución UI)
col1, col2, col3 = st.columns(3)

eleccion_usuario = None

if col1.button("Piedra 🪨", use_container_width=True):
    eleccion_usuario = "Piedra 🪨"
if col2.button("Papel 📄", use_container_width=True):
    eleccion_usuario = "Papel 📄"
if col3.button("Tijera ✂️", use_container_width=True):
    eleccion_usuario = "Tijera ✂️"

# Lógica del juego al hacer clic
if eleccion_usuario:
    eleccion_pc = random.choice(opciones)
    
    st.write("---")
    st.write(f"🧑 **Tú elegiste:** {eleccion_usuario}")
    st.write(f"🤖 **La computadora eligió:** {eleccion_pc}")
    
    # Determinar ganador
    if eleccion_usuario == eleccion_pc:
        st.info("¡Es un Empate! 🤝")
    elif (eleccion_usuario == "Piedra 🪨" and eleccion_pc == "Tijera ✂️") or \
         (eleccion_usuario == "Papel 📄" and eleccion_pc == "Piedra 🪨") or \
         (eleccion_usuario == "Tijera ✂️" and eleccion_pc == "Papel 📄"):
        st.success("¡Ganaste esta ronda! 🎉")
        st.session_state.puntaje_usuario += 1
    else:
        st.error("La computadora gana esta ronda. 💀")
        st.session_state.puntaje_pc += 1

# Mostrar el marcador actualizado
st.write("---")
st.subheader("🏆 Marcador Global")
col_score1, col_score2 = st.columns(2)
col_score1.metric(label="Tu Puntaje", value=st.session_state.puntaje_usuario)
col_score2.metric(label="Puntaje Computadora", value=st.session_state.puntaje_pc)

# Botón para reiniciar el juego
if st.button("Reiniciar Marcador", type="secondary"):
    st.session_state.puntaje_usuario = 0
    st.session_state.puntaje_pc = 0
    st.rerun()