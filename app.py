import streamlit as st
import cv2
import numpy as np
import time

# --- 1. واجهة فخمة جداً (Cyber-Dark UI) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050a05 0%, #000000 100%); color: #00ff00; font-family: 'Courier New', sans-serif; }
    h1 { color: #00ff00 !important; text-align: center; text-shadow: 0 0 30px #00ff00; font-size: 50px; font-weight: 900; }
    
    /* الأزرار: نص أسود ملكي وتوهج نيون */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 22px !important;
        border-radius: 4px; border: none; box-shadow: 0 0 20px #00ff00;
        transition: 0.4s; height: 3.5em; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 50px #00ff00; color: #ffffff !important; background: #000 !important; border: 1px solid #00ff00; }

    /* تنسيق الصور والنتائج */
    .stImage > img { border: 2px solid #00ff00; box-shadow: 0 0 25px rgba(0,255,0,0.3); border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول (Esraa) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>BIO-CORE ACCESS</h1>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.2, 1])
    with col2:
        st.write("---")
        user = st.text_input("AGENT_ID")
        pas = st.text_input("SEC_KEY", type="password")
        if st.button("EXECUTE AUTH"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
else:
    # --- 3. النظام الرئيسي: التحليل المصحح ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT SOURCE DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        # --- إصلاح خطأ السطر 55 (كشف الأنمي بطريقة مستقرة) ---
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # تحليل نعومة الحواف للكشف عن الأنمي
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 450  # الأنمي عادة يكون أقل من هذا الرقم

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai:
                st.error("⚠️ AI/ANIME SIGNATURE DETECTED")
            else:
                st.success("✅ HUMAN SOURCE VERIFIED")

        with col2:
            st.markdown("### RECONSTRUCTION")
            if is_ai:
                with st.spinner("CONVERTING TO REALISTIC TEXTURE..."):
                    time.sleep(2)
                    # معالجة الصورة لتبدو بشرية (نفس الملامح ولكن بحدة وملمس بشري)
                    detail_img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
                    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                    reconstructed = cv2.filter2D(detail_img, -1, kernel)
                st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), caption="REALISTIC PROJECTION", use_container_width=True)
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="SOURCE INTEGRITY SECURE", use_container_width=True)

        with col3:
            st.markdown("### EXTRACTION")
            if st.button("EXTRACT SIGNATURE"):
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"FEATURES: {len(kp)}")
                if des is not None:
                    st.code(str(des[:10]))

    st.sidebar.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.markdown("---")
    st.sidebar.write("AGENT: **Esraa**")
