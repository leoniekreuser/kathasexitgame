import os
from pathlib import Path
import streamlit as st
import random
import time

from raetsel.raetsel_texts import RAETSEL_1, SOLUTION_1

APP_DIR = Path(__file__).resolve().parent

if "page" not in st.session_state:
    st.session_state.page = "Start"

st.header("Hallo Katha!")

st.write("Willkommen zu deinem Exit Game! 🎉")

st.write("Löse die Rätsel, um den Weg nach Hause zu finden. Viel Erfolg! 🍀")

for raetsel in ["1", "2"]:
    if st.button(f"Zum {raetsel}. Rätsel"):
        st.session_state.page = raetsel
        st.switch_page(APP_DIR / "pages" / f"raetsel{raetsel}.py")

# selection_user = st.selectbox("Choose an option:", ["Schere ✂️", "Stein 🪨", "Papier 📄"])
# selection_computer = random.choice(["Schere ✂️", "Stein 🪨", "Papier 📄"])

# st.write(f"You selected: {selection_user}")

# # who wins?
# time.sleep(3)
# st.write(f"Computer selected: {selection_computer}")
# if selection_user == selection_computer:
#     st.write("It's a tie!")
# elif (
#     (selection_user == "Schere ✂️" and selection_computer == "Papier 📄")
#     or (selection_user == "Stein 🪨" and selection_computer == "Schere ✂️")
#     or (selection_user == "Papier 📄" and selection_computer == "Stein 🪨")
# ):
#     st.write("You win!")
# else:
#     st.write("Computer wins!")


# st.write("Was für ein tolles Spiel!")
# st.write("Wenn das hier sichtbar ist, hat die CI/CD Pipeline funktioniert.")
