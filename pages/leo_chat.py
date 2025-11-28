from raetsel.raetsel_prompts import (
    LEO_PROMPT,
    LISI_HINT_1,
    LISI_HINT_2,
    LISI_HINT_3,
    LISI_HINT_4,
)
from raetsel.raetsel_utils import display_chatbot, get_llm, display_hints
import streamlit as st
from main import APP_DIR

if "page" not in st.session_state:
    st.session_state.page = "3.3"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")
    st.divider()
    display_hints(
        [LISI_HINT_1, LISI_HINT_2, LISI_HINT_3, LISI_HINT_4], horizontal=False
    )


LEO_LLM = get_llm()

display_chatbot(
    header="Leo",
    name="leo",
    avatar="⛷️",
    system_prompt=LEO_PROMPT,
    llm=LEO_LLM,
)
