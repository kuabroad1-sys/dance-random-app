import streamlit as st
import random
import time
import requests
import re

# --- 1. 페이지 설정 (세로형 쇼츠 최적화) ---
st.set_page_config(page_title="DANCE TARGET SCANNER", layout="centered")

# --- 2. 로컬 실행용 초강력 네온 디자인 (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Orbitron:wght@900&display=swap');

    /* 전체 배경 */
    .stApp {
        background: radial-gradient(circle at center, #1a0a2a 0%, #050505 100%);
        color: #00f2ea;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* 네온 타이틀 */
    .neon-title {
        text-align: center;
        font-size: 3.5rem;
        color: #fff;
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de, 0 0 40px #ff00de;
        padding-top: 20px;
        font-family: 'Orbitron', sans-serif;
    }

    /* 스캔 라인 애니메이션 */
    .scanner {
        width: 100%;
        height: 2px;
        background-color: #00f2ea;
        box-shadow: 0 0 15px #00f2ea;
        position: relative;
        animation: scan 3s infinite linear;
    }
    @keyframes scan {
        0% { top: 0px; }
        50% { top: 300px; }
        100% { top: 0px; }
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background: transparent;
        color: #00f2ea;
        border: 2px solid #00f2ea;
        font-size: 1.8rem;
        font-weight: bold;
        height: 80px;
        width: 100%;
        border-radius: 0px;
        transition: 0.3s;
        box-shadow: 0 0 10px #00f2ea;
        margin-top: 20px;
    }
    div.stButton > button:hover {
        background: #00f2ea;
        color: #000;
        box-shadow: 0 0 50px #00f2ea;
    }

    /* 영상 컨테이너 (쇼츠 비율) */
    .video-frame {
        border: 5px solid #ff00de;
        padding: 5px;
        box-shadow: 0 0 30px #ff00de;
        background: #000;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. UI 구성 ---
st.markdown('<h1 class="neon-title">SCANNING...</h1>', unsafe_allow_html=True)
st.markdown('<div class="scanner"></div>', unsafe_allow_html=True)

# --- 4. 영상 랜덤 추출 함수 ---
def fetch_target_video():
    queries = ["dance challenge shorts", "kpop shorts dance", "틱톡 챌린지"]
    q = random.choice(queries).replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={q}"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        # 비디오 ID 패턴 매칭
        v_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        return random.choice(list(set(v_ids))) if v_ids else "jOTfBlKSQYY"
    except:
        return "jOTfBlKSQYY" # 오류 시 기본값

# --- 5. 실행 버튼 ---
if st.button("T A R G E T  L O C K"):
    with st.spinner('TARGETING GLOBAL DATA...'):
        time.sleep(1.5)
        st.session_state.v_id = fetch_target_video()
    st.balloons()

# --- 6. 영상 출력 ---
if 'v_id' in st.session_state:
    st.markdown('<div class="video-frame">', unsafe_allow_html=True)
    # 유튜브 영상 임베딩
    st.video(f"https://www.youtube.com/watch?v={st.session_state.v_id}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write(f"🔍 DETECTED ID: {st.session_state.v_id}")