from raetsel.raetsel_prompts import (
    LISI_PROMPT,
    LISI_HINT_1,
    LISI_HINT_2,
    LISI_HINT_3,
    LISI_HINT_4,
)
from raetsel.raetsel_utils import (
    display_chatbot,
    display_solution_box,
    get_llm,
    display_hints,
)
import streamlit as st
from main import APP_DIR

if "page" not in st.session_state:
    st.session_state.page = "3.3"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")
    display_hints(
        [LISI_HINT_1, LISI_HINT_2, LISI_HINT_3, LISI_HINT_4], horizontal=False
    )
    st.write("Lisis Zahl: ")
    display_solution_box(5844.80, key="3_lisi")


LISI_LLM = get_llm()

display_chatbot(
    header="Lisi",
    name="lisi",
    avatar="./data/lisi_avatar.png",
    system_prompt=LISI_PROMPT,
    llm=LISI_LLM,
)
