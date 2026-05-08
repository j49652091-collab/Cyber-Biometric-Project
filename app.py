import streamlit as st
import cv2
import numpy as np
import time

# --- 1. واجهة الأكشن والهكر (Ultra Cyber-War Edition) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { 
        background: radial-gradient(circle, #051505 0%, #000000 100%); 
        color: #00ff00; 
        font-family: 'Courier New', sans-serif; 
    }
    
    .glitch-title {
        color: #00ff00; font-size: 70px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 10px; margin-top: -20px;
    }

    /* تنسيق الأزرار: نص أسود ملكي وتوهج نيون */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 22px !important;
        border-radius: 5px; border: 2px solid #ffffff; 
        box-shadow: 0 0 30px rgba(0,255,0,0.8);
        transition: 0.4s; height: 3.5em; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 60px #00ff00; color: #fff !important; background: #000 !important; }

    /* خانات الإدخال */
    input { 
        background-color: rgba(0, 0, 0, 0.9) !important; 
        color: #00ff00 !important; border: 2px solid #00ff00 !important; 
        font-size: 20px !important; text-align: center; height: 50px !important;
    }
    
    /* إخفاء العناصر الزائدة في Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. شاشة الدخول الهجومية (Attack Interface) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    # توزيع الشاشة: صور هكر على الأطراف والدخول في المنتصف
    side_col1, main_col, side_col2 = st.columns([1, 2, 1])
    
    with side_col1:
        st.write(" ") # مساحة
        st.image("https://giphy.com", use_container_width=True)
        st.markdown("<p style='text-align:center; font-size:10px;'>SYSTEM_OVERRIDE_ACTIVE</p>", unsafe_allow_html=True)

    with main_col:
        st.markdown("<p style='text-align: center; font-size: 80px;'>🛡️</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='glitch-title'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #fff; letter-spacing: 5px; font-weight:bold;'>[ TOP SECRET ACCESS ]</p>", unsafe_allow_html=True)
        
        # حذفت المربع الفاضي الزائد هنا
        user = st.text_input("IDENTIFICATION: AGENT_ID")
        pas = st.text_input("SECURITY KEY: PASSCODE", type="password")
        
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                with st.spinner("INJECTING PAYLOAD..."): time.sleep(2)
                st.rerun()
            else:
                st.error("ACCESS DENIED: INTRUSION DETECTED!")

    with side_col2:
        st.write(" ")
        st.image("https://giphy.com", use_container_width=True)
        st.markdown("<p style='text-align:center; font-size:10px;'>ENCRYPTING_DATA_FLOW</p>", unsafe_allow_html=True)

else:
    # --- 3. النظام الرئيسي (بعد الدخول) ---
    st.markdown("<h1 class='glitch-title'>🧬 ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        is_ai = sat_mean > 115 or sat_mean < 40

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### SOURCE")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI DETECTED")
            else: st.success("✅ HUMAN VERIFIED")

        with col2:
            st.markdown("### RECONSTRUCTION")
            detail = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            reconstructed = cv2.filter2D(detail, -1, kernel)
            st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), use_container_width=True)

        with col3:
            st.markdown("### EXTRACTION")
            if st.button("GET SIGNATURE"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"POINTS: {len(kp)}")

    st.sidebar.button("TERMINATE", on_click=lambda: st.session_state.update({"auth": False}))
