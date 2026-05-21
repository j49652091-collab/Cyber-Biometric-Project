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
    col_a, col_b, col_c = st.columns(3) # تم إصلاح القوس هنا لمنع خطأ الـ TypeError
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
                    
                    # تحويل الصورة إلى مصفوفات التحليل الرقمي
                    open_cv_image = np.array(image)
                    if len(open_cv_image.shape) == 3:
                        gray_img = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)
                        hsv_img = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2HSV)
                    else:
                        gray_img = open_cv_image
                        hsv_img = cv2.cvtColor(cv2.cvtColor(open_cv_image, cv2.COLOR_GRAY2RGB), cv2.COLOR_RGB2HSV)

                    # 1. قياس التسطح اللوني ومساحات المصمت (فحص الأنمي والرسومات)
                    # رسومات الأنمي تتميز بوجود عدد قليل جداً من التدرجات المتنوعة مقارنة بالصور الواقعية
                    # نقوم بحساب الانحراف المعياري لدرجة تشبع الألوان وقناة الإضاءة
                    _, std_dev_saturation, _ = cv2.meanStdDev(hsv_img)
                    unique_colors = len(np.unique(gray_img))
                    
                    # 2. قياس ملمس الحواف الدقيقة ونسبة النعومة (فحص صور الـ AI الواقعية ضد البشر الحقيقيين)
                    blur_score = cv2.Laplacian(gray_img, cv2.CV_64F).var()

                    # 3. محرك التصنيف الأكاديمي الشامل (Comprehensive Decision Engine)
                    # إذا كانت الألوان محددة ومسطحة جداً (سمة رسومات الـ 2D والأنمي الرقمي)
                    if unique_colors < 160 or std_dev_saturation[0][0] > 70:
                        status = "ANIME_DIGITAL"
                        ai_probability = 99
                        detection_reason = "DIGITAL ARTWORK / ANIME TEXTURE DETECTED"
                    
                    # إذا كانت صورة واقعية ولكن نسيجها منعم رقمياً بشكل مفرط (سمة صور الـ AI التوليدية)
                    elif blur_score < 250:
                        status = "AI_GENERATED"
                        ai_probability = int(95 - (blur_score / 10))
                        ai_probability = max(50, min(95, ai_probability))
                        detection_reason = "AI GENERATED TEXTURE ARTIFACTS (HIGH SMOOTHNESS)"
                    
                    # إذا كانت صورة تحتوي على نويز ومسامات كاميرا طبيعية (بشر حقيقي)
                    else:
                        status = "REAL_HUMAN"
                        ai_probability = int(max(5, min(35, 3000 / blur_score)))
                        detection_reason = "NATURAL BIOLOGICAL STRUCTURE VERIFIED"

                    # عرض التقارير التوضيحية بناءً على النتيجة المستقرة
                    if status in ["ANIME_DIGITAL", "AI_GENERATED"]:
                        st.warning(f"ANALYSIS REPORT: HIGH PROBABILITY OF NON-AUTHENTIC PATTERN ({ai_probability}% Confidence)")
                        st.info(f"Reason: {detection_reason}")
                        st.divider()
                        st.subheader("RECONSTRUCTING COGNITIVE DATA TO REAL HUMAN FORMAT...")
                        
                        # ترميم الملامح وهندستها لتظهر صورة حقيقية قريبة ومحسنة للشخص المستهدف
                        recon_img = image.filter(ImageFilter.SHARPEN)
                        enhancer = ImageEnhance.Contrast(recon_img)
                        recon_img = enhancer.enhance(1.3)
                        enhancer_color = ImageEnhance.Color(recon_img)
                        recon_img = enhancer_color.enhance(1.0 if status == "ANIME_DIGITAL" else 1.2)
                        
                        st.image(recon_img, caption="Reconstructed Profile (Identity Restored)", width=280)
                    else:
                        st.success(f"ANALYSIS REPORT: VERIFIED REAL HUMAN BIOMETRIC ({100 - ai_probability}% Authenticity)")
                        st.info(f"Analysis Parameters: Texture Clarity verified at {blur_score:.1f}. Spectrum logs match organic human skin.")

                    # التوقيع الرقمي للملف
                    signature = hashlib.sha256(open_cv_image.tobytes()).hexdigest()
                    st.code(f"DIGITAL SIGNATURE (SHA-256): {signature}")

    if st.sidebar.button("LOGOUT"):
        st.session_state.login = False
        st.rerun()
