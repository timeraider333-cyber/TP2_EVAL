# TP2 - Application Streamlit pour la visualisation de données
# Auteur : à compléter
# Lien de la page web publiée : à compléter après déploiement

# ============================================================
# Etape 3 : Chargement des librairies
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# Titre de l'application
# ============================================================
st.title("TP2 : Visualisation de données")
st.write("Application Streamlit pour explorer des données CSV en 2D ou 3D.")

# ============================================================
# Etape 4 : Demander le nom de l'utilisateur et le saluer
# ============================================================
nom = st.text_input("Quel est votre prénom ?")
if nom:
    st.success(f"Bonjour, {nom} ! Bienvenue dans cette application. 👋")

# ============================================================
# Etape 5 : Chargement des données avec st.file_uploader
# ============================================================
st.subheader("📂 Chargement des données")
fichier = st.file_uploader("Chargez votre fichier CSV", type=["csv"])

if fichier is not None:
    # Lecture du fichier CSV dans un DataFrame pandas
    df = pd.read_csv(fichier)
    st.write("Aperçu des données :", df.head())

    # ============================================================
    # Etape 7 : Récupérer la liste des colonnes numériques
    # ============================================================
    colonnes_numeriques = df.select_dtypes(include="number").columns.tolist()

    if len(colonnes_numeriques) < 2:
        st.warning("Le fichier doit contenir au moins 2 colonnes numériques.")
    else:
        # ============================================================
        # Etape 6 : Selectbox pour choisir entre 2D et 3D
        # ============================================================
        st.subheader("📊 Type de visualisation")
        mode = st.selectbox("Choisissez le type de graphique :", ["2D", "3D"])

        # ============================================================
        # Etape 8 : Mode 2D — sélection de 2 colonnes + st.line_chart
        # ============================================================
        if mode == "2D":
            st.subheader("Graphique 2D")
            col_x = st.selectbox("Colonne X :", colonnes_numeriques, key="x2d")
            col_y = st.selectbox("Colonne Y :", colonnes_numeriques, key="y2d")

            # Affichage avec st.line_chart (axe x = colonne choisie en index)
            chart_data = df[[col_x, col_y]].set_index(col_x)
            st.line_chart(chart_data)

        # ============================================================
        # Etape 9 : Mode 3D — sélection de 3 colonnes + px.scatter_3d
        # ============================================================
        elif mode == "3D":
            if len(colonnes_numeriques) < 3:
                st.warning("Le fichier doit contenir au moins 3 colonnes numériques pour le mode 3D.")
            else:
                st.subheader("Nuage de points 3D")
                col_x = st.selectbox("Colonne X :", colonnes_numeriques, key="x3d")
                col_y = st.selectbox("Colonne Y :", colonnes_numeriques, key="y3d")
                col_z = st.selectbox("Colonne Z :", colonnes_numeriques, key="z3d")

                # Affichage du nuage de points 3D avec plotly express
                fig = px.scatter_3d(df, x=col_x, y=col_y, z=col_z,
                                    title=f"Nuage de points 3D : {col_x} / {col_y} / {col_z}")
                st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Veuillez charger un fichier CSV pour commencer.")
