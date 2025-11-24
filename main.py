import os
from pathlib import Path
import streamlit as st
import random
import time

from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1
from raetsel.raetsel_utils import configure_sidebar

APP_DIR = Path(__file__).resolve().parent

st.session_state.page = "0"


st.set_page_config(page_title="EXIT UR", page_icon="♥️", layout="wide")
configure_sidebar()

st.header("Hallo Katha!")

st.write("Willkommen zu deinem Exit Game! 🎉")

st.write("Löse die Rätsel, um den Weg nach Hause zu finden. Viel Erfolg! 🍀")

for raetsel in ["1", "2", "3"]:
    if st.session_state.get(f"solved_solution_{raetsel}"):
        button_text = f"{raetsel} . Rätsel gelöst ✅"
    else:
        button_text = f"Zum {raetsel}. Rätsel"
    if st.button(button_text):
        st.session_state.page = raetsel
        st.switch_page(APP_DIR / "pages" / f"raetsel{raetsel}.py")
