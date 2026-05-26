# TP2 - Application Streamlit pour la visualisation de données
# Auteur : HUI Winston
# Lien de la page web publiée : à compléter après déploiement


# Etape 3 : Chargement des librairies
import streamlit as st
import pandas as pd
import plotly.express as px


# Titre principal de l'application

st.title("📊 TP2 eval")
st.write("""
Bienvenue dans cette application de visualisation de données.
Elle vous permet de charger un fichier CSV et d'explorer vos données
à travers des graphiques interactifs en **2D** ou **3D**.
""")

st.divider()


# Etape 4 : Demander le nom de l'utilisateur et le saluer

st.header("👤 Etape 1 — Identification")
st.write("Veuillez entrer votre prénom pour personnaliser votre expérience.")

nom = st.text_input("Quel est votre prénom ?")
if nom:
    st.success(f"Bonjour, {nom} ! Bienvenue dans cette application. 👋")

st.divider()


# Etape 5 : Chargement des données avec st.file_uploader

st.header("📂 Etape 2 — Chargement des données")
st.write("""
Chargez un fichier CSV contenant vos données.
L'application détectera automatiquement les colonnes numériques
qui pourront être utilisées pour la visualisation.
""")

fichier = st.file_uploader("Choisissez votre fichier CSV", type=["csv"])

if fichier is not None:
    # Lecture du fichier CSV dans un DataFrame pandas
    df = pd.read_csv(fichier)

    st.success(f"✅ Fichier chargé avec succès : **{fichier.name}** ({len(df)} lignes, {len(df.columns)} colonnes)")
    st.write("**Aperçu des 5 premières lignes :**")
    st.dataframe(df.head())

    st.divider()

    
    # Etape 7 : Récupérer la liste des colonnes numériques
   
    colonnes_numeriques = df.select_dtypes(include="number").columns.tolist()
    st.write(f"🔢 **Colonnes numériques détectées ({len(colonnes_numeriques)}) :** {', '.join(colonnes_numeriques)}")

    if len(colonnes_numeriques) < 2:
        st.warning("⚠️ Le fichier doit contenir au moins 2 colonnes numériques pour la visualisation.")
    else:

        st.divider()

        
        # Etape 6 : Selectbox pour choisir entre 2D et 3D
       
        st.header("🎨 Etape 3 — Choix du type de visualisation")
        st.write("""
Choisissez le type de graphique que vous souhaitez afficher :
- **2D** : un graphique en ligne avec deux colonnes (axe X et axe Y)
- **3D** : un nuage de points interactif avec trois colonnes (X, Y et Z)
        """)

        mode = st.selectbox("Type de graphique :", ["2D", "3D"])

        st.divider()

       
        # Etape 8 : Mode 2D — sélection de 2 colonnes + st.line_chart
        
        if mode == "2D":
            st.header("📈 Etape 4 — Graphique 2D")
            st.write("""
Sélectionnez les deux colonnes numériques à visualiser.
La colonne **X** sera utilisée comme axe horizontal,
et la colonne **Y** comme axe vertical.
            """)

            col_x = st.selectbox("Colonne X (axe horizontal) :", colonnes_numeriques, key="x2d")
            col_y = st.selectbox("Colonne Y (axe vertical) :", colonnes_numeriques, key="y2d")

            st.write(f"**Graphique : {col_y} en fonction de {col_x}**")
            chart_data = df[[col_x, col_y]].set_index(col_x)
            st.line_chart(chart_data)

        # Etape 9 : Mode 3D — sélection de 3 colonnes + px.scatter_3d
        elif mode == "3D":
            st.header("🌐 Etape 4 — Nuage de points 3D")
            st.write("""
Sélectionnez trois colonnes numériques pour créer un nuage de points en 3 dimensions.
Vous pouvez **faire tourner** le graphique en cliquant et glissant la souris.
            """)

            if len(colonnes_numeriques) < 3:
                st.warning("⚠️ Le fichier doit contenir au moins 3 colonnes numériques pour le mode 3D.")
            else:
                col_x = st.selectbox("Colonne X :", colonnes_numeriques, key="x3d")
                col_y = st.selectbox("Colonne Y :", colonnes_numeriques, key="y3d")
                col_z = st.selectbox("Colonne Z :", colonnes_numeriques, key="z3d")

                st.write(f"**Nuage de points : {col_x} / {col_y} / {col_z}**")
                # Affichage du nuage de points 3D avec plotly express
                fig = px.scatter_3d(df, x=col_x, y=col_y, z=col_z,
                                    title=f"Nuage de points 3D : {col_x} / {col_y} / {col_z}")
                st.plotly_chart(fig, use_container_width=True)

else:
    st.info("ℹ️ Veuillez charger un fichier CSV pour commencer la visualisation.")


