from main import APP_DIR
from raetsel.raetsel_prompts import (
    LUI_PROMPT,
    LUI_HINT_1,
    LUI_HINT_2,
    LUI_HINT_3,
    LUI_HINT_4,
)
from raetsel.raetsel_utils import display_chatbot, display_hints, get_llm
import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "3.4"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")
    st.divider()
    display_hints([LUI_HINT_1, LUI_HINT_2, LUI_HINT_3, LUI_HINT_4], horizontal=False)

LUI_LLM = get_llm()

display_chatbot(
    header="Lui",
    name="lui",
    avatar="./data/lui_avatar.png",
    system_prompt=LUI_PROMPT,
    llm=LUI_LLM,
)
