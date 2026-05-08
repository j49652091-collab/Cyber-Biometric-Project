import streamlit as st
import cv2
import numpy as np
import time

# --- 1. اعدادات الصفحة وثيم الهكر ---
st.set_page_config(page_title="TERMINAL ACCESS", page_icon="🔐")

st.markdown("""
    <style>
    .stApp { background-color: black; color: #00ff00; font-family: 'Courier New'; }
    h1, h2, h3, p { color: #00ff00 !important; text-shadow: 0 0 5px #00ff00; }
    .stButton>button { background-color: #00ff00 !important; color: black !important; width: 100%; border-radius: 0px; font-weight: bold; }
    input { background-color: black !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. منطق تسجيل الدخول ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("# >> SYSTEM BREACH: AUTHORIZED ONLY_")
    st.write("---")
    user = st.text_input("IDENTIFICATION (USER)")
    pas = st.text_input("ACCESS CODE (PASS)", type="password")
    
    if st.button("EXECUTE LOGIN"):
        if user in ["Israa", "Weam", "Tasneem"] and pas == "12345":
            st.session_state['auth'] = True
            with st.spinner("BYPASSING FIREWALLS..."):
                time.sleep(2)
            st.rerun()
        else:
            st.error("ACCESS DENIED! INTRUSION DETECTED!")
else:
    # --- 3. برنامج البصمة الأصلي (يظهر بعد الدخول) ---
    st.title("🛡️ BIOMETRIC SIGNATURE SYSTEM")
    st.write(">> Status: SYSTEM ACCESSED")
    
    uploaded_file = st.file_uploader("Upload Biometric Image...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        if st.button("Extract Biometric Signature 🧬"):
            orb = cv2.ORB_create(nfeatures=1000)
            keypoints, descriptors = orb.detectAndCompute(gray, None)
            
            if descriptors is not None:
                img_out = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0))
                st.image(cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB), caption='Features Mapped')
                st.success(f"Success: {len(keypoints)} points identified!")
                st.code(descriptors[:10]) # عرض جزء من البصمة الرقمية
            else:
                st.error("Failed to detect features.")

    if st.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
