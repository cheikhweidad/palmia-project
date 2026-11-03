
 palmia.ipynb
 palmia.ipynb_

[1]
0s
code_site = """
import streamlit as st

st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

st.title("🌴 PalmIA")
st.subheader("Plateforme de diagnostic du palmier dattier")

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "ℹ️ À propos"])

with tab1:
    st.header("Analysez votre palmier")
    st.write("Téléchargez une photo pour obtenir un diagnostic.")

with tab2:
    st.header("Guide des Menaces")
    categorie = st.radio("Catégorie :", ["Maladies", "Ravageurs"])
    if categorie == "Maladies":
        st.write("Le Bayoud, L'Acariose...")
    else:
        st.write("La Cochenille, Le Charançon...")

with tab3:
    st.header("À propos")
    st.write("Projet Master - Université de Nouakchott")
"""

with open("app.py", "w") as f:
    f.write(code_site)

print("✅ Fichier app.py créé sur Colab !")
✅ Fichier app.py créé sur Colab !

[2]
0s
print (code_site)

import streamlit as st

st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

st.title("🌴 PalmIA")
st.subheader("Plateforme de diagnostic du palmier dattier")

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "ℹ️ À propos"])

with tab1:
    st.header("Analysez votre palmier")
    st.write("Téléchargez une photo pour obtenir un diagnostic.")

with tab2:
    st.header("Guide des Menaces")
    categorie = st.radio("Catégorie :", ["Maladies", "Ravageurs"])
    if categorie == "Maladies":
        st.write("Le Bayoud, L'Acariose...")
    else:
        st.write("La Cochenille, Le Charançon...")

with tab3:
    st.header("À propos")
    st.write("Projet Master - Université de Nouakchott")


[4]
0s
code_luxe = """
import streamlit as st
import base64
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(page_title="PalmIA | L'Excellence Agricole", page_icon="🌴", layout="wide")

# ==========================================
# 2. DESIGN ULTRA-PREMIUM (CSS)
# ==========================================
st.markdown(\"\"\"
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Masquer les éléments Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Fond général */
    .stApp {
        background-color: #0B1A10;
        background-image: linear-gradient(rgba(10, 25, 15, 0.85), rgba(10, 25, 15, 0.95)), url('https://raw.githubusercontent.com/cheikhweidad/palmia-project/main/oasis_bg.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }

    /* Titres */
    h1 {
        color: #F5F5DC !important;
        font-family: 'Playfair Display', serif;
        font-size: 4rem !important;
        text-align: center;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.9);
        margin-bottom: 0px;
    }
    
    h2, h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        text-align: center;
    }

    p, label, .stMarkdown {
        color: #E0E0E0 !important;
        font-size: 1.1rem;
    }

    /* Boutons */
    .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: #0B1A10 !important;
        border-radius: 50px;
        border: none;
        padding: 15px 40px;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.4);
        background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);
    }

    /* Onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        margin-top: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 0 35px;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.3);
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2E7D32 !important;
        color: white !important;
        border: 1px solid #4CAF50;
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.6);
    }

    /* Cartes Fkhama */
    .luxury-card {
        background: rgba(20, 40, 30, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .luxury-card:hover {
        transform: translateY(-8px) scale(1.02);
        border: 1px solid #D4AF37;
        box-shadow: 0 20px 40px rgba(212, 175, 55, 0.2);
    }
    
    .luxury-card h4 {
        color: #D4AF37 !important;
        font-size: 1.6rem;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    .luxury-card p {
        text-align: right;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    </style>
\"\"\", unsafe_allow_html=True)

# ==========================================
# 3. CONTENU DU SITE
# ==========================================

st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h3>L'Intelligence Artificielle au Service de la Palmeraie Mauritanienne</h3>", unsafe_allow_html=True)
st.write("<br><br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "ℹ️ À Propos"])

# --- ONGLET 1 ---
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h3>Analysez votre palmier</h3>", unsafe_allow_html=True)
        st.markdown("<p>Glissez-déposez une image (JPG, PNG) pour un diagnostic instantané.</p>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            st.success("Image chargée avec succès ! L'IA est prête à analyser.")
            if st.button("Lancer l'analyse de pointe"):
                st.info("Analyse en cours... (Cette fonctionnalité sera bientôt connectée à votre modèle).")

# --- ONGLET 2 ---
with tab2:
    st.markdown("<h3>Guide des Menaces</h3>", unsafe_allow_html=True)
    categorie = st.radio("", ["🦠 Les Maladies", "🐛 Les Ravageurs"], horizontal=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    if "Maladies" in categorie:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(\"\"\"
            <div class="luxury-card">
                <h4>Le Bayoud (Fusarium oxysporum)</h4>
                <p><b>Symptômes :</b> Décoloration des feuilles, dessèchement brutal d'un côté du palmier. Le tronc devient fragile.</p>
                <p><b>Traitement :</b> Arrachage et brûlage immédiat du palmier infecté pour éviter la propagation.</p>
            </div>
            \"\"\", unsafe_allow_html=True)
        with col_b:
            st.markdown(\"\"\"
            <div class="luxury-card">
                <h4>L'Acariose</h4>
                <p><b>Symptômes :</b> Apparition de taches blanches sur les jeunes palmes, entraînant un dépérissement progressif.</p>
                <p><b>Traitement :</b> Utilisation d'acaricides spécifiques et taille des palmes atteintes.</p>
            </div>
            \"\"\", unsafe_allow_html=True)
            
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(\"\"\"
            <div class="luxury-card">
                <h4>La Cochenille Blanche</h4>
                <p><b>Symptômes :</b> Amas blancs cotonneux sur les palmes et les fruits, affaiblissant l'arbre.</p>
                <p><b>Traitement :</b> Taille sévère, traitements insecticides et lutte biologique.</p>
            </div>
            \"\"\", unsafe_allow_html=True)
        with col_b:
            st.markdown(\"\"\"
            <div class="luxury-card">
                <h4>Le Charançon Rouge</h4>
                <p><b>Symptômes :</b> Trous dans le tronc, présence de sciure de bois, effondrement du palmier.</p>
                <p><b>Traitement :</b> Injection de produits dans le tronc, pièges à phéromones.</p>
            </div>
            \"\"\", unsafe_allow_html=True)

# --- ONGLET 3 ---
with tab3:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(\"\"\"
        <div class="luxury-card">
            <h4>PalmIA - Projet d'Excellence</h4>
            <p>Cette plateforme a été développée dans le cadre du Master Phœniciculture & Intelligence Artificielle.</p>
            <p>Elle vise à aider les agriculteurs mauritaniens à protéger leurs oasis grâce aux nouvelles technologies.</p>
            <p><b>Partenaires :</b> Université de Nouakchott, USTHB, Laboratoire d'Atar.</p>
            <p>© 2027 - Tous droits réservés.</p>
        </div>
        \"\"\", unsafe_allow_html=True)
"""

with open("app.py", "w") as f:
    f.write(code_luxe)

print("✅ Code de luxe généré avec succès !")
✅ Code de luxe généré avec succès !

[5]
0s
print(code_luxe)

import streamlit as st
import base64
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(page_title="PalmIA | L'Excellence Agricole", page_icon="🌴", layout="wide")

# ==========================================
# 2. DESIGN ULTRA-PREMIUM (CSS)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Masquer les éléments Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Fond général */
    .stApp {
        background-color: #0B1A10;
        background-image: linear-gradient(rgba(10, 25, 15, 0.85), rgba(10, 25, 15, 0.95)), url('https://raw.githubusercontent.com/cheikhweidad/palmia-project/main/oasis_bg.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }

    /* Titres */
    h1 {
        color: #F5F5DC !important;
        font-family: 'Playfair Display', serif;
        font-size: 4rem !important;
        text-align: center;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.9);
        margin-bottom: 0px;
    }
    
    h2, h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        text-align: center;
    }

    p, label, .stMarkdown {
        color: #E0E0E0 !important;
        font-size: 1.1rem;
    }

    /* Boutons */
    .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: #0B1A10 !important;
        border-radius: 50px;
        border: none;
        padding: 15px 40px;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.4);
        background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);
    }

    /* Onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        margin-top: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 0 35px;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.3);
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2E7D32 !important;
        color: white !important;
        border: 1px solid #4CAF50;
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.6);
    }

    /* Cartes Fkhama */
    .luxury-card {
        background: rgba(20, 40, 30, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .luxury-card:hover {
        transform: translateY(-8px) scale(1.02);
        border: 1px solid #D4AF37;
        box-shadow: 0 20px 40px rgba(212, 175, 55, 0.2);
    }
    
    .luxury-card h4 {
        color: #D4AF37 !important;
        font-size: 1.6rem;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    .luxury-card p {
        text-align: right;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CONTENU DU SITE
# ==========================================

st.markdown("<h1>🌴 PalmIA</h1>", unsafe_allow_html=True)
st.markdown("<h3>L'Intelligence Artificielle au Service de la Palmeraie Mauritanienne</h3>", unsafe_allow_html=True)
st.write("<br><br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "ℹ️ À Propos"])

# --- ONGLET 1 ---
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h3>Analysez votre palmier</h3>", unsafe_allow_html=True)
        st.markdown("<p>Glissez-déposez une image (JPG, PNG) pour un diagnostic instantané.</p>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            st.success("Image chargée avec succès ! L'IA est prête à analyser.")
            if st.button("Lancer l'analyse de pointe"):
                st.info("Analyse en cours... (Cette fonctionnalité sera bientôt connectée à votre modèle).")

# --- ONGLET 2 ---
with tab2:
    st.markdown("<h3>Guide des Menaces</h3>", unsafe_allow_html=True)
    categorie = st.radio("", ["🦠 Les Maladies", "🐛 Les Ravageurs"], horizontal=True)
    
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

# --- ONGLET 3 ---
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

Colab paid products
-
Cancel contracts here
*values: object, , Prints the values to a stream, or to sys.stdout by default. sep &nbsp;&nbsp;string inserted between values, default a space. end &nbsp;&nbsp;string appended after the last value, default a newline. file &nbsp;&nbsp;a file-like object (stream); defaults to the current sys.stdout. flush &nbsp;&nbsp;whether to forcibly flush the stream., hint
