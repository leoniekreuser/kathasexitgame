from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from main import APP_DIR
from raetsel.raetsel_prompts import LUI_PROMPT
from raetsel.raetsel_utils import display_chatbot, get_llm
import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "3.4"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")

LUI_LLM = get_llm()

display_chatbot(
    header="Lui",
    name="lui",
    avatar="👩‍🏫",
    llm=LUI_LLM,
)
