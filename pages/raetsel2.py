import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_2,
    SOLUTION_2,
    HINT_2_1,
    HINT_2_2,
    HINT_2_3,
    HINT_2_4,
    SOLVED_2_TEXT,
)
from raetsel.raetsel_utils import (
    APP_DIR,
    configure_sidebar,
    display_raetsel,
    display_hints,
    display_solution_box,
    page_config,
)

st.session_state.page = "2"


page_config()
configure_sidebar()
display_raetsel(raetsel_id=2, raetsel_header="In der Wiwi Bib", raetsel_text=RAETSEL_2)
col1, col2 = st.columns([3.5, 6.5])
with col1:
    st.image("./data/raetsel_2_wiwibib.png", use_container_width=True)
with col2:
    st.image("./data/raetsel_2_buch.png", use_container_width=True)

display_hints([HINT_2_1, HINT_2_2, HINT_2_3, HINT_2_4])
display_solution_box(SOLUTION_2, key="2")

if st.session_state.get("solved_1"):
    st.balloons()
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("./data/raetsel_2_fenster.png", use_container_width=True)
    with col2:
        st.write(SOLVED_2_TEXT)
        if st.button("Zum H15 gehen"):
            st.switch_page(APP_DIR / "pages" / "raetsel3.py")
