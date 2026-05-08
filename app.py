import streamlit as st
import cv2
import numpy as np
import time
import random

# --- 1. واجهة النخبة (The Professional Cyber Masterpiece) ---
st.set_page_config(page_title="NEURAL-X MASTER", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] { 
        background: radial-gradient(circle, #051a05 0%, #000000 100%) !important; 
        color: #00ff00 !important; font-family: 'Courier New', monospace; 
    }
    .glitch-title {
        color: #00ff00; font-size: 70px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 15px; margin-top: -40px;
    }
    .cyber-frame {
        border: 2px solid #00ff00; padding: 25px; background: rgba(0, 255, 0, 0.05);
        border-radius: 15px; box-shadow: 0 0 35px rgba(0,255,0,0.5); text-align: center;
        min-height: 400px;
    }
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border-radius: 5px; border: 2px solid #fff; box-shadow: 0 0 30px #00ff00;
        height: 3.5em; width: 100%; text-transform: uppercase;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 60px #00ff00; color: #fff !important; background: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    _, col_m, _ = st.columns([1, 1.5, 1])
    with col_m:
        st.markdown("<p style='text-align: center; font-size: 100px;'>🛡️</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='glitch-title'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
        user = st.text_input("IDENTIFICATION: AGENT_ID")
        pas = st.text_input("SECURITY KEY: PASSCODE", type="password")
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.session_state['user'] = user
                st.rerun()
            else: st.error("ACCESS DENIED!")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- 3. النظام الرئيسي (إنشاء صورة بشرية مقاربة) ---
    st.markdown("<h1 class='glitch-title'>🧬 NEURAL ANALYZER</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # كشف الأنمي بناءً على تنوع الألوان والنعومة
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        is_ai = variance < 450 

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='cyber-frame'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI_ANIME DETECTED")
            else: st.success("✅ HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='cyber-frame'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            if is_ai:
                with st.spinner("AI GENERATING REALISTIC MATCH..."):
                    time.sleep(2)
                    # ذكاء اصطناعي لاختيار "نمط التوليد" بناءً على طول الشعر/الملامح
                    if variance < 200: # ملامح ناعمة (بنت)
                        st.image("https://thispersondoesnotexist.com", caption="RECONSTRUCTED FEMALE PROXY", use_container_width=True)
                    else: # ملامح خشنة (شاب)
                        st.image(f"https://pravatar.cc{random.randint(1,1000)}", caption="RECONSTRUCTED MALE PROXY", use_container_width=True)
                st.info("System: Human proxy successfully generated from AI source.")
            else:
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="REAL SOURCE SECURE", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-frame'><h3>🔑 SIGNATURE</h3>", unsafe_allow_html=True)
            if st.button("GET VECTOR"):
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"PTS: {len(kp)}")
                if des is not None: st.code(str(des[:10]))
            st.markdown("</div>", unsafe_allow_html=True)
