import streamlit as st
from PIL import Image
import numpy as np
import hashlib
import random
import face_recognition
import time

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI HUMAN ANALYZER",
    page_icon="🧠",
    layout="wide"
)

# =====================================================
# STYLING
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI';
    background-color: #020617;
    color: white;
}

.main {
    background: linear-gradient(135deg,#020617,#0f172a,#111827);
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    background: linear-gradient(90deg,#38bdf8,#818cf8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:30px;
}

.login-box {
    width:450px;
    margin:auto;
    padding:40px;
    border-radius:25px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    box-shadow: 0px 0px 40px rgba(56,189,248,0.3);
}

.stTextInput input {
    background-color:#111827;
    color:white;
    border-radius:10px;
    border:1px solid #334155;
}

.stButton button {
    width:100%;
    background: linear-gradient(90deg,#06b6d4,#6366f1);
    color:white;
    border:none;
    border-radius:12px;
    padding:15px;
    font-size:18px;
    font-weight:bold;
    transition:0.3s;
}

.stButton button:hover {
    transform:scale(1.03);
    box-shadow:0px 0px 20px rgba(99,102,241,0.5);
}

.result-box {
    padding:25px;
    border-radius:20px;
    background: rgba(255,255,255,0.05);
    margin-top:20px;
}

.hash-box {
    background:#111827;
    padding:15px;
    border-radius:15px;
    color:#38bdf8;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN DATA
# =====================================================

USERNAME = "Ezz"
PASSWORD = "1234"

if "logged" not in st.session_state:
    st.session_state.logged = False

# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged:

    st.markdown("<div class='title'>AI HUMAN ANALYZER</div>", unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.subheader("🔐 Secure Login")

    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")

    if st.button("LOGIN"):

        if user == USERNAME and pw == PASSWORD:
            st.session_state.logged = True
            st.success("ACCESS GRANTED ✅")
            time.sleep(1)
            st.rerun()
        else:
            st.error("INVALID USERNAME OR PASSWORD ❌")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# MAIN SYSTEM
# =====================================================

else:

    st.markdown("<div class='title'>AI IMAGE DETECTOR</div>", unsafe_allow_html=True)

    st.write("")

    uploaded = st.file_uploader(
        "📤 Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded:

        image = Image.open(uploaded)

        col1, col2 = st.columns([1,1])

        with col1:

            st.image(image, caption="Uploaded Image", use_container_width=True)

        with col2:

            st.markdown("<div class='result-box'>", unsafe_allow_html=True)

            st.subheader("🧠 AI ANALYSIS")

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            # =====================================================
            # RANDOM DETECTION FOR DEMO
            # =====================================================

            result = random.choice([
                "AI GENERATED",
                "REAL HUMAN"
            ])

            confidence = random.randint(91, 99)

            if result == "AI GENERATED":

                st.warning(f"⚠️ RESULT: {result}")
                st.info(f"CONFIDENCE: {confidence}%")

                st.image(
                    image,
                    caption="Generated Realistic Match",
                    use_container_width=True
                )

            else:

                st.success(f"✅ RESULT: {result}")
                st.info(f"CONFIDENCE: {confidence}%")

            # =====================================================
            # DIGITAL VISUAL SIGNATURE
            # =====================================================

            img_array = np.array(image)

            visual_signature = hashlib.sha256(
                img_array.tobytes()
            ).hexdigest()

            st.write("")
            st.subheader("🔐 DIGITAL VISUAL SIGNATURE")

            st.markdown(
                f"<div class='hash-box'>{visual_signature}</div>",
                unsafe_allow_html=True
            )

            # =====================================================
            # FACE VECTOR SIGNATURE
            # =====================================================

            try:

                face_locations = face_recognition.face_locations(img_array)

                encodings = face_recognition.face_encodings(img_array)

                if len(encodings) > 0:

                    face_vector = encodings[0]

                    face_signature = hashlib.sha256(
                        face_vector.tobytes()
                    ).hexdigest()

                    st.write("")
                    st.subheader("🧬 FACE VECTOR SIGNATURE")

                    st.markdown(
                        f"<div class='hash-box'>{face_signature}</div>",
                        unsafe_allow_html=True
                    )

                    st.success("FACE DETECTED SUCCESSFULLY ✅")

                else:

                    st.error("NO FACE DETECTED ❌")

            except:

                st.error("FACE ANALYSIS FAILED ❌")

            st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("LOGOUT"):
        st.session_state.logged = False
        st.rerun()
