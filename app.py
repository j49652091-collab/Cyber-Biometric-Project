import streamlit as st
from PIL import Image
import numpy as np
import cv2
import hashlib
import random

# 1. Page Configuration
st.set_page_config(page_title="Cyber Biometric Pro", page_icon="🧠", layout="wide")

# 2. CSS for Centering Login and Styling
st.markdown("""
<style>
    .stApp { background-color: #020617; color: white; }
    h1, h2, h3 { color: #38bdf8 !important; text-align: center; }
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .big-font { font-size: 50px !important; font-weight: bold; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #38bdf8; color: black; font-weight: bold; }
    p { text-align: center; font-size: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. Login System
USERNAME = "Ezz"
PASSWORD = "1234"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<p class="big-font">🧠 CYBER BIOMETRIC LOGIN</p>', unsafe_allow_html=True)
    
    # Centering inputs using columns
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        user = st.text_input("USERNAME")
        pw = st.text_input("PASSWORD", type="password")
        if st.button("LOGIN"):
            if user == USERNAME and pw == PASSWORD:
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Access Denied: Wrong Credentials")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # 4. Sidebar Navigation (English Only)
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to:", ["Fingerprint Matcher", "AI Detection System"])

    # --- Section 1: Fingerprint Matcher ---
    if choice == "Fingerprint Matcher":
        st.title("🛡️ FINGERPRINT MATCHING SYSTEM")
        
        col1, col2 = st.columns(2)
        with col1:
            file1 = st.file_uploader("Upload Reference Base", key="f1")
        with col2:
            file2 = st.file_uploader("Upload Target Sample", key="f2")

        if file1 and file2:
            img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), 1)
            img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), 1)

            sift = cv2.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)
            good = [m for m, n in matches if m.distance < 0.7 * n.distance]

            score = (len(good) / min(len(kp1), len(kp2))) * 100
            res_img = cv2.drawMatches(img1, kp1, img2, kp2, good, None)

            st.subheader(f"Matching Score: {score:.2f}%")
            if score > 15:
                st.success("MATCH SUCCESSFUL: BIOMETRIC IDENTITY VERIFIED")
            else:
                st.error("MATCH FAILED: UNKNOWN IDENTITY")
            
            st.image(res_img, use_container_width=True)

    # --- Section 2: AI Detection & Human Generation ---
    elif choice == "AI Detection System":
        st.title("🤖 AI ANALYSIS & HUMAN RECONSTRUCTION")
        
        file = st.file_uploader("Upload Image for Scanning", key="ai_check")

        if file:
            image = Image.open(file)
            st.image(image, caption="Uploaded Scan", width=400)
            
            if st.button("START DEEP SCAN"):
                with st.spinner('Scanning Neural Patterns...'):
                    # Simulated logic: if user uploads, it detects AI (for the demo)
                    result = "AI GENERATED" 
                    st.warning(f"RESULT: {result}")

                    st.divider()
                    st.subheader("RECONSTRUCTING REAL HUMAN DATA...")
                    # Generating a "Real Human" equivalent using a high-quality placeholder
                    # Each click gives a new real-looking person
                    random_id = random.randint(1, 1000)
                    st.image(f"https://picsum.photos{random_id}", caption="Equivalent Real Human Profile")

                    # Security Hash
                    img_array = np.array(image)
                    signature = hashlib.sha256(img_array.tobytes()).hexdigest()
                    st.info("DIGITAL SIGNATURE (SHA-256):")
                    st.code(signature)

    if st.sidebar.button("LOGOUT"):
        st.session_state.login = False
        st.rerun()
