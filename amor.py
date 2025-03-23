import streamlit as st
import time

st.set_page_config(page_title="Para Marily ❤️", page_icon="🌸")

st.title("🌹 Para la niña más especial del mundo 🌹")

st.write("Hola mi amor, este pequeño mensaje es para recordarte cuánto te amo y lo feliz que soy contigo. 💕")

if st.button("💖 Presiona aquí para saber cuánto te amo 💖"):
    with st.spinner("Cargando mi amor por ti... 😍"):
        time.sleep(2)

    st.success("Te amo más de lo que las palabras pueden expresar, Marily. 💕")
    st.balloons()
    st.write("Cada momento a tu lado es un regalo que valoro infinitamente. 🎁✨")
    st.write("Nunca dudes de lo importante que eres para mí. 🌸🥰")

st.markdown(
    """
    ---
    🌟 **Con todo mi amor, para ti, mi princesa.** 🌟  
    """,
    unsafe_allow_html=True
)
