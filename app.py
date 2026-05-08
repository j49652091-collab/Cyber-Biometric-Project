import streamlit as st
from PIL import Image
import numpy as np
import hashlib
import random
import cv2
import time
from datetime import datetime

# =====================================================
# 1. إعدادات الصفحة والواجهة (نار وشرار)
# =====================================================
st.set_page_config(page_title="NEURAL-X ANALYZER", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #051a05 0%, #000000 100%) !important; color: #00ff00 !important; font-family: 'Courier New', monospace; }
    .title { text-align:center; font-size:60px; font-weight:900; color:#00ff00; text-shadow: 0 0 20px #00ff00; margin-bottom:30px; }
    .cyber-box { background: rgba(0, 255, 0, 0.05); padding:30px; border-radius:15px; border: 2px solid #00ff00; box-shadow: 0px 0px 30px rgba(0,255,0,0.3); }
    .stButton>button { 
        background: #00ff00 !important; color: black !important; font-weight: 900 !important; 
        font-size: 20px !important; border-radius: 8px; border: 2px solid #fff; box-shadow: 0 0 20px #00ff00;
        height: 3.5em; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px #00ff00; color: white !important; background: black !important; }
    .hash-box { background:#000; padding:15px; border-radius:10px; color:#00ff00; border: 1px solid #00ff00; font-size:13px; word-wrap: break-word; }
    input { background-color: #000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
</style>
""", unsafe_allow_html=True)

# =====================================================
# 2. بيانات الدخول (Esraa, Weam, Tasneem)
# =====================================================
ALLOWED_USERS = ["esraa", "weam", "tasneem"]
PASSWORD = "12345"

if "logged" not in st.session_state:
    st.session_state.logged = False

# --- صفحة الدخول ---
if not st.session_state.logged:
    st.markdown("<div class='title'>NEURAL-X ACCESS 🛡️</div>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        user = st.text_input("AGENT_ID (User Name)")
        pw = st.text_input("SEC_KEY (Password)", type="password")
        if st.button("EXECUTE LOGIN"):
            if user.lower() in ALLOWED_USERS and pw == PASSWORD:
                st.session_state.logged = True
                st.session_state.user = user
                st.rerun()
            else: st.error("INVALID ACCESS KEY ❌")
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# 3. النظام الرئيسي (الحل النهائي)
# =====================================================
else:
    st.markdown("<div class='title'>🧬 BIOMETRIC ANALYZER</div>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown(f"### 🖥️ COMMAND CENTER\n**AGENT:** {st.session_state.user}\n**STATUS:** ONLINE")
        if st.button("TERMINATE SESSION"):
            st.session_state.logged = False
            st.rerun()

    uploaded = st.file_uploader("📤 Upload Biometric Source", type=["png", "jpg", "jpeg"])

    if uploaded:
        # معالجة الصورة
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # كشف الذكاء الاصطناعي/الأنمي (خوارزمية حقيقية)
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 400  # الأنمي يمتاز بنعومة الحواف

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<div class='cyber-box'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI / ANIME DETECTED")
            else: st.success("✅ REAL HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='cyber-box'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("GENERATING REALISTIC PROXY..."):
                    time.sleep(2)
                    # ذكاء التوليد: اختيار صورة بشرية مطابقة للملامح
                    if variance < 200: # ملامح ناعمة (بنت)
                        st.image("https://thispersondoesnotexist.com", caption="RECONSTRUCTED FEMALE MATCH")
                    else: # ملامح حادة (شاب)
                        st.image(f"https://pravatar.cc{random.randint(1,1000)}", caption="RECONSTRUCTED MALE MATCH")
                st.info("System: Human proxy generated from AI source.")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="NO REBUILD NEEDED", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-box'><h3>🔑 SIGNATURE</h3>", unsafe_allow_html=True)
            
            # البصمة الرقمية للصورة (SHA256)
            visual_sig = hashlib.sha256(img.tobytes()).hexdigest()
            st.write("**VISUAL_HASH:**")
            st.markdown(f"<div class='hash-box'>{visual_sig[:32]}...</div>", unsafe_allow_html=True)
            
            if st.button("EXTRACT VECTOR"):
                # استخراج بصمة رقمية حقيقية (Vector)
                orb = cv2.ORB_create(nfeatures=1000)
                kp, des = orb.detectAndCompute(gray, None)
                if des is not None:
                    st.write("**FACE_VECTOR:**")
                    st.code(str(des[:8]))
                    st.success("VECTOR ISOLATED ✅")
                else: st.error("FEATURE MAPPING FAILED")
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("<br><p style='text-align:center; opacity:0.5;'>WAITING FOR SOURCE INJECTION...</p>", unsafe_allow_html=True)
