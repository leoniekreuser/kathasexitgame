import streamlit as st

# from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1, RAETSEL_2, SOLUTION_2


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


def display_solution_box(solution: str):
    user_input = st.text_input("Deine Antwort:")
    if st.button("Antwort überprüfen"):
        if str(user_input).strip().lower() == str(solution).strip().lower():
            st.success("Richtige Antwort! 🎉")
            return True
        else:
            st.error("Falsche Antwort. Versuche es noch einmal.")
            return False
