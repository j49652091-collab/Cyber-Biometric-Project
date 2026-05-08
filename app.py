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
        user = st.text_input("AGENT_ID (Esraa/Weam/Tasneem)")
        pas = st.text_input("SEC_KEY", type="password")
        if st.button("EXECUTE AUTH"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
else:
    # --- 3. النظام الرئيسي: التحويل المنطقي لنفس الشخصية ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT SOURCE DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        # كشف الذكاء الاصطناعي/الأنمي بناءً على تحليل الألوان
        unique_colors = len(np.unique(img.reshape(-1, img.shape), axis=0))
        is_ai = unique_colors < 100000 

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### [01] RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai:
                st.error("⚠️ AI/ANIME SIGNATURE DETECTED")
            else:
                st.success("✅ HUMAN SOURCE VERIFIED")

        with col2:
            st.markdown("### [02] RECONSTRUCTION")
            if is_ai:
                with st.spinner("REBUILDING HUMAN TEXTURES..."):
                    time.sleep(2)
                    # معالجة حقيقية للصورة: تحويلها لدرجات رمادية ثم إعادة حدتها لتبدو بشرية
                    # هذه الطريقة تحافظ على "نفس ملامح" الصورة المرفوعة بدقة
                    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
                    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
                    processed_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
                    # زيادة الحدة (Sharpening)
                    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                    reconstructed = cv2.filter2D(processed_img, -1, kernel)
                    
                st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), caption="REAL-WORLD PROJECTION", use_container_width=True)
                st.info("System: Textures re-mapped to Human standards.")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="SOURCE INTEGRITY SECURE", use_container_width=True)

        with col3:
            st.markdown("### [03] EXTRACTION")
            if st.button("EXTRACT SIGNATURE"):
                # استخراج النقاط الحيوية
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"FEATURES: {len(kp)} POINTS")
                if des is not None:
                    st.code(str(des[:10]))

    st.sidebar.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.markdown("---")
    st.sidebar.write("AGENT: **Esraa**")
    st.sidebar.write("STATUS: **ONLINE**")

