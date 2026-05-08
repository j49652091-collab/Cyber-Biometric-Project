import streamlit as st
import cv2
import numpy as np
import time
import random

# --- 1. إعدادات الواجهة والجماليات (The Luxury Cyber Theme) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    /* خلفية داكنة مع تأثير تدرج احترافي */
    .stApp { 
        background: radial-gradient(circle, #051505 0%, #000000 100%); 
        color: #00ff00; 
        font-family: 'Courier New', sans-serif; 
    }
    
    /* تصميم العناوين المشعة */
    .glitch-title {
        color: #00ff00;
        font-size: 65px;
        font-weight: 900;
        text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 5px;
        margin-bottom: 10px;
    }

    /* تأثير الكلام المتحرك في الخلفية (Matrix Look) */
    .hacker-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        color: rgba(0, 255, 0, 0.05);
        font-size: 12px;
        z-index: -1;
        overflow: hidden;
        pointer-events: none;
    }

    /* الأزرار الملكية: نص أسود ملكي وتوهج نيون */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border-radius: 2px; border: 2px solid #00ff00; 
        box-shadow: 0 0 25px rgba(0,255,0,0.6);
        transition: 0.5s; height: 3.5em; width: 100%;
        text-transform: uppercase;
    }
    .stButton>button:hover { 
        transform: scale(1.05); 
        box-shadow: 0 0 60px #00ff00; 
        color: #ffffff !important; 
        background: #000 !important; 
    }

    /* تنسيق مربعات الإدخال بشكل تقني */
    input { 
        background-color: rgba(0, 20, 0, 0.8) !important; 
        color: #00ff00 !important; 
        border: 1px solid #00ff00 !important; 
        font-size: 18px !important;
        text-align: center;
    }
    
    .status-card {
        border: 2px solid #00ff00;
        padding: 20px;
        background: rgba(0, 255, 0, 0.05);
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. شاشة الدخول الفخمة (The Terminal Login) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    # إضافة "ستيكر" أو رمز جرافيكي كبير في البداية
    st.markdown("<p style='text-align: center; font-size: 100px; margin-bottom: 0;'>🛡️</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='glitch-title'>NEURAL-X ACCESS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00ff00; letter-spacing: 3px;'>[ BIOMETRIC SECURITY PROTOCOL v5.5 ]</p>", unsafe_allow_html=True)
    
    st.write(" ") # مساحة فارغة
    
    _, col2, _ = st.columns([1, 1.5, 1])
    with col2:
        with st.container():
            st.markdown("<div class='status-card'>", unsafe_allow_html=True)
            user = st.text_input("ENTER AGENT_ID", placeholder="e.g. Esraa")
            pas = st.text_input("SEC_KEY", type="password", placeholder="•••••")
            
            if st.button("EXECUTE AUTHENTICATION"):
                if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                    st.session_state['auth'] = True
                    with st.spinner("BYPASSING ENCRYPTION LAYERS..."):
                        time.sleep(2)
                    st.rerun()
                else:
                    st.error("ACCESS DENIED: INTRUSION DETECTED!")
            st.markdown("</div>", unsafe_allow_html=True)
    
    # كلام تقني في الأسفل لزيادة الفخامة
    st.markdown("<br><p style='text-align: center; font-size: 12px; opacity: 0.5;'>IP_TRACE: 192.168.1.104 | ENCRYPTION: AES-256 | STATUS: WAITING_FOR_AUTH</p>", unsafe_allow_html=True)

else:
    # --- 3. النظام الرئيسي (بعد الدخول) ---
    st.markdown("<h1 class='glitch-title'>🧬 NEURAL-X ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        
        # خوارزمية الكشف الذكية
        is_ai = sat_mean > 115 or sat_mean < 40

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### [01] RAW SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI/ANIME DETECTED")
            else: st.success("✅ HUMAN SOURCE VERIFIED")

        with col2:
            st.markdown("### [02] RECONSTRUCTION")
            with st.spinner("ANALYZING TEXTURES..."):
                detail = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
                kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                reconstructed = cv2.filter2D(detail, -1, kernel)
                time.sleep(1)
            st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), caption="REALISTIC PROJECTION", use_container_width=True)

        with col3:
            st.markdown("### [03] EXTRACTION")
            if st.button("EXTRACT SIGNATURE"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"FEATURES: {len(kp)}")
                if des is not None: st.code(str(des[:10]))

    st.sidebar.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({"auth": False}))
    st.sidebar.write("AGENT: **Esraa**")
