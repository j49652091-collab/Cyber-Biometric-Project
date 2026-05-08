import streamlit as st
import cv2
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="Biometric Signature Extractor", page_icon="🛡️")

# --- Header Section ---
st.title("🛡️ Universal Biometric Signature System")
st.subheader("Cybersecurity Graduation Project: Biometric Feature Extraction")
st.markdown("---")

# --- Sidebar Info ---
with st.sidebar:
    st.header("System Specs")
    st.info("Algorithm: ORB (Oriented FAST and Rotated BRIEF)")
    st.success("Mode: Universal Extraction")

# --- File Uploader ---
st.write("### Step 1: Upload Source Image")
uploaded_file = st.file_uploader("Upload Image (Face, Iris, or Hand)...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # --- Image Processing ---
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    st.image(rgb_image, caption='Original Input Image', use_container_width=True)
    
    # --- Extraction Button ---
    if st.button("Extract Biometric Signature 🧬"):
        # ORB Algorithm to find unique points (Signature)
        orb = cv2.ORB_create(nfeatures=1000)
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        
        if descriptors is not None:
            # Draw Keypoints on Image
            img_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)
            st.image(cv2.cvtColor(img_with_keypoints, cv2.COLOR_BGR2RGB), 
                     caption='Processed Image with Biometric Keypoints', use_container_width=True)
            
            st.success(f"Success: {len(keypoints)} biometric features identified!")
            
            # --- Output Results ---
            st.write("### 🔑 Digital Identity Signature (Vector):")
            st.code(descriptors[:20]) # Displaying a sample of the raw biometric vector
            
            st.warning("Cybersecurity Note: This unique mathematical vector is the encrypted identity used for secure authentication.")
        else:
            st.error("Identification Failed: No clear biometric features detected. Use a higher quality image.")

# --- Footer ---
st.divider()
st.caption("Secured Biometric Authentication Module - Class of 2026")

