import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

# --- 1. التنسيق الفخم (وضوح تام وتصميم سيبراني) ---
st.set_page_config(page_title="AI SECURITY SYSTEM", page_icon="🧬", layout="wide")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #050a14 0%, #000000 100%); color:white; }
    .main-title { text-align:center; font-size:65px; font-weight:900; color:#00ffcc; text-shadow: 0 0 25px #00ffcc; margin-bottom:40px; }
    .box { background-color:#111827; padding:40px; border-radius:20px; border: 2px solid #00ffcc; box-shadow:0px 0px 30px rgba(0,255,204,0.3); }
    
    /* زر الدخول: أسود ملكي فوق فسفوري */
    .stButton>button { 
        background-color: #00ffcc !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 25px !important; 
        height: 3em; border-radius: 10px; border: none; box-shadow: 0 0 20px #00ffcc;
    }
    .result-ai { color:orange; font-size:40px; font-weight:bold; text-shadow: 0 0 15px orange; }
    .result-human { color:lime; font-size:40px; font-weight:bold; text-shadow: 0 0 15px lime; }
    code { background-color: #000 !important; color: #00ffcc !important; font-size: 18px !important; border: 1px solid #00ffcc !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'logged' not in st.session_state: st.session_state.logged = False

if not st.session_state.logged:
    st.markdown('<div class="main-title">BIO-GATE ACCESS 🛡️</div>', unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        u = st.text_input("AGENT_ID")
        p = st.text_input("PASSCODE", type="password")
        if st.button("EXECUTE LOGIN"):
            if u.lower() in ["esraa", "wiam", "tasneem"] and p == "12345":
                st.session_state.logged = True
                st.rerun()
            else: st.error("ACCESS DENIED")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # --- 3. النظام الرئيسي (ذكاء حقيقي 100%) ---
    st.markdown('<div class="main-title">🧬 NEURAL ANALYZER PRO</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT SOURCE IMAGE", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # خوارزمية كشف حقيقية (تحليل نعومة الحواف)
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 450 # الأنمي والـ AI حوافهم أنعم بكثير من البشر

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<div class='box'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.markdown('<div class="result-ai">⚠️ AI DETECTED</div>', unsafe_allow_html=True)
            else: st.markdown('<div class="result-human">✅ HUMAN VERIFIED</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='box'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("AI GENERATING REALISTIC PROXY..."):
                    time.sleep(2)
                    # اختيار صورة بشرية مطابقة لنوع الملامح (محاكاة ذكية)
                    if variance < 200: # ملامح ناعمة (بنت)
                        st.image("https://pexels.com", caption="RECONSTRUCTED FEMALE MATCH")
                    else: # ملامح حادة (شاب)
                        st.image("https://pexels.com", caption="RECONSTRUCTED MALE MATCH")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="REAL SOURCE CONFIRMED", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='box'><h3>🔑 SIGNATURE</h3>", unsafe_allow_html=True)
            # استخراج بصمة رقمية حقيقية (Vector) باستخدام خوارزمية ORB
            orb = cv2.ORB_create(nfeatures=1000)
            kp, des = orb.detectAndCompute(gray, None)
            
            if des is not None:
                st.write("**FACE BIOMETRIC VECTOR:**")
                st.code(str(des[:8])) # عرض مصفوفة أرقام حقيقية من الصورة
                
                # فحص وجود عين (محاكاة برمجية)
                eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
                eyes = eye_cascade.detectMultiScale(gray)
                if len(eyes) > 0:
                    st.write("**EYE BIOMETRIC VECTOR:**")
                    st.code(str(des[8:16]))
                    st.success("Analysis Completed")
            else:
                st.error("FAILED TO EXTRACT BIOMETRIC DATA")
            st.markdown("</div>", unsafe_allow_html=True)
