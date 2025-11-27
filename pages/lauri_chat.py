from raetsel.raetsel_prompts import LAURI_PROMPT
from raetsel.raetsel_utils import display_chatbot, get_llm
import streamlit as st
from main import APP_DIR

if "page" not in st.session_state:
    st.session_state.page = "3.2"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")

LAURI_LLM = get_llm()

display_chatbot(
    header="Lauri",
    name="lauri",
    avatar="🏃‍➡️",
    system_prompt=LAURI_PROMPT,
    llm=LAURI_LLM,
)
