import streamlit as st
from PIL import Image, ImageOps

# Configuration de la page
st.set_page_config(page_title="Portfolio - Awa Mboup", layout="wide")

# ===== TITRE =====
st.title("Awa Mboup")

# ===== DEUX COLONNES =====
col1, col2 = st.columns([1, 3])  # Colonne de droite plus large

# ===== COLONNE GAUCHE =====
with col1:
    # Image centrée et recadrée
   
    st.image("cv.jpg", width=200)

    # Coordonnées
    st.header("Coordonnées")
    st.write("📍 Dakar, Sénégal")
    st.write("📞 77 762 53 36")
    st.write("✉️ mboupawa43@gmail.com")

    # Langues
    st.header("Langues")
    st.write("- Français")
    st.write("- Portugais")

# ===== COLONNE DROITE =====
with col2:
    # Profil
    st.header("Profil")
    st.markdown("""
Je suis géographe et géomaticienne, avec un intérêt particulier pour la cartographie, les SIG et l’**aménagement du territoire**.  
Ma formation me permet d’analyser l’espace, de produire des cartes et d’utiliser des outils comme QGIS et ArcGIS pour la gestion et la visualisation des données spatiales.  

Je m’intéresse également à la création, à la communication et au travail bien fait, à travers des activités comme la lecture,le crochet, la danse et la cuisine, qui renforcent ma créativité, ma patience et mon sens de l’organisation.  
En parallèle, je développe un esprit entrepreneurial à travers mes activités professionnelles.
""")

    # Expériences et projets
    st.header("Expériences et projets")

    st.subheader("💡 Fondatrice & Créatrice – Rabaal-Ma (2023 – présent)")
    st.markdown("""
- Création et conception de vêtements en crochet  
- Gestion des commandes clients et relation client  
- Promotion des produits sur les réseaux sociaux  
- Animation d’une communauté sur TikTok
""")

    st.subheader("📊 Projets académiques en Géomatique (G15 / UCAD)")
    st.markdown("""
- Réalisation de cartes thématiques avec QGIS  
- Utilisation des systèmes de coordonnées (WGS 84 / UTM Zone 28N)  
- Géoréférencement d’images et de cartes  
- Analyse spatiale de données géographiques  
- Initiation aux bases de données spatiales
""")

    # Formations
    st.header("Formations")
    st.markdown("""
- Licence Géographie et Aménagement – UCAD  
- Formation en Géomatique – G15  
- Baccalauréat Sciences Humaines et Sociales
""")

    # Compétences
    st.header("Compétences")
    st.markdown("""
- SIG & Cartographie : QGIS, ArcGIS, Cartographie thématique, Analyse spatiale  
- Coordonnées : WGS 84 / UTM Zone 28N  
- Outils de productivité : Excel, Word, PowerPoint, Canva, conception vidéo
""")