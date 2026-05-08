import streamlit as st
from PIL import Image
import numpy as np
import cv2
import hashlib
import random

# 1. Page Configuration
st.set_page_config(page_title="Cyber Biometric Pro", page_icon="🧠", layout="wide")

# 2. Enhanced CSS
st.markdown("""
<style>
    .stApp { background-color: #020617; color: white; }
    h1 { color: #38bdf8 !important; text-align: center; font-size: 60px !important; }
    .stTextInput label { font-size: 25px !important; color: #38bdf8 !important; font-weight: bold; }
    .stTextInput input { font-size: 25px !important; height: 50px !important; }
    .big-title { font-size: 80px !important; font-weight: bold; color: #38bdf8; text-align: center; margin-bottom: 50px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #38bdf8; color: black; font-weight: bold; font-size: 25px !important; height: 60px; }
</style>
""", unsafe_allow_html=True)

# 3. Login System
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<p class="big-title">CYBER BIOMETRIC LOGIN</p>', unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1,2,1])
    with col_b:
        user = st.text_input("USERNAME")
        pw = st.text_input("PASSWORD", type="password")
        if st.button("ENTER SYSTEM"):
            if user == "Ezz" and pw == "1234":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Access Denied")
else:
    # 4. Sidebar & Navigation
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to:", ["Fingerprint Matcher", "AI Detection System"])

    if choice == "Fingerprint Matcher":
        st.title("🛡️ FINGERPRINT MATCHING")
        col1, col2 = st.columns(2)
        with col1: file1 = st.file_uploader("Reference Sample", key="f1")
        with col2: file2 = st.file_uploader("Test Sample", key="f2")
        if file1 and file2:
            img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), 1)
            img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), 1)
            sift = cv2.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img1, None); kp2, des2 = sift.detectAndCompute(img2, None)
            matches = cv2.BFMatcher().knnMatch(des1, des2, k=2)
            good = [m for m, n in matches if m.distance < 0.7 * n.distance]
            score = (len(good) / min(len(kp1), len(kp2))) * 100
            st.subheader(f"Matching Accuracy: {score:.2f}%")
            st.image(cv2.drawMatches(img1, kp1, img2, kp2, good, None), use_container_width=True)

    elif choice == "AI Detection System":
        st.title("🤖 AI ANALYSIS SYSTEM")
        file = st.file_uploader("Scan Biometric Image", key="ai_check")
        if file:
            image = Image.open(file)
            st.image(image, caption="Current Scan", width=300)
            if st.button("EXECUTE DEEP SCAN"):
                with st.spinner('Analyzing...'):
                    img_array = np.array(image)
                    # Logic: Toggle based on image mean for demo variety
                    is_ai = img_array.mean() > 110 
                    
                    if is_ai:
                        st.warning("RESULT: AI GENERATED PATTERN")
                        st.divider()
                        st.subheader("RECONSTRUCTING TO REAL HUMAN DATA...")
                        # Small fixed size for the generated image
                        seed = random.randint(1, 1000)
                        st.image(f"https://thispersondoesnotexist.com?{seed}", caption="Reconstructed Human Profile", width=250)
                    else:
                        st.success("RESULT: REAL HUMAN BIOMETRIC")
                        st.info("No reconstruction needed for verified human data.")

                    signature = hashlib.sha256(img_array.tobytes()).hexdigest()
                    st.code(f"DIGITAL SIGNATURE: {signature}")

    if st.sidebar.button("LOGOUT"):
        st.session_state.login = False
        st.rerun()
