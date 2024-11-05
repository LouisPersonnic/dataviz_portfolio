import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import plotly.io as pio
from PIL import Image
import os
import base64
import kaleido
import io

# Configuration de la page
st.set_page_config(page_title="Portfolio Louis Personnic", layout="wide", initial_sidebar_state="expanded")

# Styles personnalisés pour la barre latérale et les autres éléments
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #0E1117;
        color: #fff;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100vh;
    }
    .sidebar-title {
        font-size: 3em;
        font-weight: bold;
        color: #fff;
        margin-top: 10px;
        font-family: 'Arial Black', Gadget, sans-serif;
    }
    .sidebar-subtitle {
        font-size: 1.2em;
        font-weight: bold;
        color: #fff;
        margin-bottom: 10px;
    }
    .sidebar-link {
        font-size: 1.1em;
        color: #fff;
        text-decoration: none;
        display: block;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        transition: background-color 0.3s ease, color 0.3s ease;
        cursor: pointer;
    }
    .sidebar-link:hover {
        background-color: #444654;
        color: #e0e0e0;
    }
    .selected-link {
        background-color: #444654;
        color: #fff;
    }
    .divider {
        border-bottom: 1px solid #555;
        margin: 10px 0;
    }
    .footer-logo {
        width: 50%;  /* Half the original width */
        margin: 20px auto 0 auto; /* Center the image */
    }
    </style>
    """, unsafe_allow_html=True)

# Vérifier l'existence des fichiers
logo_path = "LOGO_EFREI_BLANC.png"
cv_path = "cv_stage_data_analyst_louis_personnic.pdf"
file_path = "table-mortalite.xlsx"

# Charger les données Excel
if os.path.exists(file_path):
    excel_data = pd.ExcelFile(file_path)
    femmes_data = excel_data.parse("Table_mortalité_Femme")
    hommes_data = excel_data.parse("Table_mortalité_Homme")
else:
    st.error("Le fichier table-mortalite.xlsx est introuvable. Veuillez vérifier le chemin du fichier.")

# Initialisation de l'état de la session pour la page sélectionnée
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Qui suis-je ?"

# Fonction pour changer de page
def set_page(page_name):
    st.session_state.selected_page = page_name

# Barre latérale avec les liens de navigation
st.sidebar.markdown('<div class="sidebar-title">Portfolio</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">- Louis Personnic</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)

if st.sidebar.button("Qui suis-je ?"):
    set_page("Qui suis-je ?")

st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Projet - Data Visualization</div>', unsafe_allow_html=True)

# Liens de navigation qui changent la page en fonction de la sélection
pages = ["Objectifs", "Visualisations", "Conclusions"]
for page in pages:
    if st.sidebar.button(page):
        set_page(page)

# Ajouter l'image du logo en bas de la barre latérale, aligné à droite
st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)
if os.path.exists(logo_path):
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}" style="width:150px; display:block; margin-left:auto; margin-right:0; position:absolute; bottom:-80px;">',
        unsafe_allow_html=True
    )
else:
    st.sidebar.write("Le logo n'est pas disponible.")



import streamlit as st
import plotly.io as pio

try:
    import kaleido
except ImportError:
    st.error("Le package 'kaleido' n'est pas installé. Veuillez l'installer avec la commande : pip install -U kaleido")

import streamlit as st
import plotly.io as pio
from fpdf import FPDF
from PIL import Image
import io
import base64

def download_pdf(fig, filename):
    try:
        # Exporter la figure Plotly au format image PNG
        image_bytes = pio.to_image(fig, format='png')

        # Charger l'image PNG dans PIL pour la manipulation
        image = Image.open(io.BytesIO(image_bytes))

        # Créer un fichier temporaire pour l'image
        temp_image_path = f"{filename}.png"
        image.save(temp_image_path, format='PNG')

        # Créer un document PDF avec FPDF
        pdf = FPDF()
        pdf.add_page()
        # Ajuster la taille de l'image pour le PDF
        pdf.image(temp_image_path, x=10, y=10, w=180)

        # Sauvegarder le PDF dans un fichier temporaire
        pdf_output_path = f"{filename}.pdf"
        pdf.output(pdf_output_path)

        # Lire le contenu du fichier PDF pour le téléchargement
        with open(pdf_output_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()

        # Utiliser st.download_button pour le téléchargement direct
        st.download_button(
            label="Télécharger le PDF",
            data=pdf_data,
            file_name=f"{filename}.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"Erreur lors de la génération du PDF : {str(e)}")



# Afficher le contenu en fonction de la page sélectionnée
selected_page = st.session_state.selected_page

if selected_page == "Qui suis-je ?":
    st.header("Louis Personnic, étudiant ingénieur data")
    
    # Paragraphe d'introduction
    st.write("""
    Actuellement étudiant en deuxième année de cycle ingénieur à Efrei Paris, spécialisé en Business Intelligence & Analytics.
    Curieux, dynamique et organisé, je m'efforce d'allier mes compétences techniques en data science et en programmation à une expérience
    pratique acquise à travers divers projets académiques et professionnels. En dehors de mes études, je m'investis activement en tant que 
    vice-président de l'association de cuisine Efrei Chefs et je cultive des passions telles que l'escalade, l'analyse d'univers fictifs, 
    et la lecture de bandes dessinées et mangas.
    """)

    # Expanders avec plus d'informations
    with st.expander("Compétences", expanded=False):
        st.write("""
        **Compétences techniques :**
        - Programmation : Je maîtrise plusieurs langages de programmation tels que C, Java, Python, JavaScript, HTML, CSS et SQL. 
          J'ai également une expérience en développement web avec le framework Vue.js.
        - Outils et logiciels : Je suis à l'aise avec divers outils et logiciels, notamment le pack Microsoft Office, VS Code, Git, 
          Netbeans, MongoDB, MySQL, et Power BI. J'utilise régulièrement des bibliothèques Python comme Pandas, Numpy pour la manipulation 
          de données, ainsi que Matplotlib et Seaborn pour la visualisation.

        **Langues :**
        - Je parle couramment l'anglais, avec un score de 870 au TOEIC.
        - J'ai obtenu le niveau affaires au Projet Voltaire (score de 819), attestant d'un bon niveau en orthographe et grammaire française.

        **Certifications :**
        - Certificat de prévention et secours civiques de niveau 1 (PSC1).
        - Permis de conduire (catégorie B).
        """)

    with st.expander("Expériences professionnelles", expanded=False):
        st.write("""
        **FNAC Montparnasse (2023-2024) :**
        - J'ai travaillé en tant que vendeur dans le secteur des produits éditoriaux (livres, jeunesse, BD, mangas). Cette expérience 
          m'a permis de développer mes compétences en vente et en service client dans un environnement dynamique.
        
        **Thermozyklus (juin-juillet 2022) :**
        - Durant ce stage ouvrier, j'étais chargé de la saisie des informations sur les fiches clients dans une entreprise spécialisée 
          dans les systèmes de régulation thermique. Ce rôle m'a donné un aperçu des processus industriels et de la gestion des données.
        """)

    with st.expander("Formations", expanded=False):
        st.write("""
        **Efrei Paris (2021-2024) :**
        - Actuellement en cours de cycle ingénieur en informatique, avec une spécialisation en Data Science et plus précisément en 
          Business Intelligence & Analytics. J'ai également participé à un programme de mobilité internationale à CPUT, l'Université de 
          Technologie du Cap, en Afrique du Sud, pour approfondir mes compétences en data science.
        """)

            
    # Vérifier si le fichier PDF est disponible pour le téléchargement
    if os.path.exists(cv_path):
        with open(cv_path, "rb") as file:
            cv_data = file.read()

            # Boutons personnalisés avec le style demandé

        st.markdown(
            """
            <style>
            .custom-button {
                background-color: transparent;
                color: white !important;
                border: 1px solid white;
                border-radius: 8px;  /* Bordures légèrement plus arrondies */
                padding: 10px 20px;
                font-size: 1.1em;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                text-align: center;
                display: inline-block;
            }
            .custom-button:hover {
                color: red!important;
                border-color: red;
            }
            .button-container {
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
            }
            </style>
        
            <div class="button-container">
                <a href="cv_stage_data_analyst_louis_personnic.pdf" download="cv_stage_data_analyst_louis_personnic.pdf" class="custom-button">
                    CV
                </a>
                <a href="https://github.com/LouisPersonnic" target="_blank" class="custom-button">
                    GitHub
                </a>
                <a href="https://www.linkedin.com/in/louis-personnic-56194a221/" target="_blank" class="custom-button">
                    LinkedIn
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Le CV n'est pas disponible.")

elif selected_page == "Objectifs":
    st.header("Introduction")
    st.write("""
    Le projet de Data Visualization utilise la base de données "Table de mortalité par âge, sexe, et niveau de comorbidité pour la France" du site data.gouv.fr
    
    Ce projet vise à explorer l'impact des comorbidités sur la mortalité et l'espérance de vie des personnes âgées de 18 ans ou plus en France métropolitaine, à partir de données collectées entre 2011 et 2018. Les données sont fiables, validées par des experts, et organisées par sexe et par niveaux de comorbidité, qui sont définis selon l'indice de comorbidité de Charlson. Les niveaux de comorbidité sont les suivants :

    Le dataset contient les colonnes suivantes : âge, taux de mortalité, ordre de survie et espérance de vie. Ces 3 dernières colonnes sont présentes en 4 fois, pour correspondre aux différents niveaux de comorbidité.

    - **CCI0** : Absence de comorbidité, correspondant aux personnes ne présentant aucune maladie chronique majeure.
    - **CCI1** : Comorbidité faible, incluant des affections mineures ou bien gérées, comme l'hypertension contrôlée ou le diabète de type 2.
    - **CCI2** : Comorbidité intermédiaire, englobant des maladies plus graves telles que les antécédents de cancer (sans métastase) ou l'insuffisance cardiaque modérée.
    - **CCI3** : Comorbidité élevée, associée à des pathologies sévères ou multiples, comme la maladie rénale chronique avancée, un cancer métastatique, ou une combinaison de plusieurs conditions chroniques.

    Ces données sont particulièrement pertinentes pour des secteurs comme les assurances, les institutions financières, et les organismes de santé publique. Les assureurs peuvent utiliser cette analyse pour évaluer les risques et ajuster les polices d'assurance-vie ou de santé en fonction de l'espérance de vie attendue et du niveau de risque associé aux antécédents médicaux. Les banques, quant à elles, peuvent s'appuyer sur ces données pour ajuster les conditions d'octroi de prêts ou les taux d'intérêt en fonction de la santé globale des emprunteurs, surtout pour les prêts à long terme. En santé publique, ces analyses permettent de prioriser les ressources pour les populations à risque et d'orienter les politiques de prévention en fonction des profils de risque.

    Lors de l'exploration initiale, les données se sont révélées complètes, sans valeurs manquantes ou aberrantes, ce qui a permis de commencer l'analyse directement. Le volume et la diversité des données disponibles offrent un cadre robuste pour des visualisations significatives, facilitant l'exploration des relations entre âge, sexe, comorbidité et mortalité.
    """)


elif selected_page == "Visualisations":
    st.header("Visualisations des données")
    file_path_xlsx = "table-mortalite.xlsx"

    # Vérifier si les données sont disponibles
    if 'femmes_data' not in locals() or 'hommes_data' not in locals():
        st.error("Les données de mortalité ne sont pas chargées. Veuillez vérifier le fichier source.")
    else:
        # Choix du mode : simple ou comparaison
        mode = st.radio("Choisissez le mode d'affichage :", ("Simple", "Comparaison"))

        if mode == "Simple":
            # Option pour sélectionner le sexe
            sexe = st.radio("Sélectionnez le sexe :", ("Femmes", "Hommes"))

            # Sélection des données en fonction du sexe choisi
            data = femmes_data if sexe == "Femmes" else hommes_data

            # Filtres interactifs
            age_min, age_max = st.slider("Sélectionnez la tranche d'âge :", int(data["Age"].min()), int(data["Age"].max()), (30, 70))
            niveau_comorbidite = st.multiselect("Sélectionnez les niveaux de comorbidité :", ["CCI0", "CCI1", "CCI2", "CCI3"], ["CCI0", "CCI1", "CCI2", "CCI3"])

            # Filtrage des données en fonction des sélections
            data_filtre = data[(data["Age"] >= age_min) & (data["Age"] <= age_max)]

            # Visualisation 1 : Taux de mortalité par tranche d'âge et sexe
            st.write("### Taux de mortalité par tranche d'âge et sexe")
            age_sexe_mortalite = data_filtre.groupby("Age")[niveau_comorbidite].mean().reset_index()
            fig1 = px.bar(age_sexe_mortalite, x="Age", y=niveau_comorbidite, title=f"Mortalité par tranche d'âge et niveau de comorbidité chez les {sexe.lower()}",
                          color_discrete_sequence=px.colors.sequential.Plasma_r)
            st.plotly_chart(fig1)

            # Bouton de téléchargement
            if st.button("Télécharger", key="download_fig1"):
                download_pdf(fig1, "graphique1")

            # Visualisation 2 : Taux de mortalité selon le niveau de comorbidité
            st.write("### Taux de mortalité selon le niveau de comorbidité")
            comorbidite_data = data_filtre.melt(id_vars=["Age"], value_vars=niveau_comorbidite,
                                                var_name="Niveau de comorbidité", value_name="Taux de mortalité")
            fig2 = px.line(comorbidite_data, x="Age", y="Taux de mortalité", color="Niveau de comorbidité",
                           title=f"Taux de mortalité chez les {sexe.lower()} selon le niveau de comorbidité",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)
            st.plotly_chart(fig2)

            # Bouton de téléchargement
            if st.button("Télécharger", key="download_fig2"):
                download_pdf(fig2, "graphique2")

            # Visualisation 3 : Courbes pour l'espérance de vie par niveau de comorbidité
            st.write("### Espérance de vie par niveau de comorbidité")
            esp_life_mean = data_filtre.melt(id_vars=["Age"], value_vars=["EV_CCI0", "EV_CCI1", "EV_CCI2", "EV_CCI3"],
                                             var_name="Niveau de comorbidité", value_name="Espérance de vie")
            fig3 = px.line(esp_life_mean, x="Age", y="Espérance de vie", color="Niveau de comorbidité",
                           title="Espérance de vie par niveau de comorbidité",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)
            st.plotly_chart(fig3)

            # Bouton de téléchargement
            if st.button("Télécharger", key="download_fig3"):
                download_pdf(fig3, "graphique3")

        elif mode == "Comparaison":
            # Comparaison des données avec deux ensembles d'options
            col1, col2 = st.columns(2)

            with col1:
                st.write("### Options pour le graphique de gauche")
                sexe1 = st.radio("Sexe (gauche) :", ("Femmes", "Hommes"), key="sexe1")
                data1 = femmes_data if sexe1 == "Femmes" else hommes_data
                age_min1, age_max1 = st.slider("Tranche d'âge (gauche) :", int(data1["Age"].min()), int(data1["Age"].max()), (30, 70), key="age1")
                niveau_comorbidite1 = st.multiselect("Niveaux de comorbidité (gauche) :", ["CCI0", "CCI1", "CCI2", "CCI3"], ["CCI0", "CCI1", "CCI2", "CCI3"], key="comorb1")

                # Filtrage des données pour le graphique de gauche
                data_filtre1 = data1[(data1["Age"] >= age_min1) & (data1["Age"] <= age_max1)]

                # Histogramme pour le graphique de gauche
                st.write("#### Taux de mortalité par tranche d'âge et sexe (gauche)")
                age_sexe_mortalite1 = data_filtre1.groupby("Age")[niveau_comorbidite1].mean().reset_index()
                fig_left1 = px.bar(age_sexe_mortalite1, x="Age", y=niveau_comorbidite1, 
                                   title=f"Mortalité par tranche d'âge chez les {sexe1.lower()}",
                                   color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_left1, key="fig_left1")
                if st.button("Télécharger", key="download_fig_left1"):
                    download_pdf(fig_left1, "graphique_gauche1")

                # Courbes pour l'espérance de vie (gauche)
                st.write("#### Espérance de vie par niveau de comorbidité (gauche)")
                esp_life_mean1 = data_filtre1.melt(id_vars=["Age"], value_vars=["EV_CCI0", "EV_CCI1", "EV_CCI2", "EV_CCI3"],
                                                   var_name="Niveau de comorbidité", value_name="Espérance de vie")
                fig_left2 = px.line(esp_life_mean1, x="Age", y="Espérance de vie", color="Niveau de comorbidité",
                                    title=f"Espérance de vie chez les {sexe1.lower()}",
                                    color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_left2, key="fig_left2")
                if st.button("Télécharger", key="download_fig_left2"):
                    download_pdf(fig_left2, "graphique_gauche2")

                # Taux de mortalité selon le niveau de comorbidité (gauche)
                st.write("#### Taux de mortalité selon le niveau de comorbidité (gauche)")
                comorbidite_data1 = data_filtre1.melt(id_vars=["Age"], value_vars=niveau_comorbidite1,
                                                      var_name="Niveau de comorbidité", value_name="Taux de mortalité")
                fig_left3 = px.line(comorbidite_data1, x="Age", y="Taux de mortalité", color="Niveau de comorbidité",
                                    title=f"Taux de mortalité chez les {sexe1.lower()} selon le niveau de comorbidité",
                                    color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_left3, key="fig_left3")
                if st.button("Télécharger", key="download_fig_left3"):
                    download_pdf(fig_left3, "graphique_gauche3")

            with col2:
                st.write("### Options pour le graphique de droite")
                sexe2 = st.radio("Sexe (droite) :", ("Femmes", "Hommes"), key="sexe2")
                data2 = femmes_data if sexe2 == "Femmes" else hommes_data
                age_min2, age_max2 = st.slider("Tranche d'âge (droite) :", int(data2["Age"].min()), int(data2["Age"].max()), (30, 70), key="age2")
                niveau_comorbidite2 = st.multiselect("Niveaux de comorbidité (droite) :", ["CCI0", "CCI1", "CCI2", "CCI3"], ["CCI0", "CCI1", "CCI2", "CCI3"], key="comorb2")

                # Filtrage des données pour le graphique de droite
                data_filtre2 = data2[(data2["Age"] >= age_min2) & (data2["Age"] <= age_max2)]

                # Histogramme pour le graphique de droite
                st.write("#### Taux de mortalité par tranche d'âge et sexe (droite)")
                age_sexe_mortalite2 = data_filtre2.groupby("Age")[niveau_comorbidite2].mean().reset_index()
                fig_right1 = px.bar(age_sexe_mortalite2, x="Age", y=niveau_comorbidite2, 
                                    title=f"Mortalité par tranche d'âge chez les {sexe2.lower()}",
                                    color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_right1, key="fig_right1")
                if st.button("Télécharger", key="download_fig_right1"):
                    download_pdf(fig_right1, "graphique_droite1")

                                # Courbes pour l'espérance de vie (droite)
                st.write("#### Espérance de vie par niveau de comorbidité (droite)")
                esp_life_mean2 = data_filtre2.melt(id_vars=["Age"], value_vars=["EV_CCI0", "EV_CCI1", "EV_CCI2", "EV_CCI3"],
                                                   var_name="Niveau de comorbidité", value_name="Espérance de vie")
                fig_right2 = px.line(esp_life_mean2, x="Age", y="Espérance de vie", color="Niveau de comorbidité",
                                     title=f"Espérance de vie chez les {sexe2.lower()}",
                                     color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_right2, key="fig_right2")
                if st.button("Télécharger", key="download_fig_right2"):
                    download_pdf(fig_right2, "graphique_droite2")

                # Taux de mortalité selon le niveau de comorbidité (droite)
                st.write("#### Taux de mortalité selon le niveau de comorbidité (droite)")
                comorbidite_data2 = data_filtre2.melt(id_vars=["Age"], value_vars=niveau_comorbidite2,
                                                      var_name="Niveau de comorbidité", value_name="Taux de mortalité")
                fig_right3 = px.line(comorbidite_data2, x="Age", y="Taux de mortalité", color="Niveau de comorbidité",
                                     title=f"Taux de mortalité chez les {sexe2.lower()} selon le niveau de comorbidité",
                                     color_discrete_sequence=px.colors.sequential.Plasma_r)
                st.plotly_chart(fig_right3, key="fig_right3")
                if st.button("Télécharger", key="download_fig_right3"):
                    download_pdf(fig_right3, "graphique_droite3")
                    
                    
        # Vérifier si le fichier existe
        if os.path.exists(file_path_xlsx):
        # Lire le contenu du fichier pour le téléchargement
            with open(file_path_xlsx, "rb") as file:
                file_data = file.read()       
                     
            # Ajouter un bouton de téléchargement
        st.download_button(
            label="Télécharger le dataset",
            data=file_data,
            file_name="table-mortalite.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

elif selected_page == "Conclusions":
    st.header("Conclusion")
    st.write("""
    L'analyse approfondie des données met en évidence des tendances significatives qui soulignent l'importance de la prise en charge des comorbidités et de la gestion des risques liés à l'âge et au sexe :

    - **Relation entre âge et mortalité** : Les taux de mortalité augmentent logiquement avec l'âge, mais cette progression est beaucoup plus marquée pour les individus avec des comorbidités élevées (CCI3). Par exemple, à partir de 70 ans, la différence de mortalité entre les personnes sans comorbidité (CCI0) et celles avec des comorbidités élevées (CCI3) devient nettement plus prononcée, illustrant l'impact cumulatif des maladies chroniques sur la mortalité.

    - **Comparaison entre sexes** : Les femmes présentent généralement une espérance de vie supérieure à celle des hommes, même avec des niveaux de comorbidité similaires. Les données montrent que pour les femmes, les écarts d'espérance de vie par rapport aux hommes sont particulièrement visibles dans les tranches d'âge les plus élevées (80 ans et plus), et ce, quel que soit le niveau de comorbidité. Cela suggère une résilience accrue face aux maladies chroniques ou une meilleure gestion de la santé au cours de la vie.

    - **Impact des comorbidités** : L'effet de chaque niveau de comorbidité sur la mortalité et l'espérance de vie est progressif. Les individus avec des comorbidités faibles (CCI1) voient leur espérance de vie légèrement réduite par rapport à ceux sans comorbidité, tandis que les comorbidités intermédiaires (CCI2) entraînent une baisse plus significative. Les personnes atteintes de comorbidités sévères (CCI3) ont une espérance de vie fortement diminuée, avec un risque de mortalité accru même dès les tranches d'âge plus jeunes (par exemple, 50-60 ans).

    - **Disparités liées à la gestion des comorbidités** : Les résultats montrent également l'importance de la gestion proactive des comorbidités pour réduire la mortalité. Les personnes avec une même catégorie de comorbidité peuvent avoir des espérances de vie différentes, ce qui peut être attribué à la gestion des soins, l'accès aux traitements, ou les différences dans les modes de vie.

    En somme, ces analyses confirment que l'âge, le sexe et le niveau de comorbidité sont des facteurs déterminants de la mortalité et de l'espérance de vie. Ces résultats peuvent guider les politiques de santé et les stratégies de gestion des risques pour améliorer la qualité de vie des populations les plus vulnérables et optimiser l'utilisation des ressources dans les systèmes de santé.
    """)



