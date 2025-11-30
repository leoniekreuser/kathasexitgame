from raetsel.raetsel_prompts import (
    JULLI_PROMPT,
    JULLI_HINT_1,
    JULLI_HINT_2,
    JULLI_HINT_3,
    JULLI_HINT_4,
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
    st.session_state.page = "3.1"

with st.sidebar:
    if st.button("Zurück in der Hörsaal H15"):
        st.switch_page(APP_DIR / "pages" / "raetsel3.py")
    display_hints(
        ["julli hint 1", "julli hint 2", "julli hint 3", "julli hint 4"],
        horizontal=False,
    )
    st.write("Jullis Zahl: ")
    display_solution_box(32, key="3_julli")


JULLI_LLM = get_llm()

display_chatbot(
    header="Julli",
    name="julli",
    avatar="./data/julli_avatar.png",
    system_prompt=JULLI_PROMPT,
    llm=JULLI_LLM,
)
