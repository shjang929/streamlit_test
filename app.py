import streamlit as st

from common.show import show_msg
from common.constants import ROLE
from common.history import init_history
from common.ai import get_msg_of_ai

st.title("ChatBot Service")

init_history()
    
user_input =st.chat_input("메시지 입력해주세요.")
if user_input:
    #사용자
    show_msg(**{
        "role": ROLE.user,
        "msg": user_input
    })
# 컴퓨터 글 프린트
# wwith st.chat_messsage("assistant"):
#   st.markdown("코딩이 그렇게 좋아?")
    show_msg(**{
        "role": ROLE.assistant,
        "msg": get_msg_of_ai(user_input)
    })