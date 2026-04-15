import streamlit as st
import random
import requests
import re

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="Yuju's Random Dance Finder", layout="centered")

# --- 2. 디자인 고도화 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@700&family=Orbitron:wght@900&family=Black+Han+Sans&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #1a0a2a 0%, #050505 100%);
        color: #00f2ea;
    }
    
    .neon-title {
        text-align: center;
        font-size: 3.5rem;
        color: #fff;
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de;
        padding-top: 20px;
        font-family: 'Orbitron', sans-serif;
        line-height: 1.1;
    }

    .yuju-brand {
        text-align: center;
        font-size: 1.5rem;
        color: #ffb7ff;
        font-family: 'Gaegu', cursive;
        margin-bottom: 30px;
        text-shadow: 0 0 5px #ff00de;
    }

    div.stButton > button {
        background: transparent;
        color: #00f2ea;
        border: 2px solid #00f2ea;
        font-size: 2.2rem;
        font-family: 'Black Han Sans', sans-serif;
        height: 85px;
        width: 100%;
        border-radius: 20px;
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
        border-radius: 15px;
        box-shadow: 0 0 30px #ff00de;
        background: #000;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. UI 구성 ---
st.markdown('<h1 class="neon-title">RANDOM DANCE<br>FINDER</h1>', unsafe_allow_html=True)
st.markdown('<p class="yuju-brand">✨ Yuju\'s Random Dance Finder ✨</p>', unsafe_allow_html=True)

# --- 4. 영상 추출 로직 ---
def fetch_target_video():
    queries = ["dance challenge shorts", "kpop shorts dance", "랜플댄 챌린지", "tiktok dance"]
    q = random.choice(queries).replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={q}"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        # 이 부분이 에러가 났던 지점입니다. 한 줄로 정확히 이어져야 합니다.
        v_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        if v_ids:
            return random.choice(list(set(v_ids)))
        else:
            return "GQuE_V3_0O4"
    except Exception:
        return "GQuE_V3_0O4"

# --- 5. 가동 버튼 ---
if st.button("🕺 랜플댄스 찾기! 💃"):
    st.session_state.v_id = fetch_target_video()
    st.balloons()

# --- 6. 결과 출력 ---
if 'v_id' in st.session_state:
    st.markdown('<div class="video-frame">', unsafe_allow_html=True)
    st.video(f"https://www.youtube.com/watch?v={st.session_state.v_id}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ffb7ff; font-family:\'Gaegu\'; font-size:1.5rem;">💖 유주가 찾아낸 오늘의 댄스 타겟! 💖</p>', unsafe_allow_html=True)