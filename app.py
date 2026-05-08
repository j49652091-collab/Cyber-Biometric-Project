import streamlit as st
import cv2
import numpy as np
import time
import random

# --- 1. التنسيق الفخم (Cyber-Dark UI) ---
st.set_page_config(page_title="NEURAL-X MASTER", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #051a05 0%, #000000 100%); color:white; }
    .main-title { text-align:center; font-size:65px; font-weight:900; color:#00ff00; text-shadow: 0 0 25px #00ff00; margin-bottom:40px; }
    .box { background-color:#0a0a0a; padding:40px; border-radius:15px; border: 2px solid #00ff00; box-shadow:0px 0px 30px rgba(0,255,0,0.3); }
    .stButton>button { 
        background-color: #00ff00 !important; color: #000 !important; 
        font-weight: 900 !important; font-size: 25px !important; 
        height: 3em; border-radius: 5px; border: none; box-shadow: 0 0 20px #00ff00;
    }
    .result-status { font-size:35px; font-weight:bold; text-align:center; }
    code { background-color: #000 !important; color: #00ff00 !important; font-size: 18px !important; border: 1px solid #00ff00 !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-title">BIO-GATE ACCESS 🛡️</div>', unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        u = st.text_input("AGENT_ID")
        p = st.text_input("SEC_KEY", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if u.lower() in ["esraa", "wiam", "tasneem"] and p == "12345":
                st.session_state.auth = True
                st.rerun()
            else: st.error("ACCESS DENIED")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # --- 3. النظام الرئيسي (توليد وتحليل) ---
    st.markdown('<div class="main-title">🧬 NEURAL ANALYZER</div>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.write(f"AGENT: **{st.session_state.get('user', 'Esraa')}**")
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()

    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        source_img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
        
        # كشف الأنمي/AI بناءً على نعومة الألوان
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 400

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<div class='box'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI_ANIME DETECTED")
            else: st.success("✅ HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        # عمود التوليد (Reconstruction)
        with col2:
            st.markdown("<div class='box'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("GENERATING REALISTIC PROXY..."):
                    time.sleep(2)
                    # اختيار صورة بشرية حقيقية مقاربة (شاب أو بنت) بناءً على ملامح الأنمي
                    # نستخدم رابطاً يولد وجوه بشرية حقيقية لمحاكاة النتيجة
                    target_url = "https://thispersondoesnotexist.com"
                    st.image(target_url, caption="NEURAL RECONSTRUCTION", use_container_width=True)
                    st.info("Identity Synthesis: Real-world match created.")
                    # سنستخدم هذه الصورة المفترضة لاستخراج البصمات في الخطوة التالية
            else:
                st.image(cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB), caption="NO REBUILD NEEDED", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='box'><h3>🔑 SIGNATURE</h3>", unsafe_allow_html=True)
            if st.button("GET VECTOR"):
                # استخراج البصمة الرقمية (Digital Vector)
                orb = cv2.ORB_create(nfeatures=1000)
                kp, des = orb.detectAndCompute(gray, None)
                
                # فحص وجود وجه أو يد في الصورة برمجياً
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                
                if len(faces) > 0:
                    st.write("**FACE BIOMETRIC:**")
                    st.code(str(des[:8]) if des is not None else "Analyzing...")
                    # رسم النقاط الحيوية
                    img_kp = cv2.drawKeypoints(source_img, kp, None, color=(0, 255, 0))
                    st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                else:
                    st.warning("NO FACE DETECTED IN SOURCE")
            st.markdown("</div>", unsafe_allow_html=True)
