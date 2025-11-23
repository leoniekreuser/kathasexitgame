from raetsel.raetsel_utils import display_raetsel, display_hints, display_solution_box
import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_1,
    SOLUTION_1,
    HINT_1_1,
    HINT_1_2,
    HINT_1_3,
    HINT_1_4,
)

if "page" not in st.session_state:
    st.session_state.page = "1"

display_raetsel(1, RAETSEL_1)
display_hints([HINT_1_1, HINT_1_2, HINT_1_3, HINT_1_4])
display_solution_box(SOLUTION_1)
