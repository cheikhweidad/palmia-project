import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

# --- DESIGN (Sans image de fond pour éviter les bugs) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Fond vert sombre uni */
    .stApp {
        background-color: #0B1A10;
        font-family: 'Poppins', sans-serif;
    }

    h1 { color: #F5F5DC !important; font-family: 'Playfair Display', serif; font-size: 3.5rem !important; text-align: center; }
    h2, h3, h4 { color: #D4AF37 !important; font-family: 'Playfair Display', serif; text-align: center; }
    p, label { color: #E0E0E0 !important; font-size: 1.1rem; text-align: center; }

    /* Boutons Dorés */
    .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: #0B1A10 !important;
        border-radius: 50px; border: none; padding: 12px 30px; font-weight: 600; width: 100%;
    }
    
    /* Onglets */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        height: 55px; background-color: rgba(255, 255, 255, 0.05); border-radius: 30px;
        padding: 0 30px; color: #D4AF37 !important; border: 1px solid rgba(212, 175, 55, 0.3); font-weight: 600;
    }
    .stTabs [aria-selected="true"] { background-color: #2E7D32 !important; color: white !important; border: 1px solid #4CAF50; }

    /* Cartes */
    .luxury-card {
        background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 15px; padding: 25px; margin-bottom: 20px;
    }
    .luxury-card h4 { text-align: right; }
    .luxury-card p { text-align: right; }
    </style>
""", unsafe_allow_html=True)

# --- CONTENU ---
st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h3>L'Intelligence Artificielle au Service de la Palmeraie Mauritanienne</h3>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic Intelligent", "📚 Encyclopédie", "ℹ️ À Propos"])

with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        uploaded_file = st.file_uploader("Glissez-déposez une image (JPG, PNG)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image analysée", use_column_width=True)
            if st.button("Lancer l'analyse"):
                with st.spinner("Analyse en cours..."):
                    img = image.resize((224, 224))
                    img_array = np.array(img) / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    try:
                        @st.cache_resource
                        def load_model():
                            return tf.keras.models.load_model("modele_palmier_v1.h5")
                        model = load_model()
                        prediction = model.predict(img_array)[0][0]
                        if prediction > 0.5:
                            st.error(f"⚠️ **MALADE** (Confiance : {prediction*100:.2f}%)")
                        else:
                            st.success(f"✅ **SAIN** (Confiance : {(1-prediction)*100:.2f}%)")
                    except Exception as e:
                        st.error(f"Erreur : {e}")

with tab2:
    categorie = st.radio("Sélectionnez une catégorie :", ["🦠 Maladies", "🐛 Ravageurs"], horizontal=True)
    if "Maladies" in categorie:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""<div class="luxury-card"><h4>Le Bayoud</h4><p>Symptômes : Décoloration des feuilles.<br>Traitement : Arrachage.</p></div>""", unsafe_allow_html=True)
        with col_b:
            st.markdown("""<div class="luxury-card"><h4>L'Acariose</h4><p>Symptômes : Taches blanches.<br>Traitement : Acaricides.</p></div>""", unsafe_allow_html=True)
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""<div class="luxury-card"><h4>La Cochenille</h4><p>Symptômes : Amas blancs.<br>Traitement : Insecticides.</p></div>""", unsafe_allow_html=True)
        with col_b:
            st.markdown("""<div class="luxury-card"><h4>Le Charançon</h4><p>Symptômes : Trous dans le tronc.<br>Traitement : Pièges.</p></div>""", unsafe_allow_html=True)

with tab3:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""<div class="luxury-card"><h4>À Propos</h4><p>Master Phœniciculture & IA.<br>Université de Nouakchott.</p></div>""", unsafe_allow_html=True)
