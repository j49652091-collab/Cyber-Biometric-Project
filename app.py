import streamlit as st
import cv2
import numpy as np
import time

# --- 1. Page Configuration (Hacker Theme) ---
st.set_page_config(page_title="TERMINAL ACCESS", page_icon="🔐", layout="centered")

# --- 2. Custom CSS for Hacker Look ---
st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    .stApp {
        background-color: #000000;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3, p, span {
        color: #00ff00 !important;
        text-shadow: 0 0 5px #00ff00;
    }
    .stButton>button {
        background-color: #00ff00 !important;
        color: black !important;
        font-weight: bold;
        border-radius: 0px;
        border: none;
        width: 100%;
    }
    input {
        background-color: black !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Login Logic ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown("# >> SYSTEM BREACH DETECTED_")
    st.write("---")
    st.subheader("ENTER AUTHENTICATION CREDENTIALS")
    
    user = st.text_input("IDENTIFICATION (USER)")
    pas = st.text_input("ACCESS CODE (PASS)", type="password")
    
    if st.button("EXECUTE LOGIN"):
        if user in ["Israa", "Weam", "Tasneem"] and pas == "12345":
            st.session_state['authenticated'] = True
            with st.spinner("BYPASSING FIREWALLS..."):
                time.sleep(2)
            st.rerun()
        else:
            st.error("ACCESS DENIED! INTRUSION DETECTED!")
            st.toast("Alerting Security Protocol...", icon="🚨")

# --- 4. Main Biometric System (After Login) ---
else:
    st.title("🛡️ BIOMETRIC SIGNATURE SYSTEM")
    st.write(f">> Welcome Agent: {st.session_state.get('user', 'Authorized')}")
    st.markdown("---")

    # --- Sidebar Info ---
    with st.sidebar:
        st.header("SYSTEM STATUS")
        st.write("● ENCRYPTION: ACTIVE")
        st.write("● TRACE_ID: 9664ef8")
        if st.button("TERMINATE SESSION"):
            st.session_state['authenticated'] = False
            st.rerun()

    # --- File Uploader ---
    st.write("### [STEP 01]: UPLOAD BIOMETRIC SOURCE")
    uploaded_file = st.file_uploader("Select Image...", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        st.image(rgb_image, caption='SOURCE_INPUT', use_container_width=True)
        
        if st.button("START EXTRACTION 🧬"):
            orb = cv2.ORB_create(nfeatures=1000)
            keypoints, descriptors = orb.detectAndCompute(gray, None)
            
            if descriptors is not None:
                img_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)
                st.image(cv2.cvtColor(img_with_keypoints, cv2.COLOR_BGR2RGB), 
                         caption='FEATURES_MAPPED', use_container_width=True)
                
                st.success(f"SUCCESS: {len(keypoints)} FEATURES DECRYPTED!")
                st.write("### 🔑 DIGITAL IDENTITY VECTOR:")
                st.code(descriptors[:15]) 
                st.warning("ENCRYPTION NOTE: Mathematical vector generated for secure authentication.")
            else:
                st.error("FAILED: CLEAR FEATURES NOT FOUND.")

    st.divider()
    st.caption("SECURED TERMINAL - CLASS OF 2026 - STATUS: EXPLOIT_ACTIVE")


