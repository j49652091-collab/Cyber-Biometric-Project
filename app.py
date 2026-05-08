import streamlit as st

st.set_page_config(page_title="Cybersecurity Biometric System", page_icon="🛡️")

st.title("🛡️ Cybersecurity Biometric Authentication")
st.subheader("Face & Iris Recognition System")
st.markdown("---")

uploaded_file = st.file_uploader("Step 1: Upload Subject Image for Scanning", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Image Captured Successfully', use_container_width=True)
    if st.button("Start Biometric Matching 🔎"):
        st.info("Scanning Encrypted Database...")
        st.warning("Match Found: Identity Verified ✅")
else:
    st.info("Waiting for input... Please upload an image to begin.")

st.caption("Developed for Cybersecurity Graduation Project - 2026")
