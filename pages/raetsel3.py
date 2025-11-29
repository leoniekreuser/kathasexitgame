import streamlit as st
from main import APP_DIR
from raetsel.raetsel_texts import RAETSEL_3, SOLVED_3_TEXT
from raetsel.raetsel_utils import (
    configure_sidebar,
    display_raetsel,
    display_solution_box,
    page_config,
)

st.session_state.page = "3"

page_config()
configure_sidebar()

display_raetsel(raetsel_id=3, raetsel_header="Im H15", raetsel_text=RAETSEL_3)
col1, col2 = st.columns([8, 2])
with col1:
    st.image("./data/raetsel_3_computer.png")
with col2:
    for i, bot in enumerate(["lauri", "lisi", "julli", "lui", "leo"]):
        if st.button(f"Sprich mit {bot.capitalize()}"):
            st.session_state.page = f"{bot}_chat"
            st.switch_page(APP_DIR / "pages" / f"{bot}_chat.py")


st.divider()
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write("Lauris Zahl: ")
    display_solution_box(155, key="3_lauri")
with col2:
    st.write("Lisis Zahl: ")
    display_solution_box(5844.80, key="3_lisi")
with col3:
    st.write("Jullis Zahl: ")
    display_solution_box(32, key="3_julli")
with col4:
    st.write("Luis Zahl: ")
    display_solution_box(486, key="3_lui")
with col5:
    st.write("Leos Zahl: ")
    display_solution_box(5140, key="3_leo")

all_solved = all(
    [
        st.session_state.get("solved_3_lauri")
        and st.session_state.get("solved_3_lisi")
        and st.session_state.get("solved_3_julli")
        and st.session_state.get("solved_3_lui")
        and st.session_state.get("solved_3_leo")
    ]
)

if all_solved:
    st.success("Alle Zahlen gesammelt! Das Rätsel ist gelöst! 🎉")
    st.balloons()
    st.session_state["solved_3"] = True

    col1, col2 = st.columns([8, 2])
    with col1:
        st.image("./data/raetsel_3_audimax.png", width="stretch")

    # st.write(SOLVED_3_TEXT)
    if st.button("Zum Audimax gehen"):
        st.switch_page(APP_DIR / "pages" / "raetsel4.py")
