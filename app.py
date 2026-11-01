import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import base64
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(page_title="PalmIA - L'Excellence Agricole", page_icon="🌴", layout="wide")

# ==========================================
# 2. FONCTION POUR LA PHOTO DE FOND
# ==========================================
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# On vérifie si l'image est bien présente sur GitHub
if os.path.exists("oasis_bg.jpg"):
    bg_image = get_base64("oasis_bg.jpg")
    bg_css = f"background: linear-gradient(rgba(10, 25, 15, 0.7), rgba(10, 25, 15, 0.8)), url('data:image/jpeg;base64,{bg_image}') no-repeat center center fixed; background-size: cover;"
else:
    bg_css = "background: #0B1A10;"

# ==========================================
# 3. LE DESIGN LUXUEUX (CSS AVANCÉ)
# ==========================================
st.markdown(f"""
    <style>
    /* Importation de polices élégantes */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Masquer les éléments par défaut de Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Application de la photo de fond */
    .stApp {{
        {bg_css}
        font-family: 'Poppins', sans-serif;
    }}

    /* Conteneur principal style "Verre Dépoli" */
    .block-container {{
        background: rgba(15, 30, 20, 0.65); /* Vert très sombre transparent */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(212, 175, 55, 0.3); /* Bordure dorée */
        border-radius: 20px;
        padding: 3rem 4rem;
        margin-top: 3rem;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
    }}

    /* Titres */
    h1 {{
        color: #F5F5DC !important; /* Beige clair */
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem !important;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        margin-bottom: 0px;
    }}
    
    h2, h3, h4 {{
        color: #D4AF37 !important; /* Or */
        font-family: 'Playfair Display', serif;
        text-align: center;
    }}

    p, label {{
        color: #E0E0E0 !important;
        font-size: 1.1rem;
        text-align: center;
    }}

    /* Boutons Dorés */
    .stButton>button {{
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: #0B1A10 !important;
        border-radius: 50px;
        border: none;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        width: 100%;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.5);
        background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);
    }}

    /* Onglets (Tabs) personnalisés */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 15px;
        justify-content: center;
        margin-bottom: 30px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        height: 55px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 0 30px;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.3);
        font-weight: 600;
        transition: all 0.3s;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: #2E7D32 !important; /* Vert palmier */
        color: white !important;
        border: 1px solid #4CAF50;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
    }}

    /* Cartes pour l'Encyclopédie */
    .luxury-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }}
    
    .luxury-card:hover {{
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #D4AF37;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    
    .luxury-card h4 {{
        text-align: right;
        margin-bottom: 10px;
    }}
    
    .luxury-card p {{
        text-align: right;
        line-height: 1.8;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. CONTENU DU SITE
# ==========================================

# En-tête
st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h3>L'Intelligence Artificielle au Service de la Palmeraie Mauritanienne</h3>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Onglets
tab1, tab2, tab3 = st.tabs(["📸 Diagnostic Intelligent", "📚 Encyclopédie des Menaces", "ℹ️ À Propos"])

# --- ONGLET 1 : DIAGNOSTIC ---
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h4>Analysez votre palmier</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Glissez-déposez une image (JPG, PNG) pour un diagnostic instantané", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image analysée", use_column_width=True)
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("Lancer l'analyse de pointe"):
                with st.spinner("L'Intelligence Artificielle analyse votre image..."):
                    img = image.resize((224, 224))
                    img_array = np.array(img) / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    try:
                        @st.cache_resource
                        def load_model():
                            return tf.keras.models.load_model("modele_palmier_v1.h5")
                        
                        model = load_model()
                        prediction = model.predict(img_array)[0][0]
                        
                        st.write("<br>", unsafe_allow_html=True)
                        if prediction > 0.5:
                            st.error(f"⚠️ **RÉSULTAT : MALADE** (Confiance : {prediction*100:.2f}%)")
                        else:
                            st.success(f"✅ **RÉSULTAT : SAIN** (Confiance : {(1-prediction)*100:.2f}%)")
                    except Exception as e:
                        st.error(f"Erreur technique : {e}")

# --- ONGLET 2 : ENCYCLOPÉDIE ---
with tab2:
    categorie = st.radio("Sélectionnez une catégorie :", ["🦠 Les Maladies", "🐛 Les Ravageurs"], horizontal=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    if "Maladies" in categorie:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>Le Bayoud (Fusarium oxysporum)</h4>
                <p><b>Symptômes :</b> Décoloration des feuilles, dessèchement brutal d'un côté du palmier.</p>
                <p><b>Traitement :</b> Arrachage et brûlage du palmier infecté.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>L'Acariose</h4>
                <p><b>Symptômes :</b> Apparition de taches blanches sur les jeunes palmes.</p>
                <p><b>Traitement :</b> Utilisation d'acaricides spécifiques.</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>La Cochenille Blanche</h4>
                <p><b>Symptômes :</b> Amas blancs sur les palmes et les fruits.</p>
                <p><b>Traitement :</b> Taille des palmes infestées, traitements insecticides.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>Le Charançon Rouge</h4>
                <p><b>Symptômes :</b> Trous dans le tronc, sciure de bois.</p>
                <p><b>Traitement :</b> Injection dans le tronc, pièges à phéromones.</p>
            </div>
            """, unsafe_allow_html=True)

# --- ONGLET 3 : À PROPOS ---
with tab3:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="luxury-card">
            <h4>PalmIA - Projet d'Excellence</h4>
            <p>Cette plateforme a été développée dans le cadre du Master Phœniciculture & Intelligence Artificielle.</p>
            <p>Elle vise à aider les agriculteurs mauritaniens à protéger leurs oasis grâce aux nouvelles technologies.</p>
            <p><b>Partenaires :</b> Université de Nouakchott, USTHB, Laboratoire d'Atar.</p>
            <p>© 2027 - Tous droits réservés.</p>
        </div>
        """, unsafe_allow_html=True)
