import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_4,
    SOLUTION_4,
    HINT_4_1,
    HINT_4_2,
    HINT_4_3,
    HINT_4_4,
)
from raetsel.raetsel_utils import (
    configure_sidebar,
    display_raetsel,
    display_hints,
    display_solution_box,
    page_config,
)

st.session_state.page = "4"


page_config()
configure_sidebar()
display_raetsel(raetsel_id=4, raetsel_header="Im Audimax", raetsel_text=RAETSEL_4)
st.image("./data/raetsel_4_gedicht.png", width=800)
st.image("./data/raetsel_4_stundenplan.png")
st.divider()
display_hints([HINT_4_1, HINT_4_2, HINT_4_3, HINT_4_4])
display_solution_box(SOLUTION_4, key="4")
