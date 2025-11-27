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
display_raetsel(raetsel_id=3, raetsel_header="Im H15", raetsel_text=RAETSEL_3)
st.image("./data/raetsel_3_computer.png")
st.divider()
configure_sidebar()

cols = st.columns(5)
for i, bot in enumerate(["lauri", "lisi", "julli", "lui", "leo"]):
    with cols[i]:
        if st.button(f"Sprich mit {bot.capitalize()}"):
            st.session_state.page = f"{bot}_chat"
            st.switch_page(APP_DIR / "pages" / f"{bot}_chat.py")

st.divider()

st.write("Lauris Zahl: ")
display_solution_box(155, key="3_lauri")
st.write("Lisis Zahl: ")
display_solution_box(5844.80, key="3_lisi")
st.write("Jullis Zahl: ")
display_solution_box(32, key="3_julli")
st.write("Luis Zahl: ")
display_solution_box(405, key="3_lui")

if all(
    [
        st.session_state.get("solved_3_lauri")
        and st.session_state.get("solved_3_lisi")
        and st.session_state.get("solved_3_julli")
        and st.session_state.get("solved_3_lui")
    ]
):
    st.success("Alle Zahlen gesammelt! Das Rätsel ist gelöst! 🎉")
    st.session_state["solved_3"] = True
