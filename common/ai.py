import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

from .constants import ROLE

@st.cache_resource
def get_client():
    load_dotenv()
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_msg_of_ai(
    user_input:str, model_name:str="openai/gpt-oss-20b") -> str:
        
        messages = [
            {
            "role": history['role'].name,
            "content": history['msg']
        }for history in st.session_state.history
        ]
        
        messages.append({
            "role": ROLE.user.name,
            "content": user_input
        })            
        
        client = get_client()
        response = client.chat.completions.create(
            messages=messages,
            model=model_name
        )
        
        return response.choices[0].message.content