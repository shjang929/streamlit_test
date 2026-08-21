import streamlit as st
from common.show import show_msg

def init_history() -> None:

    if "history" not in st.session_state:
        st.session_state.history = []
        
    for h in st.session_state.history:
        show_msg(**h, is_history=True)