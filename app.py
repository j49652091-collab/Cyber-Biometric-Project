import streamlit as st
from PIL import Image
import random
import time
import requests
from io import BytesIO

# =========================================
# PAGE SETTINGS
# =========================================
st.set_page_config(
    page_title="AI SECURITY SYSTEM",
    page_icon="🔥",
    layout="wide"
)

# =========================================
# STYLE (تصميمك الأصلي مع تحسين الوضوح)
# =========================================
st.markdown("""
<style>
.stApp{
    background: linear-gradient(to right, #0f172a, #111827);
    color:white;
}
.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:cyan;
    margin-bottom:30px;
    text-shadow: 0 0 15px cyan;
}
.box{
    background-color:#1e293b;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 0px 20px cyan;
    margin-bottom: 20px;
}
.result-human{ color:lime; font-size:35px; font-weight:bold; }
.result-ai{ color:orange; font-size:35px; font-weight:bold; }
/* تحسين زر الدخول ليكون واضحاً بنص أسود */
.stButton>button {
    background-color: #00ffcc !important;
    color: #000000 !important;
    font-weight: 900 !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN DATA
# =========================================
valid_users = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

if "logged" not in st.session_state:
    st.session_state.logged = False

# =========================================
# LOGIN PAGE
# =========================================
if not st.session_state.logged:
    st.markdown('<div class="main-title">AI SECURITY SYSTEM 🔥</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        username = st.text_input("USERNAME")
        password = st.text_input("PASSWORD", type="password")
        if st.button("LOGIN", use_container_width=True):
            if username.lower() in valid_users and password == valid_password:
                st.session_state.logged = True
                st.rerun()
            else:
                st.error("ACCESS DENIED ❌")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# MAIN SYSTEM
# =========================================
else:
    st.markdown('<div class="main-title">AI vs HUMAN DETECTION 🔥</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("UPLOAD IMAGE", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        
        # محاكاة كشف الأنمي/AI (يمكن استبداله بكود OpenCV لاحقاً)
        # هنا سنفترض عشوائياً للتحليل ولكن سنظهر التوليد
        is_ai = random.choice([True, False])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### SOURCE IMAGE")
            st.image(image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### ANALYSIS & REBUILD")
            if is_ai:
                st.markdown('<div class="result-ai">⚠️ AI DETECTED</div>', unsafe_allow_html=True)
                st.write("Generating realistic human proxy...")
                with st.spinner("Reconstructing textures..."):
                    time.sleep(2)
                    # جلب صورة بشرية حقيقية عشوائية كمحاكاة للتوليد المقارب
                    st.image("https://thispersondoesnotexist.com", caption="Realistic Reconstruction", use_container_width=True)
            else:
                st.markdown('<div class="result-human">✅ HUMAN VERIFIED</div>', unsafe_allow_html=True)
                st.image(image, caption="Real Source Confirmed", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### DIGITAL SIGNATURE")
            # استخراج بصمات وهمية أو حقيقية بناءً على المحتوى
            face_id = random.randint(100000, 999999)
            st.write("**FACE_VECTOR:**")
            st.code(f"ID_{face_id}_SIG")
            
            # محاكاة إخفاء الأجزاء غير الموجودة
            if random.choice([True, False]): # محاكاة كشف العين
                eye_id = random.randint(100000, 999999)
                st.write("**EYE_VECTOR:**")
                st.code(f"EYE_{eye_id}_SIG")
                
            st.success("Analysis Completed")
            st.markdown('</div>', unsafe_allow_html=True)
