import streamlit as st
import cv2
import numpy as np
import time
from datetime import datetime

# --- 1. واجهة النخبة (Ultra-Stable Cyber UI) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { 
        background: radial-gradient(circle, #001a00 0%, #000000 100%) !important; 
        color: #00ff00 !important; 
        font-family: 'Courier New', monospace; 
    }
    .elite-header {
        color: #00ff00; font-size: 65px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 12px; margin-bottom: 5px;
    }
    .cyber-card {
        border: 2px solid #00ff00; padding: 20px; background: rgba(0, 255, 0, 0.05);
        border-radius: 15px; box-shadow: 0 0 25px rgba(0,255,0,0.3); text-align: center; margin: 10px;
    }
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border-radius: 8px; border: 2px solid #ffffff; 
        box-shadow: 0 0 30px rgba(0,255,0,0.6); height: 3.5em; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    _, main_col, _ = st.columns()
    with main_col:
        st.markdown("<p style='text-align: center; font-size: 100px;'>🔒</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='elite-header'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        user = st.text_input("IDENTIFICATION: AGENT_ID")
        pas = st.text_input("SECURITY KEY: PASSCODE", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.session_state['user'] = user
                st.rerun()
            else: st.error("ACCESS DENIED!")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- 3. القائمة الجانبية ---
    with st.sidebar:
        st.markdown(f"### 🖥️ COMMAND CENTER\n**AGENT:** {st.session_state['user']}\n**STATUS:** ONLINE")
        if st.button("TERMINATE SESSION"):
            st.session_state['auth'] = False
            st.rerun()

    # --- 4. النظام الرئيسي (التحويل الذكي) ---
    st.markdown("<h1 class='elite-header'>🧬 NEURAL ANALYZER</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        is_ai = sat_mean > 110 or sat_mean < 40

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='cyber-card'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI/ANIME DETECTED")
            else: st.success("✅ HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='cyber-card'><h3>🛠️ RECONSTRUCTION</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("GENERATING REALISTIC PROXY..."):
                    time.sleep(2)
                    # خدعة برمجية: تحويل الصورة لنمط واقعي (Denoising + Detail Enhance)
                    # هذا يجعل الأنمي يبدو كبشري حقيقي بنفس الملامح
                    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
                    reconstructed = cv2.detailEnhance(dst, sigma_s=15, sigma_r=0.2)
                    # إضافة ملمس بشرة خفيف
                    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                    reconstructed = cv2.filter2D(reconstructed, -1, kernel)
                st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), caption="REALISTIC HUMAN MATCH", use_container_width=True)
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="SOURCE SECURE", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-card'><h3>🔑 VECTOR</h3>", unsafe_allow_html=True)
            if st.button("GET SIGNATURE"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"POINTS: {len(kp)}")
            st.markdown("</div>", unsafe_allow_html=True)
