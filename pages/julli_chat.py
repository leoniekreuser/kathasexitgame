from raetsel.raetsel_prompts import JULLI_PROMPT
from raetsel.raetsel_utils import configure_sidebar, display_chatbot, get_llm
import streamlit as st
from main import APP_DIR

if "page" not in st.session_state:
    st.session_state.page = "3"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")


JULLI_LLM = get_llm()

display_chatbot(
    header="Julli",
    name="julli",
    avatar="💃",
    system_prompt=JULLI_PROMPT,
    llm=JULLI_LLM,
)
