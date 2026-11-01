import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- CONFIGURATION ET DESIGN (CSS Avancé) ---
st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

st.markdown("""
    <style>
    /* Fond principal beige clair */
    .stApp { background-color: #FAFAFA; }
    
    /* Titres en vert palmier */
    h1, h2, h3 { color: #2E7D32 !important; }
    
    /* Boutons verts */
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #1B5E20; }
    
    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #F5F5DC;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        color: #2E7D32;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2E7D32;
        color: white;
    }
    
    /* Cartes personnalisées pour l'encyclopédie */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #2E7D32;
    }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE ---
st.title("🌴 PalmIA : Diagnostic Intelligent du Palmier Dattier")
st.markdown("**Bienvenue sur la plateforme d'aide au diagnostic pour les oasis mauritaniennes.**")
st.write("---")

# --- ONGLETS ---
tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie (Maladies & Ravageurs)", "ℹ️ À propos"])

# ==========================================
# ONGLET 1 : DIAGNOSTIC IA
# ==========================================
with tab1:
    st.header("Analysez votre palmier")
    st.write("Téléchargez une photo d'une palme ou d'un fruit pour identifier une maladie ou un ravageur.")
    
    uploaded_file = st.file_uploader("Choisir une image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image téléchargée", use_column_width=True)
        
        with col2:
            st.write("### Analyse en cours...")
            with st.spinner("L'Intelligence Artificielle analyse l'image..."):
                img = image.resize((224, 224))
                img_array = np.array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)
                
                try:
                    @st.cache_resource
                    def load_model():
                        return tf.keras.models.load_model("modele_palmier_v1.h5")
                    
                    model = load_model()
                    prediction = model.predict(img_array)[0][0]
                    
                    st.subheader("Résultat :")
                    if prediction > 0.5:
                        st.error(f"⚠️ **MALADE** (Confiance : {prediction*100:.2f}%)")
                    else:
                        st.success(f"✅ **SAIN** (Confiance : {(1-prediction)*100:.2f}%)")
                except Exception as e:
                    st.error(f"Erreur de chargement du modèle : {e}")

# ==========================================
# ONGLET 2 : ENCYCLOPÉDIE
# ==========================================
with tab2:
    st.header("Guide des Menaces du Palmier Dattier")
    categorie = st.radio("Catégorie :", ["Maladies", "Ravageurs"], horizontal=True)
    
    if categorie == "Maladies":
        st.subheader("🦠 Les Maladies")
        
        st.markdown("""
        <div class="card">
            <h4>Le Bayoud (Fusarium oxysporum)</h4>
            <p><b>Symptômes :</b> Décoloration des feuilles, dessèchement brutal d'un côté du palmier.</p>
            <p><b>Traitement :</b> Arrachage et brûlage du palmier infecté.</p>
        </div>
        <div class="card">
            <h4>L'Acariose</h4>
            <p><b>Symptômes :</b> Apparition de taches blanches sur les jeunes palmes.</p>
            <p><b>Traitement :</b> Utilisation d'acaricides spécifiques.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.subheader("🐛 Les Ravageurs")
        
        st.markdown("""
        <div class="card">
            <h4>La Cochenille Blanche (Parlatoria blanchardi)</h4>
            <p><b>Symptômes :</b> Amas blancs sur les palmes et les fruits.</p>
            <p><b>Traitement :</b> Taille des palmes infestées, traitements insecticides.</p>
        </div>
        <div class="card">
            <h4>Le Charançon Rouge</h4>
            <p><b>Symptômes :</b> Trous dans le tronc, sciure de bois.</p>
            <p><b>Traitement :</b> Injection dans le tronc, pièges à phéromones.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# ONGLET 3 : À PROPOS
# ==========================================
with tab3:
    st.header("À propos de PalmIA")
    st.write("Cette plateforme a été développée dans le cadre du Master Phœniciculture & Intelligence Artificielle.")
    st.write("**Partenaires :** Université de Nouakchott, USTHB, Laboratoire d'Atar.")
    st.write("© 2027 - Tous droits réservés.")
