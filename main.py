import streamlit as st
import random
import time

with st.sidebar:
    st.title("Sidebar Title")
    st.write("This is the sidebar content.")
st.header("Hello, Streamlit! 🚀")

selection_user = st.selectbox("Choose an option:", ["Schere ✂️", "Stein 🪨", "Papier 📄"])
selection_computer = random.choice(["Schere ✂️", "Stein 🪨", "Papier 📄"])

st.write(f"You selected: {selection_user}")
#st.write(f"Computer selected: {selection_computer}")
#who wins? 
time.sleep(3)
if selection_user == selection_computer:
    st.write("It's a tie!")
elif (selection_user == "Schere ✂️" and selection_computer == "Papier 📄") or \
     (selection_user == "Stein 🪨" and selection_computer == "Schere ✂️") or \
     (selection_user == "Papier 📄" and selection_computer == "Stein 🪨"):
    st.write("You win!")
else:
    st.write("Computer wins!")


st.write("Was für ein tolles Spiel!")