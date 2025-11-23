import streamlit as st
from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1

if "page" not in st.session_state:
    st.session_state.page = "1"

st.header("Rätsel 1")

st.write(RAETSEL_1)

user_input = st.text_input("Gib hier deine Lösung ein:")


if st.button("Lösung überprüfen"):
    try:
        if int(user_input) == SOLUTION_1:
            st.success("Richtige Lösung! 🎉")
        else:
            st.error("Falsche Lösung. Versuche es noch einmal.")
    except ValueError:
        st.error("Bitte gib eine gültige Zahl ein.")
