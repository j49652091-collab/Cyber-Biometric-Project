import streamlit as st
import cv2
import numpy as np
import time
from datetime import datetime

# =========================================
# 1. واجهة النخبة (Ultra-Premium Cyber UI)
# =========================================
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp, [data-testid="stSidebar"] { 
        background: radial-gradient(circle, #051a05 0%, #000000 100%) !important; 
        color: #00ff00 !important; font-family: 'Courier New', monospace; 
    }
    .glitch-header {
        color: #00ff00; font-size: 70px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 15px; margin-top: -40px;
    }
    .cyber-card {
        border: 2px solid #00ff00; padding: 25px; background: rgba(0, 255, 0, 0.05);
        border-radius: 15px; box-shadow: 0 0 35px rgba(0,255,0,0.4); text-align: center;
    }
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 22px !important;
        border-radius: 5px; border: 2px solid #fff; box-shadow: 0 0 35px rgba(0,255,0,0.8);
        transition: 0.4s; height: 3.5em; width: 100%; text-transform: uppercase;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 60px #00ff00; color: #fff !important; background: #000 !important; }
    input { background-color: rgba(0, 0, 0, 0.9) !important; color: #00ff00 !important; border: 2px solid #00ff00 !important; text-align: center; font-size: 20px !important; }
    .info-panel { border: 1px solid #00ff00; padding: 12px; background: rgba(0, 255, 0, 0.02); font-size: 11px; text-align: left; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# =========================================
# 2. نظام الدخول (نار وشرار)
# =========================================
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    col_l, col_m, col_r = st.columns([1, 1.5, 1])
    with col_l:
        st.markdown("<br><br><h1 style='text-align:center; font-size:120px;'>📡</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:red; text-align:center; font-weight:bold; font-size:20px;'>[ SCANNING_AIRWAVES ]</p>", unsafe_allow_html=True)
        st.markdown("<div class='info-panel'><b>ID:</b> SEC_NODE_01<br><b>FREQ:</b> 5.8 GHz<br><b>SIGNAL:</b> ■■■■■■■□□ 92%<br><b>DECRYPTOR:</b> ACTIVE</div>", unsafe_allow_html=True)

    with col_m:
        st.markdown("<p style='text-align: center; font-size: 100px; margin-top: 20px;'>🛡️</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='glitch-header'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
        user = st.text_input("AGENT_ID")
        pas = st.text_input("SEC_KEY", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if user.lower() in ["esraa", "wiam", "tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.session_state['user'] = user
                st.rerun()
            else: st.error("ACCESS DENIED: INTRUSION DETECTED!")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_r:
        st.markdown("<br><br><h1 style='text-align:center; font-size:120px;'>💻</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:cyan; text-align:center; font-weight:bold; font-size:20px;'>[ ATTACK_MODE_READY ]</p>", unsafe_allow_html=True)
        st.markdown("<div class='info-panel'><b>PAYLOAD:</b> ACTIVE<br><b>PROXY:</b> ENABLED<br><b>THREADS:</b> 256<br><b>SEC_BYPASS:</b> TRUE</div>", unsafe_allow_html=True)

# =========================================
# 3. النظام الرئيسي (التحليل الخارق)
# =========================================
else:
    with st.sidebar:
        st.markdown(f"### 🖥️ COMMAND CENTER\n**AGENT:** {st.session_state['user']}\n**STATUS:** ONLINE")
        st.markdown(f"**DATE:** {datetime.now().strftime('%d/%m/%Y')}\n**NODE:** Jordan_Safe_Link")
        if st.button("TERMINATE SESSION"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown("<h1 class='glitch-header'>🧬 NEURAL ANALYZER</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        # قراءة ومعالجة الصورة
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # خوارزمية كشف حقيقية (تحليل التباين واللون)
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        is_ai = variance < 400 or sat_mean > 110 # كشف الأنمي بناءً على نعومة الحواف وقوة الألوان

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='cyber-frame'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI_ANIME DETECTED")
            else: st.success("✅ HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='cyber-frame'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("AI RECONSTRUCTING HUMAN PROXY..."):
                    time.sleep(2)
                    # ذكاء اصطناعي: إذا كانت الحواف ناعمة جداً -> فتاة، وإلا -> شاب
                    if variance ", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-frame'><h3>🔑 SIGNATURE</h3>", unsafe_allow_html=True)
            if st.button("GET VECTOR"):
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                if des is not None:
                    st.success(f"PTS: {len(kp)} MAPPED")
                    st.code(str(des[:8]))
            st.markdown("</div>", unsafe_allow_html=True)
