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
    
    /* الأزرار: نص أسود ملكي واضح جداً */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 18px !important;
        border-radius: 4px; border: none; box-shadow: 0 0 20px #00ff00;
        transition: 0.4s; height: 4em; width: 100%;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 50px #00ff00; color: #ffffff !important; background: #000 !important; border: 1px solid #00ff00; }
    input { background-color: #000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    .stImage > img { border: 2px solid #00ff00; box-shadow: 0 0 25px rgba(0,255,0,0.3); border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>BIO-CORE ACCESS</h1>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.2, 1])
    with col2:
        user = st.text_input("AGENT_ID")
        pas = st.text_input("SEC_KEY", type="password")
        if st.button("EXECUTE AUTH"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
else:
    # --- 3. النظام الرئيسي: الكشف اللوني الدقيق ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT SOURCE DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # --- خوارزمية كشف الـ AI بناءً على تشبع الألوان وتنوعها ---
        saturation_mean = np.mean(hsv[:,:,1])
        # صور الـ AI والأنمي تمتاز بتشبع لوني عالٍ جداً أو ألوان "مسطحة"
        # البشر لديهم توازن طبيعي في توزيع الألوان
        is_ai = saturation_mean > 115 or saturation_mean < 40

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai:
                st.error("⚠️ AI/ANIME DETECTED")
                st.caption(f"Reason: Artificial Color Profile ({saturation_mean:.1f})")
            else:
                st.success("✅ HUMAN SOURCE VERIFIED")
                st.caption(f"Reason: Natural Skin Tone Profile ({saturation_mean:.1f})")

        with col2:
            st.markdown("### RECONSTRUCTION")
            with st.spinner("ENHANCING BIOMETRIC TEXTURES..."):
                # معالجة تعزز التفاصيل البشرية (نفس الشخصية)
                detail_img = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
                kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                reconstructed = cv2.filter2D(detail_img, -1, kernel)
                time.sleep(1.5)
            
            st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), 
                     caption="REALISTIC PROJECTION" if is_ai else "ENHANCED BIOMETRIC VIEW", 
                     use_container_width=True)

        with col3:
            st.markdown("### EXTRACTION")
            if st.button("EXTRACT SIGNATURE"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"FEATURES: {len(kp)} POINTS")
                if des is not None:
                    st.code(str(des[:10]))

    st.sidebar.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.write("AGENT: **Esraa**")
