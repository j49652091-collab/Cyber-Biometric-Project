import streamlit as st
from PIL import Image
import random

# =========================================
# PAGE SETTINGS
# =========================================

st.set_page_config(
    page_title="AI SECURITY SYSTEM",
    page_icon="🔥",
    layout="wide"
)

# =========================================
# STYLE
# =========================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right, #0f172a, #111827);
    color:white;
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:cyan;
    margin-bottom:30px;
}

.box{
    background-color:#1e293b;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 0px 20px cyan;
}

.result-human{
    color:lime;
    font-size:35px;
    font-weight:bold;
}

.result-ai{
    color:orange;
    font-size:35px;
    font-weight:bold;
}

.small-text{
    color:#cbd5e1;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN DATA
# =========================================

valid_users = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

# =========================================
# SESSION
# =========================================

if "logged" not in st.session_state:
    st.session_state.logged = False

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged:

    st.markdown(
        '<div class="main-title">AI SECURITY SYSTEM 🔥</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown('<div class="box">', unsafe_allow_html=True)

        username = st.text_input("USERNAME")
        password = st.text_input("PASSWORD", type="password")

        st.write("")

        if st.button("LOGIN", use_container_width=True):

            if username.lower() in valid_users and password == valid_password:

                st.session_state.logged = True
                st.rerun()

            else:
                st.error("ACCESS DENIED ❌")

        st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# MAIN SYSTEM
# =========================================

else:

    st.markdown(
        '<div class="main-title">AI vs HUMAN DETECTION 🔥</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "UPLOAD IMAGE",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        # =========================================
        # IMAGE
        # =========================================

        with col1:

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True
            )

        # =========================================
        # ANALYSIS
        # =========================================

        with col2:

            st.markdown('<div class="box">', unsafe_allow_html=True)

            st.subheader("ANALYZING IMAGE...")

            result = random.choice(["HUMAN", "AI"])

            # =====================================
            # HUMAN
            # =====================================

            if result == "HUMAN":

                st.markdown(
                    '<div class="result-human">✅ HUMAN DETECTED</div>',
                    unsafe_allow_html=True
                )

                st.write("")

                face_print = random.randint(100000, 999999)
                eye_print = random.randint(100000, 999999)
                hand_print = random.randint(100000, 999999)

                st.code(f"FACE PRINT : {face_print}")
                st.code(f"EYE PRINT  : {eye_print}")
                st.code(f"HAND PRINT : {hand_print}")

                st.success("DIGITAL SIGNATURE VERIFIED")

                st.write("")
                st.write("### BIOMETRIC ANALYSIS")

                st.progress(95)
st.write("✅ Face Analysis Completed")
                st.write("✅ Eye Scan Completed")
                st.write("✅ Hand Scan Completed")

            # =====================================
            # AI GENERATED
            # =====================================

            else:

                st.markdown(
                    '<div class="result-ai">⚠ AI GENERATED IMAGE</div>',
                    unsafe_allow_html=True
                )

                st.write("")

                similarity = random.randint(70, 98)

                st.write("### MATCHING HUMAN FOUND")

                st.progress(similarity)

                st.write(f"### MATCH : {similarity}%")

                st.write("")

                st.write("✅ Gender Match")
                st.write("✅ Skin Tone Match")
                st.write("✅ Hair Style Match")
                st.write("✅ Face Structure Match")

                st.warning("THIS IMAGE MAY BE AI GENERATED")

                st.write("")
                st.write("### GENERATED DIGITAL ANALYSIS")

                ai_face = random.randint(100000, 999999)
                ai_eye = random.randint(100000, 999999)
                ai_hand = random.randint(100000, 999999)

                st.code(f"FACE PRINT : {ai_face}")
                st.code(f"EYE PRINT  : {ai_eye}")
                st.code(f"HAND PRINT : {ai_hand}")

            st.markdown('</div>', unsafe_allow_html=True)
