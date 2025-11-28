import os
from pathlib import Path
import streamlit as st
import random
import time

from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1
from raetsel.raetsel_utils import configure_sidebar
from cosmosdb import cosmosdb

st.markdown(
    """
    <style>
    /* Haupt-Container schmaler und mittig */
    .block-container {
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

APP_DIR = Path(__file__).resolve().parent

st.session_state.page = "0"


st.set_page_config(page_title="EXIT UR", page_icon="♥️", layout="wide")
configure_sidebar()

games = cosmosdb.get_all_games()

st.header("Hallo Katha!")

st.write("Willkommen zu deinem Exit Game! 🎉")
st.container(height=10, border=False)

if not "game_selected" in st.session_state or not st.session_state["game_selected"]:
    st.write("Wähle ein gespeichertes Spiel:")
    col1, col2, _ = st.columns([0.5, 2, 7.5])

    with col1:
        for game_id in games:
            if st.button(f"🗑️", key=f"delete_{game_id}"):
                cosmosdb.delete_game(game_id)
                st.rerun()
    with col2:
        for game_id in games:
            if st.button(game_id):
                st.session_state["game_selected"] = True
                st.session_state["game_id"] = game_id
                existing_state = cosmosdb.retrieve_session_state(game_id)
                if existing_state:
                    st.session_state.update(existing_state)
                st.rerun()
    st.container(height=20, border=False)
    st.write("Oder starte ein neues Spiel:")
    game_id = st.text_input(
        label="lbl",
        placeholder="Gib eine neue Spiel-ID ein:",
        label_visibility="hidden",
    )
    if st.button("Neues Spiel starten"):
        if game_id in games:
            st.error("Diese Spiel-ID existiert bereits. Bitte wähle eine andere.")
        else:
            st.session_state.game_selected = True
            st.session_state.game_id = game_id
            st.session_state.update(
                {
                    "page": "0",
                    "solved_1": False,
                    "solved_2": False,
                    "solved_3": False,
                    "solved_3_lauri": False,
                    "solved_3_lisi": False,
                    "solved_3_julli": False,
                    "solved_3_lui": False,
                    "solved_3_leo": False,
                    "locked_1": False,
                    "locked_2": True,
                    "locked_3": True,
                    "locked_4": True,
                    "solved_4": False,
                }
            )
            cosmosdb.save_session_state(game_id, st.session_state)
        st.rerun()

if "game_selected" in st.session_state and st.session_state["game_selected"]:
    with st.sidebar:
        if st.button("🚪Log Out"):
            st.session_state["game_selected"] = False
            st.rerun()
        if st.button("💾 Spiel speichern"):
            cosmosdb.save_session_state(st.session_state.game_id, st.session_state)
            st.success(f"Spielstand für {st.session_state.game_id} gespeichert! 💾")


if not "game_selected" in st.session_state or not st.session_state["game_selected"]:
    st.stop()

st.write("Löse die Rätsel, um den Weg nach Hause zu finden. Viel Erfolg! 🍀")

for raetsel in ["1", "2", "3", "4"]:
    if f"locked_{raetsel}" not in st.session_state:
        st.session_state[f"locked_{raetsel}"] = True
    if raetsel == "1":  # First raetsel is always unlocked
        st.session_state[f"locked_1"] = False
    if st.session_state.get(f"solved_{raetsel}"):
        button_text = f"{raetsel} . Rätsel gelöst ✅"
        st.session_state[f"locked_{int(raetsel) + 1}"] = False  # unlock riddle
    else:
        button_text = f"Zum {raetsel}. Rätsel"
    if st.button(button_text, disabled=st.session_state[f"locked_{raetsel}"]):
        st.session_state.page = raetsel
        st.switch_page(APP_DIR / "pages" / f"raetsel{raetsel}.py")
