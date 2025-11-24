from raetsel.raetsel_prompts import LISI_PROMPT
from raetsel.raetsel_utils import configure_sidebar, display_chatbot, get_llm
import streamlit as st
from main import APP_DIR

if "page" not in st.session_state:
    st.session_state.page = "3.3"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")


LISI_LLM = get_llm()

display_chatbot(
    header="Lisi",
    name="lisi",
    avatar="⛷️",
    system_prompt=LISI_PROMPT,
    llm=LISI_LLM,
)
