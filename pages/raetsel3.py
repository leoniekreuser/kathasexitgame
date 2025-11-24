import streamlit as st
from main import APP_DIR
from raetsel.raetsel_texts import RAETSEL_3
from raetsel.raetsel_utils import (
    configure_sidebar,
    display_raetsel,
    display_solution_box,
    page_config,
)

st.session_state.page = "3"

page_config()
display_raetsel(3, RAETSEL_3)
configure_sidebar()

cols = st.columns(5)
for i, bot in enumerate(["lauri", "lisi", "julli", "lui", "leo"]):
    with cols[i]:
        if st.button(f"Sprich mit {bot.capitalize()}"):
            st.session_state.page = f"{bot}_chat"
            st.switch_page(APP_DIR / "pages" / f"{bot}_chat.py")

st.divider()

st.write("Lauris Zahl: ")
display_solution_box(155, key="3_lauri_solution")
st.write("Lisis Zahl: ")
display_solution_box(3953.80, key="3_lisi_solution")
st.write("Jullis Zahl: ")
display_solution_box(32, key="3_julli_solution")
st.write("Luis Zahl: ")
display_solution_box(405, key="3_lui_solution")
