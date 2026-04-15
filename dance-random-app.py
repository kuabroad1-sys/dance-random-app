import streamlit as st
import random
import requests
import re

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Yuju's Random Dance Finder", layout="centered")

# --- 2. 디자인 고도화 (귀여운 폰트 및 스타일 추가) ---
st.markdown("""
    <style>
    /* 구글 폰트에서 귀엽고 둥근 폰트와 힙한 폰트 불러오기 */
    @import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@700&family=Orbitron:wght@900&family=Black+Han+Sans&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #1a0a2a 0%, #050505 100%);
        color: #00f2ea;
    }
    
    /* 메인 타이틀 */
    .neon-title {
        text-align: center;
        font-size: 3.5rem;
        color: #fff;
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de;
        padding-top: 20px;
        font-family: 'Orbitron', sans-serif;
        line-height: 1.1;
    }

    /* Yuju's Random Dance Finder (귀여운 폰트 적용) */
    .yuju-brand {
        text-align: center;
        font-size: 1.5rem;
        color: #ffb7ff;
        font-family: 'Gaegu', cursive; /* 귀여운 손글씨 느낌 */
        margin-bottom: 30px;
        text-shadow: 0 0 5px #ff00de;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background: transparent;
        color: #00f2ea;
        border: 2px solid #00f2ea;
        font-size: 2.2rem;
        font-family: 'Black Han Sans', sans-serif;
        height: 85px;
        width: 100%;
        border-radius: 20px; /* 약간 둥글게 변경 */
        transition: 0.3s;
        box-shadow: 0 0 15px #00f2ea;
    }
    div.stButton > button:hover {
        background: #00f2ea;
        color: #000;
        box-shadow: 0 0 50px #00f2ea;
        transform: scale(1.02);
    }

    .video-frame {
        border: 8px solid #ff00de;
        padding: 5px;
        border-radius: 1