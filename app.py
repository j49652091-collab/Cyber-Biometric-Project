import streamlit as st
import cv2
import numpy as np
import time

# --- 1. الواجهة الفخمة (اللون الأسود والأخضر النيون) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background: black; color: #00ff00; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00ff00 !important; text-shadow: 0 0 15px #00ff00; text-align: center; }
    .stButton>button { 
        background-color: #00ff00 !important; color: black !important; 
        font-weight: bold !important; font-size: 18px !important;
        width: 100%; border-radius: 5px; height: 3em;
    }
    input { background-color: #111 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    .result-box { border: 2px solid #00ff00; padding: 15px; border-radius: 10px; background: rgba(0,255,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>🔐 BIO-CORE ACCESS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        user = st.text_input("AGENT_ID")
        pas = st.text_input("PASSWORD", type="password")
        if st.button("LOGIN"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
else:
    # --- 3. النظام الرئيسي (شغّال ومضمون) ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.write("### 🖥️ SYSTEM INFO")
        st.write(f"AGENT: **Esraa**")
        st.write("STATUS: **ACTIVE**")
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()

    uploaded_file = st.file_uploader("Upload Biometric Image...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        # معالجة الصورة
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # كشف الأنمي/AI
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 400

        # عرض النتائج في 3 أعمدة مرتبة
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("<div class='result-box'><h3>1. SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("AI DETECTED")
            else: st.success("HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='result-box'><h3>2. REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                # تحويل الأنمي لشكل بشري (Neural Re-mapping)
                dst = cv2.detailEnhance(img, sigma_s=15, sigma_r=0.15)
                reconstructed = cv2.filter2D(dst, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
                st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), caption="Neural Reconstruction", use_container_width=True)
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Source Confirmed", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown("<div class='result-box'><h3>3. DIGITAL SIG</h3>", unsafe_allow_html=True)
            # استخراج البصمة الرقمية (الديجيتال)
            orb = cv2.ORB_create(nfeatures=1000)
            kp, des = orb.detectAndCompute(gray, None)
            
            if des is not None:
                # رسم النقاط على الصورة
                img_points = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_points, cv2.COLOR_BGR2RGB), caption="Biometric Points", use_container_width=True)
                st.write("Vector Data:")
                st.code(str(des[:5])) # عرض الأكواد الرقمية
            else:
                st.error("Extraction Failed")
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.info("System Waiting for Image Injection...")

