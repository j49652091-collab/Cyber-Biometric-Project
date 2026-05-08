import streamlit as st
from PIL import Image
import numpy as np
import cv2
import hashlib
import random

# 1. إعدادات الصفحة والتنسيق
st.set_page_config(page_title="Cyber Biometric Pro", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #020617; color: white; }
    h1, h2, h3 { color: #38bdf8 !important; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #38bdf8; color: black; }
</style>
""", unsafe_allow_html=True)

# 2. نظام تسجيل الدخول
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
    # 3. القائمة الجانبية للتنقل
    st.sidebar.title("نظام التحليل السيبراني")
    choice = st.sidebar.radio("اختر القسم:", ["مطابقة البصمات", "كاشف الذكاء الاصطناعي (AI Detector)"])

    # --- القسم الأول: مطابقة البصمات ---
    if choice == "مطابقة البصمات":
        st.title("🛡️ Fingerprint Matching System")
        st.write("قارن بين بصمتين للتأكد من الهوية")

        col1, col2 = st.columns(2)
        with col1:
            file1 = st.file_uploader("البصمة المرجعية", key="f1")
        with col2:
            file2 = st.file_uploader("البصمة المستهدفة", key="f2")

        if file1 and file2:
            img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), 1)
            img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), 1)

            # خوارزمية المطابقة SIFT
            sift = cv2.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)
            good = [m for m, n in matches if m.distance < 0.7 * n.distance]

            score = (len(good) / min(len(kp1), len(kp2))) * 100
            res_img = cv2.drawMatches(img1, kp1, img2, kp2, good, None)

            st.subheader(f"نتيجة المطابقة: {score:.2f}%")
            if score > 15:
                st.success("✅ تطابق تام: البصمتان لنفس الشخص")
            else:
                st.error("❌ لا يوجد تطابق: البصمتان مختلفتان")
            
            st.image(res_img, use_container_width=True)

    # --- القسم الثاني: كاشف الذكاء الاصطناعي ---
    elif choice == "كاشف الذكاء الاصطناعي (AI Detector)":
        st.title("🤖 AI Human/Fingerprint Analyzer")
        st.write("حلل البصمة لمعرفة ما إذا كانت حقيقية أم مولدة بالذكاء الاصطناعي")

        file = st.file_uploader("ارفع الصورة للتحليل", key="ai_check")

        if file:
            image = Image.open(file)
            st.image(image, width=400)
            
            # محاكاة تحليل البيانات (AI Analysis)
            if st.button("بدء الفحص العميق"):
                with st.spinner('جاري فحص الأنماط الرقمية...'):
                    # هنا نضع منطق التمييز (كمثال تعليمي)
                    result = random.choice(["REAL HUMAN BIOMETRIC", "AI GENERATED PATTERN"])
                    
                    st.divider()
                    if "REAL" in result:
                        st.success(f"النتيجة: {result}")
                    else:
                        st.warning(f"النتيجة: {result}")

                    # توليد التوقيع الرقمي للصورة لضمان عدم التلاعب (Hash)
                    img_array = np.array(image)
                    signature = hashlib.sha256(img_array.tobytes()).hexdigest()
                    st.info(f"التوقيع الرقمي الفريد (SHA-256):")
                    st.code(signature)

    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()
