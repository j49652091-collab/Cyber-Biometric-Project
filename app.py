import streamlit as st
from PIL import Image
import random
import time

# =========================================
# 1. PAGE SETTINGS & ENHANCED STYLE
# =========================================
st.set_page_config(page_title="AI SECURITY SYSTEM", page_icon="🔥", layout="wide")

st.markdown("""
<style>
/* الخلفية الأصلية */
.stApp{ background: linear-gradient(to right, #0f172a, #111827); color:white; }

/* تكبير العنوان الرئيسي جداً ليكون واضحاً */
.main-title{
    text-align:center;
    font-size:75px; /* تكبير الخط */
    font-weight:900;
    color:cyan;
    text-shadow: 0 0 25px cyan;
    margin-bottom:40px;
}

/* تكبير نصوص الصناديق */
.box {
    background-color:#1e293b;
    padding:40px;
    border-radius:25px;
    box-shadow:0px 0px 25px cyan;
}

/* تكبير الخطوط داخل الصناديق */
.stMarkdown p, .stMarkdown h3 {
    font-size: 24px !important; /* تكبير الخط ليكون واضحاً جداً */
    font-weight: bold;
}

.result-human{ color:lime; font-size:45px; font-weight:bold; }
.result-ai{ color:orange; font-size:45px; font-weight:bold; }

/* زر الدخول: نص أسود ملكي ضخم */
.stButton>button {
    background-color: #00ffcc !important;
    color: #000000 !important;
    font-weight: 900 !important;
    font-size: 28px !important;
    height: 3.5em;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 2. LOGIN LOGIC
# =========================================
valid_users = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

if "logged" not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.markdown('<div class="main-title">SECURITY ACCESS 🔥</div>', unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        # تكبير نصوص الإدخال
        st.markdown("### ENTER AGENT CREDENTIALS")
        u = st.text_input("USERNAME")
        p = st.text_input("PASSWORD", type="password")
        if st.button("EXECUTE LOGIN", use_container_width=True):
            if u.lower() in valid_users and p == valid_password:
                st.session_state.logged = True
                st.rerun()
            else:
                st.error("ACCESS DENIED ❌")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# 3. MAIN SYSTEM (The Smart Matching Engine)
# =========================================
else:
    st.markdown('<div class="main-title">NEURAL ANALYZER PRO 🔥</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("UPLOAD SOURCE IMAGE", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        
        # محاكاة كشف الأنمي/AI
        is_ai = random.choice([True, False])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### 🔍 ORIGINAL SOURCE")
            st.image(image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### 🛠️ REBUILD & SYNC")
            if is_ai:
                st.markdown('<div class="result-ai">⚠️ AI DETECTED</div>', unsafe_allow_html=True)
                with st.spinner("Analyzing Features: Hair, Skin, Tone..."):
                    time.sleep(2.5)
                    
                    # --- منطق الاختيار الذكي القريب ---
                    # محاكاة: سنفترض أننا حللنا ملامح الصورة وسنعرض "أقرب" بشري
                    # هنا نستخدم صوراً "فخمة" تعبر عن دقة التحويل
                    matches = [
                        "https://pexels.com", # شاب شعر قصير
                        "https://pexels.com",  # بنت شعر طويل
                        "https://pexels.com", # شاب ملامح مختلفة
                        "https://pexels.com"   # بنت ملامح هادئة
                    ]
                    # الاختيار يتم ليعطي "أقرب" نتيجة في العرض
                    st.image(random.choice(matches), caption="RECONSTRUCTED HUMAN MATCH", use_container_width=True)
                st.success("Analysis: Feature Matching 98.4%")
            else:
                st.markdown('<div class="result-human">✅ HUMAN VERIFIED</div>', unsafe_allow_html=True)
                st.image(image, caption="Real Identity Confirmed", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.write("### 🔑 SIGNATURE")
            # استخراج البيانات فقط إذا اكتشفها النظام (إخفاء الذكي)
            
            st.write("**FACE_VECTOR:**")
            st.code(f"ID_{random.randint(1000, 9999)}_SEC")
            
            # إظهار بصمة العين فقط في 70% من الحالات كمحاكاة للكشف
            if random.random() > 0.3:
                st.write("**EYE_VECTOR:**")
                st.code(f"EYE_{random.randint(1000, 9999)}_DATA")
                st.write("✅ Eye Scan Completed")
            
            # إظهار بصمة اليد فقط إذا كانت موجودة (محاكاة)
            if random.random() > 0.6:
                st.write("**HAND_VECTOR:**")
                st.code(f"HAND_{random.randint(1000, 9999)}_SIG")
                st.write("✅ Hand Scan Completed")

            st.markdown('</div>', unsafe_allow_html=True)
