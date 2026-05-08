import streamlit as st
import cv2
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="نظام مطابقة البصمات", layout="centered")

def match_fingerprints(img1, img2):
    # 1. تحويل الصور إلى الرمادي لسهولة المعالجة
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # 2. إنشاء مستخرج الميزات (SIFT)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)
    
    # 3. البحث عن التطابقات باستخدام FLANN (أسرع للمطابقة)
    index_params = dict(algorithm=1, trees=10)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    
    # 4. اختيار التطابقات الجيدة فقط (اختبار نسبة "لو")
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
            
    # 5. حساب النسبة المئوية للتشابه
    score = (len(good_matches) / min(len(kp1), len(kp2))) * 100
    
    # رسم خطوط التطابق بين الصورتين
    result_img = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    return score, result_img

# --- واجهة المستخدم (Streamlit) ---
st.title("🔍 نظام التحقق من بصمة الإصبع")
st.write("ارفع صورتين للبصمة لمقارنتهما برمجياً")

uploaded_file1 = st.file_uploader("البصمة الأولى (المرجع)", type=["jpg", "png", "bmp"])
uploaded_file2 = st.file_uploader("البصمة الثانية (للفحص)", type=["jpg", "png", "bmp"])

if uploaded_file1 and uploaded_file2:
    # تحويل الملفات المرفوعة إلى تنسيق OpenCV
    img1 = cv2.imdecode(np.frombuffer(uploaded_file1.read(), np.uint8), 1)
    img2 = cv2.imdecode(np.frombuffer(uploaded_file2.read(), np.uint8), 1)

    if st.button("تحليل ومطابقة"):
        with st.spinner('جاري التحليل...'):
            score, result_img = match_fingerprints(img1, img2)
            
            st.divider()
            st.subheader(f"نسبة التشابه: {score:.2f}%")
            
            if score > 20: # عتبة النجاح (يمكن تعديلها)
                st.success("✅ النتيجة: البصمتان متطابقتان")
            else:
                st.error("❌ النتيجة: البصمتان غير متطابقتين")
            
            # عرض الصورة الناتجة التي توضح نقاط الربط
            st.image(result_img, caption="توضيح نقاط التشابه المكتشفة بين البصمتين", use_container_width=True)
