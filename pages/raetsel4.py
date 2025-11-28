import streamlit as st
from raetsel.raetsel_texts import (
    RAETSEL_4,
    SOLUTION_4,
    HINT_4_1,
    HINT_4_2,
    HINT_4_3,
    HINT_4_4,
)
from raetsel.raetsel_utils import (
    APP_DIR,
    configure_sidebar,
    display_raetsel,
    display_hints,
    display_solution_box,
    page_config,
)

st.session_state.page = "4"


page_config()
configure_sidebar()
display_raetsel(raetsel_id=4, raetsel_header="Im Audimax", raetsel_text=RAETSEL_4)
col1, col2 = st.columns([5, 5])
with col1:
    st.image("./data/raetsel_4_gedicht.png", width="stretch")
with col2:
    st.image("./data/raetsel_4_stundenplan.png", width="stretch")

st.write(
    "Außerdem entdeckst Du auf der Seite des Sitzes einen seltsamen Bildschirm. Darauf kann eine 6-stellige Nummer eingegeben werden: "
)
st.image("./data/raetsel_4_bildschirm.png", width=600)
st.divider()
display_hints([HINT_4_1, HINT_4_2, HINT_4_3, HINT_4_4])
st.write("Gib die 6-stellige Nummer ein, um das Rätsel zu lösen:")
cols = st.columns(6)
for number in range(6):
    with cols[number]:
        st.session_state["raetsel_4_number_" + str(number)] = st.number_input(
            label="lbl",
            step=1,
            min_value=0,
            max_value=9,
            key=str(number),
            label_visibility="hidden",
        )

number_mapping = {"0": 8, "1": 9, "2": 7, "3": 3, "4": 1, "5": 5}

if st.button("Prüfen"):
    points = 0
    for i in range(6):
        if st.session_state["raetsel_4_number_" + str(i)] == number_mapping[str(i)]:
            points += 1
    if points == 6:
        st.success("Richtig! Das Rätsel ist gelöst! 🎉")
        st.session_state["solved_4"] = True
    else:
        st.error(f"Falsche Lösung. Du hast {6-points} Fehler. Versuche es noch einmal.")

if f"solved_4" not in st.session_state:
    st.session_state["solved_4"] = False
elif st.session_state["solved_4"]:
    st.success("Rätsel bereits gelöst! ✅ Lösung: " + str("897315"))

if not "first_time_complete" in st.session_state:
    st.session_state["first_time_complete"] = True

if st.session_state["solved_4"]:
    if st.session_state["first_time_complete"]:
        st.switch_page(APP_DIR / "pages" / "ZIEL.py")
    else:
        st.success("Du hast das Rätsel bereits gelöst!")
        if st.button("Zum Ziel gehen"):
            st.switch_page(APP_DIR / "pages" / "ZIEL.py")
        if st.button("Zurück zur Startseite"):
            st.switch_page(APP_DIR / "main.py")
