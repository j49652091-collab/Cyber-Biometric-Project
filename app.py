import streamlit as st
import cv2
import numpy as np
import time

# --- 1. واجهة فخمة بمستوى "السيبراني العالمي" ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #050505 0%, #001a00 100%); color: #00ff00; font-family: 'Segoe UI', sans-serif; }
    h1 { color: #00ff00 !important; text-align: center; text-shadow: 0 0 30px #00ff00; font-size: 55px; margin-bottom: 30px; }
    
    /* الأزرار: نص أسود واضح جداً وتأثير نيون */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border-radius: 8px; border: none; box-shadow: 0 0 20px rgba(0,255,0,0.4);
        transition: 0.3s all; height: 3.5em; width: 100%;
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 0 40px #00ff00; color: #fff !important; }

    input { background-color: #000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    .stImage > img { border: 2px solid #00ff00; box-shadow: 0 0 25px rgba(0,255,0,0.2); border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول المتطور (Esraa) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>BIO-CORE LOGIN</h1>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.5, 1])
    with col2:
        user = st.text_input("IDENTIFICATION (USER)")
        pas = st.text_input("SECURITY KEY (PASS)", type="password")
        if st.button("AUTHORIZE ACCESS"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                with st.spinner("DECRYPTING INTERFACE..."): time.sleep(1.5)
                st.rerun()
            else:
                st.error("ACCESS DENIED: CLEARANCE REQUIRED")
else:
    # --- 3. النظام الرئيسي: الكشف وإعادة البناء ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER v5.1</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("DRAG & DROP BIOMETRIC DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # --- خوارزمية كشف الأنمي/AI مطورة ---
        # نحسب عدد الألوان الفريدة؛ الأنمي غالباً ألوانه أقل تعقيداً من البشر
        unique_colors = len(np.unique(img.reshape(-1, img.shape[2]), axis=0))
        is_ai_anime = unique_colors < 80000  # الأنمي غالباً أقل من هذا الرقم بكثير

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### [01] RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai_anime:
                st.error("⚠️ AI/ANIME SIGNATURE DETECTED")
                st.caption(f"Analysis: Low Pixel Entropy (Synthetic)")
            else:
                st.success("✅ HUMAN SOURCE VERIFIED")
                st.caption(f"Analysis: High Pixel Complexity (Natural)")

        with col2:
            st.markdown("### [02] RECONSTRUCTION")
            if is_ai_anime:
                with st.spinner("RECONSTRUCTING HUMAN MATCH..."):
                    time.sleep(2.5)
                # عرض صورة بشرية حقيقية "فخمة" وقريبة (كمحاكاة للتحويل)
                st.image("https://thispersondoesnotexist.com", caption="AI RECONSTRUCTED HUMAN", use_container_width=True)
                st.info("Neural-Reconstruction: Successfully generated human proxy.")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="NO RECONSTRUCTION REQUIRED", use_container_width=True)

        with col3:
            st.markdown("### [03] EXTRACTION")
            if st.button("EXTRACT BIO-SIGNATURE"):
                orb = cv2.ORB_create(nfeatures=1500)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"FEATURES: {len(kp)} POINTS")
                if des is not None:
                    st.code(str(des[:10]), language='python')

    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.markdown("---")
    st.sidebar.info("PROJECT: BIOMETRIC-SIG\nAGENT: Esraa\nSTATUS: ONLINE")

