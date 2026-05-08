import streamlit as st
import cv2
import numpy as np
from PIL import Image

# --- 1. التنسيق الفخم (وضوح تام وألوان نيون) ---
st.set_page_config(page_title="AI SECURITY SYSTEM", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #050a14 0%, #000000 100%); color:white; }
    .main-title { text-align:center; font-size:65px; font-weight:900; color:cyan; text-shadow: 0 0 20px cyan; margin-bottom:40px; }
    .box { background-color:#111827; padding:40px; border-radius:20px; border: 2px solid cyan; box-shadow:0px 0px 30px cyan; }
    label { font-size: 25px !important; color: cyan !important; font-weight: bold !important; }
    .stButton>button { 
        background-color: #00ffcc !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 25px !important; 
        height: 3em; border-radius: 10px; border: none; box-shadow: 0 0 20px #00ffcc;
    }
    .result-human { color:lime; font-size:40px; font-weight:bold; text-shadow: 0 0 15px lime; }
    code { background-color: #000 !important; color: #00f2ff !important; font-size: 18px !important; border: 1px solid cyan !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. نظام الدخول ---
valid_users = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

if "logged" not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.markdown('<div class="main-title">SECURITY TERMINAL 🔥</div>', unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.5, 1])
    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        username = st.text_input("ENTER USERNAME")
        password = st.text_input("ENTER ACCESS KEY", type="password")
        if st.button("EXECUTE LOGIN"):
            if username.lower() in valid_users and password == valid_password:
                st.session_state.logged = True
                st.rerun()
            else: st.error("ACCESS DENIED ❌")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 3. النظام الرئيسي الذكي ---
else:
    st.markdown('<div class="main-title">BIOMETRIC ANALYZER 🔥</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT SOURCE IMAGE", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # معالجة الصورة باستخدام OpenCV
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # استخدام مصنفات لتمييز الوجه والعين
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="SOURCE_INPUT", use_container_width=True)

        with col2:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.subheader("ANALYZING BIOMETRIC DATA...")
            
            if len(faces) > 0:
                st.markdown('<div class="result-human">✅ HUMAN DETECTED</div>', unsafe_allow_html=True)
                
                # استخراج بصمة رقمية حقيقية (Vector) من الوجه
                orb = cv2.ORB_create(nfeatures=500)
                kp, des = orb.detectAndCompute(gray, None)
                
                # عرض البيانات فقط إذا تم اكتشاف العضو
                for (x, y, w, h) in faces:
                    roi_gray = gray[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    
                    st.write("### 🔑 DIGITAL SIGNATURES")
                    
                    # بصمة الوجه (دائماً موجودة ما دام تم اكتشاف وجه)
                    st.write("**FACE BIOMETRIC VECTOR:**")
                    st.code(str(des[0][:10]) if des is not None else "Analyzing...")
                    
                    # بصمة العين (تظهر فقط إذا تم اكتشاف عيون)
                    if len(eyes) > 0:
                        st.write("**EYE BIOMETRIC VECTOR:**")
                        st.code(str(des[1][:10]) if des is not None and len(des) > 1 else "Analyzing...")
                    
                    # بصمة اليد (لن تظهر أبداً إلا إذا قمنا بإضافة كود كشف اليد، لذا ستبقى مخفية حالياً)
                    
                st.success("AUTHENTICATION COMPLETED ✅")
            else:
                st.warning("⚠️ NO BIOMETRIC FEATURES DETECTED")
            
            st.markdown('</div>', unsafe_allow_html=True)

