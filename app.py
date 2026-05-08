import streamlit as st
from PIL import Image
import numpy as np
import hashlib
import random

st.set_page_config(
    page_title="Cyber Biometric",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color:#020617;
    color:white;
}
</style>
""", unsafe_allow_html=True)

USERNAME = "Ezz"
PASSWORD = "1234"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("🧠 CYBER BIOMETRIC LOGIN")

    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")

    if st.button("LOGIN"):

        if user == USERNAME and pw == PASSWORD:
            st.session_state.login = True
            st.rerun()

        else:
            st.error("Wrong Login")

else:

    st.title("AI HUMAN ANALYZER")

    file = st.file_uploader("Upload Image")

    if file:

        image = Image.open(file)

        st.image(image)

        result = random.choice([
            "AI GENERATED",
            "REAL HUMAN"
        ])

        st.subheader(result)

        img_array = np.array(image)

        signature = hashlib.sha256(
            img_array.tobytes()
        ).hexdigest()

        st.subheader("Digital Signature")

        st.code(signature)
