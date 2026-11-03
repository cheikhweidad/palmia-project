import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# ==========================================
# 1. CONFIGURATION ET DESIGN (Fond Vert)
# ==========================================
st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    .stApp { background-color: #1B4332; font-family: 'Poppins', sans-serif; }
    
    h1 { color: #F5F5DC !important; text-align: center; font-weight: bold;}
    h2, h3 { color: #D4AF37 !important; text-align: center; }
    p, label { color: #F5F5DC !important; }
    
    .stButton>button {
        background-color: #D4AF37; color: #1B4332 !important;
        border-radius: 30px; border: none; padding: 12px 30px;
        font-weight: 600; width: 100%;
    }
    .stButton>button:hover { background-color: #FFD700; }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.1); border-radius: 10px;
        color: #F5F5DC !important; padding: 10px 20px; font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #D4AF37 !important; color: #1B4332 !important;
    }
    
    .luxury-card {
        background: #F9F9F6; border-radius: 15px; padding: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        border-top: 5px solid #D4AF37; margin-bottom: 20px;
    }
    
    .luxury-card h4 { color: #1B4332 !important; text-align: right; margin-bottom: 15px; }
    .luxury-card p { color: #333 !important; text-align: right; line-height: 1.8; }
    
    /* Style pour le bouton de redirection */
    div.stButton > button:first-child { margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CONTENU DU SITE
# ==========================================
st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h3>Diagnostic Intelligent du Palmier Dattier</h3>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "📄 Documents & Ressources", "ℹ️ À propos"])

# --- ONGLET 1 : DIAGNOSTIC ---
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h3>Analysez votre palmier</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Glissez-déposez une image (JPG, PNG)", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Image analysée", use_column_width=True)
            
            if st.button("Lancer l'analyse de pointe"):
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
                        
                        st.write("---")
                        
                        # Simulation d'une prédiction de maladie spécifique
                        if prediction > 0.5:
                            # Pour l'exemple, on simule la détection du Bayoud
                            maladie_detectee = "Le Bayoud"
                            st.error(f"⚠️ **MALADIE DÉTECTÉE : {maladie_detectee}** (Confiance : {prediction*100:.2f}%)")
                            st.write("👉 Cliquez ci-dessous pour accéder directement à la fiche de traitement.")
                            
                            if st.button(f"Consulter la fiche : {maladie_detectee}"):
                                st.session_state['onglet_actif'] = 1 # Dirige vers l'onglet Encyclopédie
                                st.session_state['categorie'] = "🦠 Les Maladies"
                                st.rerun()
                                
                        else:
                            st.success(f"✅ **RÉSULTAT : SAIN** (Confiance : {(1-prediction)*100:.2f}%)")
                    except Exception as e:
                        st.error(f"Erreur de chargement du modèle : {e}")

# --- ONGLET 2 : ENCYCLOPÉDIE ---
with tab2:
    st.markdown("<h3>Guide des Menaces</h3>", unsafe_allow_html=True)
    
    # Gestion de la redirection depuis l'onglet 1
    default_index = 0
    if 'categorie' in st.session_state and st.session_state['categorie'] == "🦠 Les Maladies":
        default_index = 0
    
    categorie = st.radio("Sélectionnez une catégorie :", ["🦠 Les Maladies", "🐛 Les Ravageurs"], index=default_index, horizontal=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    if "Maladies" in categorie:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>Le Bayoud (Fusarium oxysporum)</h4>
                <p><b>Symptômes :</b> Décoloration des feuilles, dessèchement brutal d'un côté du palmier. Le tronc devient fragile.</p>
                <p><b>Traitement :</b> Arrachage et brûlage immédiat du palmier infecté pour éviter la propagation.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>L'Acariose</h4>
                <p><b>Symptômes :</b> Apparition de taches blanches sur les jeunes palmes, entraînant un dépérissement progressif.</p>
                <p><b>Traitement :</b> Utilisation d'acaricides spécifiques et taille des palmes atteintes.</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="luxury-card">
                <h4>La Cochenille Blanche</h4>
                <p><b>Symptômes :</b> Amas blancs cotonneux sur les palmes et les fruits, affaiblissant l'arbre.</p>
                <p><b>Traitement :</b> Taille sévère, traitements insecticides et lutte biologique.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="luxury-card">
                <h4>Le Charançon Rouge</h4>
                <p><b>Symptômes :</b> Trous dans le tronc, présence de sciure de bois, effondrement du palmier.</p>
                <p><b>Traitement :</b> Injection de produits dans le tronc, pièges à phéromones.</p>
            </div>
            """, unsafe_allow_html=True)

# --- ONGLET 3 : DOCUMENTS ---
with tab3:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h3>Documents & Ressources</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class="luxury-card">
            <p>Retrouvez ici les documents techniques et scientifiques relatifs à la phœniciculture et aux maladies du palmier dattier.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pour ajouter des documents : tu dois les uploader sur GitHub (dans le même dossier que app.py)
        # et mettre leur nom exact dans les liens ci-dessous.
        st.markdown("### 📄 Fiches Techniques")
        st.markdown("[📥 Télécharger la fiche technique sur le Bayoud](https://raw.githubusercontent.com/cheikhweidad/palmia-project/main/fiche_bayoud.pdf)")
        st.markdown("[📥 Télécharger le guide de traitement des ravageurs](https://raw.githubusercontent.com/cheikhweidad/palmia-project/main/guide_ravageurs.pdf)")
        
        st.write("---")
        st.info("💡 Pour ajouter un document, uploadez-le sur GitHub et ajoutez son lien dans le code.")

# --- ONGLET 4 : À PROPOS ---
with tab4:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="luxury-card">
            <h4>À propos de PalmIA</h4>
            <p><b>Statut :</b> Projet en cours de développement (Version Beta).</p>
            <p><b>Contexte :</b> Cette plateforme a été créée dans le cadre d'une collaboration internationale pour le développement et la protection des oasis.</p>
            <p><b>Partenaires :</b></p>
            <ul style="color: #333; text-align: right; list-style-type: none; padding: 0;">
                <li>Université de Nouakchott (Mauritanie)</li>
                <li>Université des Sciences et de la Technologie Houari Boumediene (USTHB, Algérie)</li>
            </ul>
            <p><b>Objectif :</b> Mettre l'Intelligence Artificielle au service des agriculteurs pour préserver le patrimoine phœnicicole.</p>
            <p>© 2027 - Tous droits réservés.</p>
        </div>
        """, unsafe_allow_html=True)
