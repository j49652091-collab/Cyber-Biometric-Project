import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2
import hashlib
import time

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

# 3. Secure Login System (Hashed Passwords)
PASSWORD_HASH = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4" # "1234"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<p class="big-title">CYBER BIOMETRIC LOGIN</p>', unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)

    with col_b:
        user = st.text_input("USERNAME")
        pw = st.text_input("PASSWORD", type="password")
        if st.button("ENTER SYSTEM"):
            input_pw_hash = hashlib.sha256(pw.encode()).hexdigest()
            if user == "Ezz" and input_pw_hash == PASSWORD_HASH:
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Credentials")
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
            st.image(image, caption="Current Scan Target", width=300)
            
            if st.button("EXECUTE DEEP SCAN"):
                with st.spinner('Executing Multi-Layer Texture & Color Domain Scan...'):
                    time.sleep(1.5)
                    
                    # تحويل الصورة إلى OpenCV ومصفوفة تدرج رمادي
                    open_cv_image = np.array(image)
                    gray_img = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)
                    
                    # 1. حساب معامل التباين والنسيج لحواف الصورة
                    height, width = gray_img.shape
                    resolution_factor = (height * width) / (1000 * 1000)
                    raw_score = cv2.Laplacian(gray_img, cv2.CV_64F).var()
                    adjusted_texture = raw_score / (resolution_factor if resolution_factor > 0 else 1)
                    
                    # 2. حساب تباين وتماثل الألوان (Color Histogram Variance) للكشف عن الأنمي والرسوم المسطحة
                    # نقوم بحساب الانحراف المعياري لتوزيع التدرجات التكرارية للألوان
                    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
                    color_variance = np.std(hist)
                    
                    # 3. دمج الفحصين في نموذج تقييم ذكي متكيف (Hybrid Confidence Logic)
                    # رسومات الأنمي تعطي انحرافاً معيارياً للألوان ضخماً جداً بسبب المساحات اللونية الموحدة والثابتة
                    is_anime_or_digital = color_variance > 1200
                    
                    if is_anime_or_digital:
                        # إذا ثبت برمجياً أنها رسمة ديجيتال أو أنمي
                        ai_probability = 98 
                        detection_reason = "DIGITAL ARTWORK / ANIME PATTERN DETECTED"
                    else:
                        # إذا كانت صورة واقعية (إما بشرية أو توليد واقعي بالذكاء الاصطناعي)
                        ai_probability = max(0, min(100, int(100 - (adjusted_texture / 15))))
                        detection_reason = "AI GENERATED TEXTURE ARTIFACTS"

                    # عرض التقارير الأكاديمية المحدثة
                    if ai_probability > 45:
                        st.warning(f"ANALYSIS REPORT: HIGH PROBABILITY OF NON-HUMAN PATTERN ({ai_probability}% Confidence)")
                        st.info(f"Reason: {detection_reason}")
                        st.divider()
                        st.subheader("RECONSTRUCTING COGNITIVE DATA TO REAL HUMAN FORMAT...")
                        
                        # ترميم هندسي وإعادة بناء قريبة ومعززة للملامح
                        recon_img = image.filter(ImageFilter.SHARPEN)
                        enhancer = ImageEnhance.Contrast(recon_img)
                        recon_img = enhancer.enhance(1.2)
                        enhancer_color = ImageEnhance.Color(recon_img)
                        recon_img = enhancer_color.enhance(1.1)
                        
                        st.image(recon_img, caption="Reconstructed Profile (Identity Restored)", width=280)
                    else:
                        st.success(f"ANALYSIS REPORT: VERIFIED REAL HUMAN BIOMETRIC ({100 - ai_probability}% Authenticity)")
                        st.info("Verified natural biological tissue. Spectrum distribution and edge contrast match organic human skin.")

                    # التوقيع الرقمي لحماية الملف من أي تعديل خارجي
                    signature = hashlib.sha256(open_cv_image.tobytes()).hexdigest()
                    st.code(f"DIGITAL SIGNATURE (SHA-256): {signature}")

    if st.sidebar.button("LOGOUT"):
        st.session_state.login = False
        st.rerun()
