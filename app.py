import streamlit as st
import cv2
import numpy as np
import time
from datetime import datetime

# --- 1. واجهة النخبة (Ultra-Stable Cyber UI) ---
st.set_page_config(page_title="NEURAL-X ELITE", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    /* تصميم الخلفية الداكنة العميقة */
    .stApp, [data-testid="stSidebar"] { 
        background: radial-gradient(circle, #001a00 0%, #000000 100%) !important; 
        color: #00ff00 !important; 
        font-family: 'Courier New', monospace; 
    }
    
    /* عنوان النيون الفخم */
    .elite-header {
        color: #00ff00; font-size: 65px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
        letter-spacing: 12px; margin-bottom: 5px;
    }

    /* كوادِر النيون للصور والنتائج */
    .cyber-card {
        border: 2px solid #00ff00;
        padding: 20px;
        background: rgba(0, 255, 0, 0.05);
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(0,255,0,0.3);
        text-align: center;
        margin: 10px;
    }

    /* الأزرار الملكية: نص أسود واضح */
    .stButton>button { 
        background-color: #00ff00 !important; color: #000000 !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border-radius: 8px; border: 2px solid #ffffff; 
        box-shadow: 0 0 30px rgba(0,255,0,0.6);
        transition: 0.4s; height: 3.5em; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 60px #00ff00; color: #fff !important; background: #000 !important; }

    /* تنسيق القائمة الجانبية الذكية */
    .sidebar-box {
        border-left: 3px solid #00ff00;
        padding-left: 15px;
        margin-bottom: 20px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. شاشة الدخول (المستقرة والفخمة) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    # استخدام أعمدة لتوسيط المحتوى بدلاً من الصور المكسورة
    _, main_col, _ = st.columns([1, 2, 1])
    
    with main_col:
        st.markdown("<p style='text-align: center; font-size: 100px;'>🔒</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='elite-header'>NEURAL-X</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #fff; letter-spacing: 4px; font-weight:bold;'>[ MILITARY-GRADE BIOMETRIC ACCESS ]</p>", unsafe_allow_html=True)
        
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        user = st.text_input("IDENTIFICATION: AGENT_ID", placeholder="Enter Name...")
        pas = st.text_input("SECURITY KEY: PASSCODE", type="password", placeholder="•••••")
        
        if st.button("EXECUTE AUTHENTICATION"):
            if user in ["Esraa", "Weam", "Tasneem"] and pas == "12345":
                st.session_state['auth'] = True
                st.session_state['user'] = user
                with st.spinner("DECRYPTING INTERFACE..."): time.sleep(1.5)
                st.rerun()
            else:
                st.error("ACCESS DENIED: INTRUSION DETECTED!")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # رموز تقنية بدلاً من الصور
        st.markdown("<p style='text-align: center; font-size: 12px; opacity: 0.6;'>STATUS: WAITING_FOR_SYNC | ENCRYPTION: SHA-512 | NODE: 0.0.0.0</p>", unsafe_allow_html=True)

else:
    # --- 3. القائمة الجانبية (Sidebar) المليئة بالمعلومات الذكية ---
    with st.sidebar:
        st.markdown("## 🖥️ SYSTEM TERMINAL")
        st.markdown(f"""
        <div class='sidebar-box'>
        <b style='color:white;'>AGENT:</b> {st.session_state['user']}<br>
        <b style='color:white;'>LOG_TIME:</b> {datetime.now().strftime('%H:%M:%S')}<br>
        <b style='color:white;'>DATE:</b> {datetime.now().strftime('%d/%m/%Y')}<br>
        <b style='color:white;'>LOCATION:</b> Jordan / Secure_Hub<br>
        <hr style='border-color:#00ff00;'>
        <b style='color:white;'>NETWORK:</b> <span style='color:#00ff00;'>CONNECTED</span><br>
        <b style='color:white;'>Uptime:</b> {time.process_time():.2f}s<br>
        <b style='color:white;'>ID_TRACE:</b> #9664EF8
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("TERMINATE SESSION"):
            st.session_state['auth'] = False
            st.rerun()

    # --- 4. النظام الرئيسي وعرض النتائج ---
    st.markdown("<h1 class='elite-header'>🧬 NEURAL ANALYZER</h1>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("INJECT BIOMETRIC SOURCE DATA...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat_mean = np.mean(hsv[:,:,1])
        is_ai = sat_mean > 115 or sat_mean < 40

        # ترتيب النتائج داخل كوادِر نيون مرتبة
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='cyber-card'><h3>🔍 SOURCE</h3>", unsafe_allow_html=True)
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
            if is_ai: st.error("⚠️ AI/ANIME DETECTED")
            else: st.success("✅ HUMAN VERIFIED")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='cyber-card'><h3>🛠️ REBUILD</h3>", unsafe_allow_html=True)
            detail = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            reconstructed = cv2.filter2D(detail, -1, kernel)
            st.image(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='cyber-card'><h3>🔑 VECTOR</h3>", unsafe_allow_html=True)
            if st.button("GET SIGNATURE"):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                orb = cv2.ORB_create(nfeatures=1200)
                kp, des = orb.detectAndCompute(gray, None)
                img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.success(f"PTS: {len(kp)}")
                if des is not None: st.code(str(des[:8]))
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<br><p style='text-align: center; opacity: 0.4;'>READY FOR SOURCE INJECTION | WAITING...</p>", unsafe_allow_html=True)
