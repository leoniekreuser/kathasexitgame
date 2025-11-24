import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_2,
    SOLUTION_2,
    HINT_2_1,
    HINT_2_2,
    HINT_2_3,
    HINT_2_4,
)
from raetsel.raetsel_utils import (
    configure_sidebar,
    display_raetsel,
    display_hints,
    display_solution_box,
    page_config,
)

st.session_state.page = "2"


page_config()
configure_sidebar()
display_raetsel(2, RAETSEL_2)
display_hints([HINT_2_1, HINT_2_2, HINT_2_3, HINT_2_4])
display_solution_box(SOLUTION_2, key="solution_2")
