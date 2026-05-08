
import streamlit as st
import cv2
import numpy as np
import time
from datetime import datetime

# --- 1. واجهة النخبة (The Ultimate Cyber UI) ---
st.set_page_config(page_title="NEURAL-X MASTER", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { 
        background: radial-gradient(circle, #051a05 0%, #000000 100%) !important; 
        color: #00ff00 !important; font-family: 'Courier New', monospace; 
    }
    .glitch-title {
        color: #00ff00; font-size: 70px; font-weight: 900; text-align: center;
        text-shadow: 0 0 30px #00ff00; letter-spacing: 15px; margin-top: -30px;
    }
    .cyber-frame {
        border: 2px solid #00ff00; padding: 20px; background: rgba(0, 255, 0, 0.05);
        border-radius: 15px; box-shadow: 0 0 25px rgba(0,255,0,0.4); text-align: center;
    }
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 22px !important;
        border-radius: 5px; border: 2px solid #fff; box-shadow: 0 0 30px #00ff00;
    }
    .stButton>button:hover { transform: scale(1.05); background: #000 !important; color: #fff !important; }
    input { background-color: #000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. شاشة الدخول (نار وشرار) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    col_left, col_main, col_right = st.columns([1, 2, 1])
    
    with col_left:
        st.markdown("<h1 style='text-align:center;'>📡</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:red; text-align:center;'>[ SCANNING... ]</p>", unsafe_allow_html=True)
        st.image("https://giphy.com")
        st.markdown("<p style='font-size:10px; opacity:0.6; text-align:center;'>SIGNAL_STRENGTH: 99%<br>LOCATION: AMMAN_NODE</p>", unsafe_allow_html=True)

    with col_main:
        st.markdown("<p style='text-align: center; font-size: 100px; margin-top: 20px;'>🛡️</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='glitch-title'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
        user = st.text_input("AGENT_ID (Esraa/Weam/Tasneem)")
        pas = st.text_input("SEC_KEY (PASSCODE)", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.session_state['user'] = user
                with st.spinner("BYPASSING FIREWALLS..."): time.sleep(2)
                st.rerun()
            else: st.error("ACCESS DENIED!")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("<h1 style='text-align:center;'>💻</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:cyan; text-align:center;'>[ ATTACK_READY ]</p>", unsafe_allow_html=True)
        st.image("https://giphy.com")
        st.markdown("<p style='font-size:10px; opacity:0.6; text-align:center;'>ENCRYPTION: AES-512<br>STATUS: ACTIVE</p>", unsafe_allow_html=True)

else:
    # --- 3. القائمة الجانبية الذكية ---
    with st.sidebar:
        st.markdown(f"### 🖥️ COMMAND CENTER\n**AGENT:** {st.session_state['user']}\n**TIME:** {datetime.now().strftime('%H:%M:%S')}")
        st.markdown("<hr style='border-color:#00ff00'>", unsafe_allow_html=True)
        st.write("● CPU: 24%\n● NETWORK: SECURE\n● TRACE: Amman_Node_01")
        if st.button("TERMINATE SESSION"):
            st.session_state['auth'] = False
            st.rerun()

    # --- 4. النظام الرئيسي (إعادة البناء المقاربة) ---
    st.markdown("<h1 class='glitch-title'>🧬 NEURAL ANALYZER</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        is_ai = sat_mean > 115 or sat_mean < 40 # كشف الأنمي بناءً على حدة الألوان

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
                with st.spinner("AI GENERATING REALISTIC MATCH..."):
                    time.sleep(2)
                    # هنا نعرض صورة بشرية حقيقية "توليدية" مطابقة للمواصفات العامة
                    st.image("https://thispersondoesnotexist.com", caption="RECONSTRUCTED HUMAN PROXY", use_container_width=True)
                st.info("System: Neural Proxy generated for AI source.")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="REAL SOURCE SECURE", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-frame'><h3>🔑 DIGITAL SIG</h3>", unsafe_allow_html=True)
            if st.button("GET VECTOR"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"POINTS: {len(kp)}")
                if des is not None: st.code(str(des[:10]))
            st.markdown("</div>", unsafe_allow_html=True)
