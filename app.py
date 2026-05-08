import streamlit as st
from PIL import Image
import random

# --- 1. إعدادات الصفحة والجماليات (نصوص كبيرة وواضحة) ---
st.set_page_config(page_title="AI SECURITY SYSTEM", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(to right, #050a14, #000000); color:white; }
    
    /* تكبير عنوان الصفحة */
    .main-title { text-align:center; font-size:65px; font-weight:900; color:cyan; text-shadow: 0 0 20px cyan; margin-bottom:40px; }
    
    /* تحسين الصندوق وتكبير الخطوط داخله */
    .box { background-color:#111827; padding:40px; border-radius:20px; border: 2px solid cyan; box-shadow:0px 0px 30px cyan; }
    label { font-size: 25px !important; color: cyan !important; font-weight: bold !important; }
    
    /* زر الدخول: نص أسود واضح جداً خلفية فسفورية */
    .stButton>button { 
        background-color: #00ffcc !important; 
        color: #000000 !important; 
        font-weight: 900 !important; 
        font-size: 25px !important; 
        height: 3em; border-radius: 10px; border: none;
        box-shadow: 0 0 20px #00ffcc;
    }
    
    .result-human { color:lime; font-size:40px; font-weight:bold; text-shadow: 0 0 15px lime; }
    .result-ai { color:orange; font-size:40px; font-weight:bold; text-shadow: 0 0 15px orange; }
    
    /* وضوح الأكواد الرقمية */
    code { background-color: #000 !important; color: #00f2ff !important; font-size: 20px !important; border: 1px solid cyan !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. بيانات الدخول ---
valid_users = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

if "logged" not in st.session_state:
    st.session_state.logged = False

# --- 3. صفحة الدخول (تعديل الوضوح) ---
if not st.session_state.logged:
    st.markdown('<div class="main-title">SECURITY TERMINAL 🔥</div>', unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        # تكبير نصوص الإدخال
        username = st.text_input("ENTER USERNAME")
        password = st.text_input("ENTER ACCESS KEY", type="password")
        st.write("")
        if st.button("EXECUTE LOGIN"):
            if username.lower() in valid_users and password == valid_password:
                st.session_state.logged = True
                st.rerun()
            else:
                st.error("ACCESS DENIED ❌")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 4. النظام الرئيسي (بعد الدخول) ---
else:
    st.markdown('<div class="main-title">BIOMETRIC ANALYZER 🔥</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT SOURCE IMAGE", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption="SOURCE_INPUT", use_container_width=True)

        with col2:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.subheader("ANALYZING DATA...")
            
            # محاكاة الكشف
            result = "HUMAN" if random.random() > 0.5 else "AI"

            if result == "HUMAN":
                st.markdown('<div class="result-human">✅ HUMAN VERIFIED</div>', unsafe_allow_html=True)
                st.write("")
                # عرض البصمات كأرقام تعريفية (IDs) كما في صورتك
                st.code(f"FACE_ID : {random.randint(100000, 999999)}")
                st.code(f"EYE_ID  : {random.randint(100000, 999999)}")
                st.code(f"HAND_ID : {random.randint(100000, 999999)}")
                st.success("DIGITAL SIGNATURE VERIFIED ✅")
                
                st.write("### BIOMETRIC STATUS")
                st.progress(98)
                st.write("● Face Scan: COMPLETED")
                st.write("● Eye Scan: COMPLETED")
                st.write("● Hand Scan: COMPLETED")
            else:
                st.markdown('<div class="result-ai">⚠️ AI DETECTED</div>', unsafe_allow_html=True)
                st.warning("SYNTHETIC DATA FOUND")
                st.progress(40)
                st.code(f"TRACE_ID: {random.randint(100000, 999999)}")
            
            st.markdown('</div>', unsafe_allow_html=True)
