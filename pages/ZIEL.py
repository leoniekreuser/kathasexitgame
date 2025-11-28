import streamlit as st

from raetsel.raetsel_utils import configure_sidebar

st.session_state.page = "4"

st.session_state["first_time_complete"] = False

st.set_page_config(page_title="EXIT UR", page_icon="♥️", layout="wide")
configure_sidebar()

st.header("Geschafft! 🎉")
st.divider()
st.snow()


col1, col2 = st.columns([2, 8])
with col1:
    st.image("./data/wir_alle.jpeg", width="stretch")
    st.image("./data/wir_alle_2.jpeg", width="stretch")
with col2:
    st.write("""TBD: Gratulieren + Ende der Story""")
