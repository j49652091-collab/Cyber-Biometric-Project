import streamlit as st
import cv2
import numpy as np

# إعداد واجهة التطبيق
st.set_page_config(page_title="نظام مطابقة البصمات", page_icon="🕵️‍♂️")

def match_fingerprints(img1, img2):
    # تحويل الصور إلى تدرج الرمادي (Gray Scale)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # استخدام خوارزمية SIFT لاستخراج الميزات
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)
    
    # استخدام مطابقة الميزات (BFMatcher)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    
    # تصفية النقاط المتطابقة بناءً على اختبار نسبة "لو"
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
            
    # حساب نسبة التشابه
    score = (len(good_matches) / min(len(kp1), len(kp2))) * 100
    
    # رسم خطوط التشابه بين البصمتين
    result_img = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    return score, result_img

# تصميم واجهة المستخدم
st.title("🔍 نظام التحقق من بصمة الإصبع")
st.info("قم برفع صورتين للبصمة للمقارنة بينهما وتحليل نقاط التشابه")

col1, col2 = st.columns(2)
with col1:
    file1 = st.file_uploader("البصمة المرجعية", type=['jpg', 'png', 'jpeg'])
with col2:
    file2 = st.file_uploader("البصمة المراد فحصها", type=['jpg', 'png', 'jpeg'])

if file1 and file2:
    # قراءة ومعالجة الصور المرفوعة
    img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), 1)
    img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), 1)
    
    if st.button("بدء عملية المطابقة"):
        score, result_img = match_fingerprints(img1, img2)
        
        st.write("---")
        st.subheader(f"نسبة التشابه: {score:.2f}%")
        
        if score > 18: # حد التشابه (Threshold)
            st.success("✅ النتيجة: البصمتان متطابقتان!")
        else:
            st.error("❌ النتيجة: البصمتان غير متطابقتين.")
            
        # عرض صورة المقارنة
        st.image(result_img, caption="توضيح النقاط المتقابلة بين البصمتين", use_container_width=True)

st.sidebar.markdown("""
### حول التطبيق:
هذا التطبيق يستخدم معالجة الصور الرقمية (OpenCV) وخوارزمية **SIFT** لمقارنة الأنماط الفريدة في بصمات الأصابع.
""")
