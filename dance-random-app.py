import streamlit as st
import random
import time
import requests
import re

# --- 1. 페이지 설정 (브라우저 탭 이름도 변경) ---
st.set_page_config(page_title="Random Dance Finder by Yuju", layout="centered")

# --- 2. 화려한 디자인 (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Noto+Sans+KR:wght@700&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #1a0a2a 0%, #050505 100%);
        color: #00f2ea;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Yuju의 네온 타이틀 스타일 */
    .neon-title {
        text-align: center;
        font-size: 3.2rem;
        color: #fff;
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de, 0 0 40px #ff00de;
        padding-top: 20px;
        line-height: 1.2;
    }

    .sub-text {
        text-align: center;
        font-size: 1rem;
        color: #00f2ea;
        letter-spacing: 3px;
        margin-bottom: 30px;
        opacity: 0.8;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background: transparent;
        color: #00f2ea;
        border: 2px solid #00f2ea;
        font-size: 1.5rem;
        font-weight: bold;
        height: 70px;
        width: 100%;
        border-radius: 0px;
        transition: 0.3s;
        box-shadow: 0 0 10px #00f2ea;
    }
    div.stButton > button:hover {
        background: #00f2ea;
        color: #000;
        box-shadow: 0 0 50px #00f2ea;
    }

    .video-frame {
        border: 5px solid #ff00de;
        padding: 5px;
        box-shadow: 0 0 30px #ff00de;
        background: #000;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. UI 구성 (새로운 제목 적용) ---
st.markdown('<h1 class="neon-title">RANDOM DANCE<br>FINDER</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">PRODUCED BY YUJU</p>', unsafe_allow_html=True)

# --- 4. 영상 추출 로직 ---
def fetch_target_video():
    queries = ["dance challenge shorts", "kpop shorts dance", "틱톡 챌린지", "인스타 릴스 댄스"]
    q = random.choice(queries).replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={q}"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        v_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        return random.choice(list(set(v_ids))) if v_ids else "GQuE_V3_0O4"
    except:
        return "GQuE_V3_0O4"

# --- 5. 가동 버튼 ---
if st.button("S C A N  N O W"):
    with st.spinner('YUJU SYSTEM IS SCANNING...'):
        time.sleep(1.2)
        st.session_state.v_id = fetch_target_video()
    st.balloons()

# --- 6. 결과 출력 ---
if 'v_id' in st.session_state:
    st.markdown('<div class="video-frame">', unsafe_allow_html=True)
    st.video(f"https://www.youtube.com/watch?v={st.session_state.v_id}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write(f"✨ SCAN COMPLETED BY YUJU SYSTEM")