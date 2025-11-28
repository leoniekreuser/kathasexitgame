from raetsel.raetsel_utils import (
    APP_DIR,
    configure_sidebar,
    display_raetsel,
    display_hints,
    display_solution_box,
    page_config,
)
import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_1,
    SOLUTION_1,
    HINT_1_1,
    HINT_1_2,
    HINT_1_3,
    HINT_1_4,
    SOLVED_1_TEXT,
)

st.session_state.page = "1"
page_config()
configure_sidebar()


display_raetsel(
    raetsel_id=1,
    raetsel_header="Gefangen in der Uni Regensburg",
    raetsel_text=RAETSEL_1,
)
col1, col2 = st.columns([4.5, 5.5])
with col1:
    st.image("./data/raetsel_1_kugel.png", use_container_width=True)
with col2:
    st.image("./data/raetsel_1_notiz.png", use_container_width=True)
display_hints([HINT_1_1, HINT_1_2, HINT_1_3, HINT_1_4])
display_solution_box(SOLUTION_1, key="1")

if st.session_state.get("solved_1"):
    st.balloons()
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("./data/raetsel_1_schluessel.png", use_container_width=True)
    with col2:
        st.write(SOLVED_1_TEXT)
        if st.button("Zur Wiwi Bib gehen"):
            st.switch_page(APP_DIR / "pages" / "raetsel2.py")
