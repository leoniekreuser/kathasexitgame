import streamlit as st
from raetsel.raetsel_texts import RAETSEL_2, SOLUTION_2

if "page" not in st.session_state:
    st.session_state.page = "2"

st.header("Rätsel 2")

st.write(RAETSEL_2)

user_input = st.text_input("Gib hier deine Lösung ein:")


if st.button("Lösung überprüfen"):
    try:
        if user_input.lower() == SOLUTION_2:
            st.success("Richtige Lösung! 🎉")
        else:
            st.error("Falsche Lösung. Versuche es noch einmal.")
    except ValueError:
        st.error("Bitte gib eine gültige Zahl ein.")
