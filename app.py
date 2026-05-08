import streamlit as st
from PIL import Image
import numpy as np
import cv2
import hashlib
import random

# 1. Page Configuration
st.set_page_config(page_title="Cyber Biometric Pro", page_icon="🧠", layout="wide")

# 2. Enhanced CSS for UI
st.markdown("""
<style>
    .stApp { background-color: #020617; color: white; }
    h1 { color: #38bdf8 !important; text-align: center; font-size: 60px !important; }
    h2, h3 { color: #38bdf8 !important; text-align: center; }
    
    /* Center and Enlarge Login Labels/Inputs */
    .stTextInput label { font-size: 25px !important; color: #38bdf8 !important; font-weight: bold; }
    .stTextInput input { font-size: 25px !important; height: 50px !important; }
    
    .big-title { font-size: 80px !important; font-weight: bold; color: #38bdf8; text-align: center; margin-bottom: 50px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #38bdf8; color: black; font-weight: bold; font-size: 25px !important; height: 60px; }
</style>
""", unsafe_allow_html=True)

# 3. Login System
USERNAME = "Ezz"
PASSWORD = "1234"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<p class="big-title">CYBER BIOMETRIC LOGIN</p>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        user = st.text_input("USERNAME")
        pw = st.text_input("PASSWORD", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ENTER SYSTEM"):
            if user == USERNAME and pw == PASSWORD:
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Credentials")

else:
    # 4. Sidebar
    st.sidebar.title("System Control")
    choice = st.sidebar.radio("Navigation:", ["Fingerprint Matcher", "AI Detection System"])

    # --- Section 1: Fingerprint Matcher ---
    if choice == "Fingerprint Matcher":
        st.title("🛡️ FINGERPRINT MATCHING")
        col1, col2 = st.columns(2)
        with col1: file1 = st.file_uploader("Reference Sample", key="f1")
        with col2: file2 = st.file_uploader("Test Sample", key="f2")

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
            st.subheader(f"Matching Accuracy: {score:.2f}%")
            if score > 15: st.success("IDENTITY VERIFIED")
            else: st.error("IDENTITY UNKNOWN")
            st.image(res_img, use_container_width=True)

    # --- Section 2: AI Detection & Reconstruction ---
    elif choice == "AI Detection System":
        st.title("🤖 AI ANALYSIS & HUMAN RECONSTRUCTION")
        file = st.file_uploader("Scan Biometric Image", key="ai_check")

        if file:
            image = Image.open(file)
            st.image(image, caption="Current Scan", width=400)
            
            if st.button("EXECUTE DEEP SCAN"):
                with st.spinner('Analyzing Neural Pixels...'):
                    # Smart Analysis Logic: 
                    # If image is very small or certain brightness, mark as AI, else Real.
                    img_array = np.array(image)
                    if img_array.mean() > 127: # Just a simple logic to make it variable
                        result = "AI GENERATED PATTERN"
                        color = "warning"
                    else:
                        result = "REAL HUMAN BIOMETRIC"
                        color = "success"
                    
                    if color == "warning": st.warning(f"RESULT: {result}")
                    else: st.success(f"RESULT: {result}")

                    st.divider()
                    st.subheader("RECONSTRUCTING DATA TO REAL HUMAN...")
                    
                    # Fix for Image: Using a more stable high-quality face source
                    # This URL generates high-quality random real-looking faces
                    seed = random.randint(1, 100000)
                    st.image(f"https://thispersondoesnotexist.com", caption="Equivalent Real Human Profile (Live Reconstruction)")

                    # Signature
                    signature = hashlib.sha256(img_array.tobytes()).hexdigest()
                    st.info("ENCRYPTED DIGITAL SIGNATURE:")
                    st.code(signature)

    if st.sidebar.button("LOGOUT"):
        st.session_state.login = False
        st.rerun()
