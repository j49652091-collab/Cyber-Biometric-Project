import streamlit as st
import cv2
import numpy as np
import time
import random

# --- 1. إعدادات الواجهة الاحترافية (Cyber-Tech UI) ---
st.set_page_config(page_title="NEURAL-X RECONSTRUCTION", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ff00; font-family: 'Courier New'; }
    h1, h2, h3 { color: #00ff00 !important; text-align: center; text-shadow: 0 0 20px #00ff00; }
    
    /* إصلاح الأزرار: نص أسود واضح */
    .stButton>button { 
        background-color: #00ff00 !important; 
        color: #000 !important; 
        font-weight: bold !important; 
        border-radius: 0px; border: 2px solid #00ff00;
    }
    .stButton>button:hover { background-color: #000 !important; color: #00ff00 !important; }
    
    .reportview-container .main { background: #000; }
    input { background-color: #000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>BIO-GATE ACCESS CONTROL</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("---")
        user = st.text_input("AGENT_ID (USER)")
        pas = st.text_input("ENCRYPTION_KEY", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                with st.spinner("BYPASSING PROTOCOLS..."): time.sleep(1.5)
                st.rerun()
            else:
                st.error("ACCESS DENIED: IDENTITY UNKNOWN")
else:
    # --- 3. النظام الرئيسي: إعادة البناء والتحليل ---
    st.markdown("<h1>🧬 NEURAL RECONSTRUCTION SYSTEM</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE (REAL OR AI)...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        original_img = cv2.imdecode(file_bytes, 1)
        
        # محاكاة كشف الأنمي/AI
        is_anime = random.choice([True, False]) 

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("1. UPLOADED SOURCE")
            st.image(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_anime:
                st.warning("⚠️ AI/ANIME DETECTED")
            else:
                st.success("✅ REAL SOURCE DETECTED")

        with col2:
            st.subheader("2. RECONSTRUCTION")
            if is_anime:
                with st.spinner("RECONSTRUCTING HUMAN FACE..."):
                    time.sleep(2)
                # عرض صورة بشرية حقيقية كمحاكاة للتحويل (يمكنك وضع رابط صورة حقيقية هنا)
                st.image("https://thispersondoesnotexist.com", caption="AI RECONSTRUCTED HUMAN", use_container_width=True)
                st.info("Neural-Link: Anime features converted to Human Bio-data.")
                process_img = original_img # في الحقيقة سنعالج الأصلية للتوضيح
            else:
                st.image(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB), caption="NO RECONSTRUCTION NEEDED", use_container_width=True)
                process_img = original_img

        with col3:
            st.subheader("3. SIGNATURE EXTRACTION")
            if st.button("EXTRACT BIO-SIG"):
                gray = cv2.cvtColor(process_img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1000)
                kp, des = orb.detectAndCompute(gray, None)
                
                img_kp = cv2.drawKeypoints(process_img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"Extracted: {len(kp)} Points")
                if des is not None:
                    st.code(str(des[:5]))

    st.sidebar.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({"auth": False}))
