import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import base64

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(page_title="PalmIA - منصة النخيل الذكية", page_icon="🌴", layout="wide")

# ==========================================
# 2. دالة لجلب الصورة كخلفية (Base64)
# ==========================================
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# تأكد أن اسم الصورة يطابق ما رفعته في GitHub
try:
    bg_image = get_base64("oasis_bg.jpg")
    bg_css = f"background-image: url('data:image/jpeg;base64,{bg_image}');"
except:
    # في حال لم يتم رفع الصورة، سيستخدم لون أخضر داكن فخم
    bg_css = "background-color: #0B1A10;"

# ==========================================
# 3. التصميم الفخم (CSS متقدم جداً)
# ==========================================
st.markdown(f"""
    <style>
    /* استيراد خطوط عربية وإنجليزية فخمة */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Poppins:wght@300;600&display=swap');

    /* إخفاء عناصر Streamlit الافتراضية لمظهر موقع حقيقي */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* الخلفية العظيمة */
    .stApp {{
        {bg_css}
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Cairo', sans-serif;
    }}

    /* حاوية المحتوى الرئيسي (تأثير زجاجي داكن) */
    .block-container {{
        background: rgba(10, 25, 15, 0.75); /* لون أخضر داكن شفاف */
        backdrop-filter: blur(12px); /* تأثير الزجاج */
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3); /* إطار ذهبي خفيف */
        padding: 3rem 4rem;
        margin-top: 2rem;
        box-shadow: 0 25px 50px 0 rgba(0, 0, 0, 0.5);
    }}

    /* تنسيق العناوين */
    h1, h2, h3 {{
        color: #F5F5DC !important; /* لون بيج فخم */
        font-family: 'Cairo', sans-serif;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }}
    
    h1 {{
        font-weight: 900;
        font-size: 3.5rem !important;
        margin-bottom: 0px;
    }}
    
    h2 {{ font-weight: 700; color: #D4AF37 !important; }} /* ذهبي */
    h3 {{ font-weight: 400; font-size: 1.2rem !important; color: #E0E0E0 !important; }}

    /* تنسيق النصوص */
    p, label, .stMarkdown {{
        color: #E0E0E0 !important;
        font-size: 1.1rem;
        text-align: center;
    }}

    /* تنسيق الأزرار الفخمة */
    .stButton>button {{
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); /* تدرج ذهبي */
        color: #0B1A10 !important;
        border-radius: 50px;
        border: none;
        padding: 15px 40px;
        font-weight: 900;
        font-family: 'Cairo', sans-serif;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        width: 100%;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.4);
        background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);
    }}

    /* تنسيق التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 20px;
        background-color: transparent;
        justify-content: center;
        margin-top: 20px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        height: 60px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 50px;
        padding: 0 30px;
        color: #D4AF37 !important; /* ذهبي */
        font-weight: 700;
        border: 1px solid rgba(212, 175, 55, 0.3);
        transition: all 0.3s;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: #2E7D32 !important; /* أخضر نخيلي */
        color: white !important;
        border: 1px solid #2E7D32;
        box-shadow: 0 0 15px rgba(46, 125, 50, 0.5);
    }}

    /* تصميم البطاقات (Cards) */
    .luxury-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }}
    
    .luxury-card:hover {{
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #D4AF37;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    
    .luxury-card h4 {{
        color: #D4AF37 !important; /* ذهبي */
        font-size: 1.5rem;
        margin-bottom: 15px;
    }}
    
    .luxury-card p {{
        text-align: right; /* محاذاة النص العربي لليمين */
        line-height: 1.8;
    }}
    
    /* تنسيق منطقة رفع الصور */
    .stFileUploader {{
        background: rgba(255, 255, 255, 0.05);
        border: 2px dashed #D4AF37;
        border-radius: 15px;
        padding: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. محتوى الصفحة
# ==========================================

# العنوان الرئيسي (مثل الصور)
st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h2>نظام التشخيص الذكي لنخيل التمر</h2>", unsafe_allow_html=True)
st.markdown("<h3>احمِ واحتك بفضل قوة الذكاء الاصطناعي في موريتانيا</h3>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# التبويبات
tab1, tab2, tab3 = st.tabs(["📸 التشخيص بالذكاء الاصطناعي", "📚 موسوعة الأمراض والآفات", "ℹ️ عن المنصة"])

# --- التبويب 1: التشخيص ---
with tab1:
    st.write("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        uploaded_file = st.file_uploader("قم برفع صورة لسعفة أو ثمرة للبدء في التحليل...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="الصورة المرفوعة", use_column_width=True)
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("بدء التحليل الذكي"):
                with st.spinner("جاري تحليل الصورة بواسطة الذكاء الاصطناعي..."):
                    img = image.resize((224, 224))
                    img_array = np.array(img) / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    try:
                        @st.cache_resource
                        def load_model():
                            return tf.keras.models.load_model("modele_palmier_v1.h5")
                        
                        model = load_model()
                        prediction = model.predict(img_array)[0][0]
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        if prediction > 0.5:
                            st.error(f"⚠️ **النخلة مصابة (Malade)** - نسبة الثقة: {prediction*100:.2f}%")
                        else:
                            st.success(f"✅ **النخلة سليمة (Saine)** - نسبة الثقة: {(1-prediction)*100:.2f}%")
                    except Exception as e:
                        st.error(f"خطأ في تحميل النموذج: {e}")

# --- التبويب 2: الموسوعة ---
with tab2:
    st.write("<br>", unsafe_allow_html=True)
    categorie = st.radio("اختر الفئة:", ["الأمراض (Maladies)", "الآفات (Ravageurs)"], horizontal=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    
    if "الأمراض" in categorie:
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>مرض البيوض (Bayoud)</h4>
                <p><b>الأعراض:</b> اصفرار وذبول السعف من جهة واحدة، وجفاف النخلة بشكل مفاجئ.</p>
                <p><b>العلاج:</b> قلع النخلة المصابة وحرقها، وتعقيم التربة المحيطة.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>الأكاروز (Acariose)</h4>
                <p><b>الأعراض:</b> ظهور بقع بيضاء دقيقة على السعف الفتي، مما يؤدي إلى تشوهه.</p>
                <p><b>العلاج:</b> استخدام المبيدات الأكاروسية المتخصصة والرش الدوري.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>حشرة النخيل القشرية البيضاء (Cochenille)</h4>
                <p><b>الأعراض:</b> كتل بيضاء قطنية على السعف والثمار، وضعف عام في النخلة.</p>
                <p><b>العلاج:</b> تقليم السعف المصاب، واستخدام المبيدات الحشرية أو المكافحة الحيوية.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>سوسة النخيل الحمراء (Charançon)</h4>
                <p><b>الأعراض:</b> ثقوب في جذع النخلة، خروج نشارة خشبية، وسقوط النخلة.</p>
                <p><b>العلاج:</b> الحقن في الجذع، واستخدام مصائد الفيرمونات.</p>
            </div>
            """, unsafe_allow_html=True)

# --- التبويب 3: عن المنصة ---
with tab3:
    st.write("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="luxury-card">
            <h4>PalmIA - مشروع التخرج</h4>
            <p>تم تطوير هذه المنصة في إطار ماستر النخيل والذكاء الاصطناعي.</p>
            <p>تهدف المنصة إلى مساعدة المزارعين الموريتانيين على حماية واحاتهم باستخدام أحدث التقنيات.</p>
            <p><b>الشركاء:</b> جامعة نواكشوط، USTHB، ومختبر أطار.</p>
            <p>© 2027 - جميع الحقوق محفوظة.</p>
        </div>
        """, unsafe_allow_html=True)
