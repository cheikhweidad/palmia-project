import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(page_title="PalmIA", page_icon="🌴", layout="wide")

st.title("🌴 PalmIA : Diagnostic Intelligent du Palmier Dattier")
st.markdown("**Bienvenue sur la plateforme d'aide au diagnostic pour les oasis mauritaniennes.**")
st.write("---")

tab1, tab2, tab3 = st.tabs(["📸 Diagnostic IA", "📚 Encyclopédie", "ℹ️ À propos"])

with tab1:
    st.header("Analysez votre palmier")
    st.write("Téléchargez une photo d'une palme ou d'un fruit pour identifier une maladie ou un ravageur.")
    
    uploaded_file = st.file_uploader("Choisir une image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image téléchargée", width=300)
        st.write("Analyse en cours...")
        
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
            st.subheader("Résultat :")
            if prediction > 0.5:
                st.error(f"⚠️ **MALADE** (Confiance : {prediction*100:.2f}%)")
            else:
                st.success(f"✅ **SAIN** (Confiance : {(1-prediction)*100:.2f}%)")
        except Exception as e:
            st.error(f"Erreur de chargement du modèle : {e}")

with tab2:
    st.header("Guide des Menaces")
    categorie = st.radio("Catégorie :", ["Maladies", "Ravageurs"], horizontal=True)
    if categorie == "Maladies":
        st.subheader("🦠 Les Maladies")
        st.write("**Le Bayoud :** Décoloration des feuilles, dessèchement.")
        st.write("**L'Acariose :** Taches blanches sur les jeunes palmes.")
    else:
        st.subheader("🐛 Les Ravageurs")
        st.write("**La Cochenille Blanche :** Amas blancs sur les palmes et les fruits.")
        st.write("**Le Charançon Rouge :** Trous dans le tronc, sciure de bois.")

with tab3:
    st.header("À propos")
    st.write("Projet Master Phœniciculture & IA - Université de Nouakchott.")
