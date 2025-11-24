import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent

# from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1, RAETSEL_2, SOLUTION_2

load_dotenv()


def display_raetsel(raetsel_id: int, raetsel_text: str):
    st.header(f"Rätsel {raetsel_id}")
    st.divider()
    st.write(raetsel_text)
    st.divider()


def display_hints(hints: list[str]):
    anzahl_hints = len(hints)
    if anzahl_hints == 0:
        return
    st.subheader("Hinweise")
    # as many streamlit cols as anzahl_hints:
    hint_cols = st.columns(anzahl_hints)
    for idx, hint in enumerate(hints, start=1):
        with hint_cols[idx - 1]:
            with st.expander(f"💡 Hinweis {idx}"):
                with st.expander(f"Wirklich anzeigen?"):
                    st.write(hint)
    st.divider()


def display_solution_box(solution: str, key: str):
    if f"solved_{key}" not in st.session_state:
        st.session_state["solved_" + key] = False
    elif st.session_state["solved_" + key]:
        st.success("Rätsel bereits gelöst! ✅ Lösung: " + str(solution))
        return True
    user_input = st.text_input("Deine Antwort:", key=key)
    if st.button("Antwort überprüfen", key=f"check_{key}"):
        if str(user_input).strip().lower() == str(solution).strip().lower():
            st.success("Richtige Antwort! 🎉")
            st.session_state["solved_" + key] = True
            return True
        else:
            st.error("Falsche Antwort. Versuche es noch einmal.")
            return False


def get_llm():
    llm = AzureChatOpenAI(
        azure_deployment=os.environ.get("LLM_DEPLOYMENT_NAME"),
        model="gpt-4.1",
        temperature=1,
    )
    return llm


def display_chatbot(
    header: str, name: str, system_prompt: str, avatar: str, llm: AzureChatOpenAI
):
    st.header(header)

    if f"{name}_messages" not in st.session_state:
        st.session_state[f"{name}_messages"] = [SystemMessage(content=system_prompt)]

    for msg in st.session_state[f"{name}_messages"]:
        if isinstance(msg, AIMessage):
            st.chat_message(name, avatar=avatar).write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("Katha", avatar="🤓").write(msg.content)

    lui_prompt = st.chat_input(f"Sprich mit {header} und finde ihre Zahl heraus!")
    if lui_prompt:
        with st.chat_message("Katha", avatar="🤓"):
            st.write(lui_prompt)
            st.session_state[f"{name}_messages"].append(
                HumanMessage(content=lui_prompt)
            )

        with st.chat_message(name, avatar=avatar):
            placeholder = st.empty()
            full_answer = ""

            for chunk in llm.stream(st.session_state[f"{name}_messages"]):
                delta = chunk.content or ""
                full_answer += delta
                placeholder.markdown(full_answer + "▌")

            st.session_state[f"{name}_messages"].append(AIMessage(content=full_answer))


def page_config():
    st.set_page_config(page_title="EXIT Uni Regensburg", page_icon="♥️", layout="wide")


def configure_sidebar():
    with st.sidebar:
        if st.session_state.page != "0":
            if st.button("Zurück zur Startseite"):
                st.switch_page(APP_DIR / "main.py")
