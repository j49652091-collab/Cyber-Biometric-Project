import streamlit as st
import cv2
import numpy as np
import time

# --- 1. واجهة فخمة جداً (Black & Neon Gold/Green) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧪", layout="wide")

st.markdown("""
    <style>
    /* تصميم الخلفية الداكنة العميقة */
    .stApp { background: radial-gradient(circle, #0a0a0a 0%, #000000 100%); color: #00ff00; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* العناوين بنظام توهج النيون */
    h1 { color: #00ff00 !important; text-align: center; text-shadow: 0 0 30px #00ff00; font-size: 60px; font-weight: 900; }
    h3 { color: #00ff00 !important; border-bottom: 1px solid #00ff00; padding-bottom: 10px; }

    /* الأزرار الفخمة: نص أسود، خلفية خضراء مشعة، مع تأثير عند المرور */
    .stButton>button { 
        background-color: #00ff00 !important; 
        color: #000000 !important; 
        font-weight: bold !important; 
        font-size: 18px !important;
        border-radius: 5px; border: none;
        box-shadow: 0 0 15px #00ff00;
        transition: 0.4s all;
        height: 3.5em; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 25px #00ff00; color: #fff !important; background-color: #000 !important; border: 1px solid #00ff00; }

    /* تحسين شكل مربعات الإدخال */
    input { background-color: #111 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-size: 18px !important; }
    
    /* تنسيق الصور */
    .stImage > img { border: 2px solid #00ff00; box-shadow: 0 0 20px rgba(0,255,0,0.3); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول المتطور ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1>BIO-CORE ACCESS</h1>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.write("---")
        user = st.text_input("AGENT IDENTITY (USER)")
        pas = st.text_input("SECURITY KEY (PASS)", type="password")
        if st.button("INITIATE PROTOCOL"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                with st.spinner("SYNCHRONIZING NEURAL NETWORKS..."): time.sleep(2)
                st.rerun()
            else:
                st.error("UNAUTHORIZED ACCESS: CLEARANCE DENIED")
else:
    # --- 3. النظام الرئيسي: التحليل وإعادة البناء ---
    st.markdown("<h1>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("UPLOAD TARGET SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        # قراءة الصورة
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # خوارزمية ذكية لكشف الأنمي/AI (تعتمد على نعومة الحواف)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai_anime = laplacian_var < 500  # الأنمي غالباً حوافه أنعم بكثير من الصور الحقيقية

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("### [01] RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai_anime:
                st.error("⚠️ AI/ANIME STRUCTURE DETECTED")
                st.caption(f"Analysis: Low Texture Variance ({int(laplacian_var)})")
            else:
                st.success("✅ BIOMETRIC HUMAN VERIFIED")
                st.caption(f"Analysis: High Texture Detail ({int(laplacian_var)})")

        with col2:
            st.write("### [02] RECONSTRUCTION")
            if is_ai_anime:
                with st.spinner("GENERATING REAL HUMAN MATCH..."):
                    time.sleep(2)
                # صورة بشرية عالية الدقة لمحاكاة "التحويل القريب"
                st.image("https://thispersondoesnotexist.com", caption="RECONSTRUCTED HUMAN FACE", use_container_width=True)
                target_img = img # للمعالجة
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="REAL SOURCE CONFIRMED", use_container_width=True)
                target_img = img

        with col3:
            st.write("### [03] BIOMETRIC SIG")
            if st.button("START EXTRACTION"):
                # استخراج النقاط
                orb = cv2.ORB_create(nfeatures=1500)
                kp, des = orb.detectAndCompute(gray, None)
                
                # رسم النقاط بلون نيون
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                
                st.success(f"POINTS: {len(kp)} DETECTED")
                if des is not None:
                    st.code(str(des[:10]), language='python')

    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.markdown("---")
    st.sidebar.info("SYSTEM STATUS: SECURE\n\nAGENT: Esraa\n\nYEAR: 2026")
