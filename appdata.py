import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

#Titre
st.markdown("<h1 style='text-align: center; color: red;'> AFRICORNER DATA APP</h1>", unsafe_allow_html=True)

#Description
st.markdown("""
This app performs webscraping of data from CoinAfrique over multiples pages. And we can also
download scraped data from the app directly without scraping them.
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [CoinAfrique](https://sn.coinafrique.com/) -- [CoinAfrique/Catégorie](https://sn.coinafrique.com/categorie/vetements-homme).
""")

# Arrière Plan
def add_bg_from_local(image_file):
    #Ouvre le fichier image en mode binaire("rb")
    with open(image_file, "rb") as image_file:
        # lis le contenu et encode en base64
        encoded_string = base64.b64encode(image_file.read())
    #Crée le style pour mettre l'image en arrière plan
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True
    )

#image de fond
add_bg_from_local("image.jpg")

# je crée un décorateur st qui va mémoriser le resultat de la fonction suivante
@st.cache_data

def convert_df(df):
    # mettre en cache la conversion pour éviter un nouveau calcul à chaque éxecution 
    return df.to_csv().encode('utf-8')

#création d'une fonction load avec les 4 paramètres
def load(dataframe, title, key, key1) :
    # Créer 3 colonnes avec celle du milieu plus large
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button(title, key1):
            st.subheader('Display data dimension')
            st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
            st.dataframe(dataframe)

            csv = convert_df(dataframe)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Data.csv',
                mime='text/csv',
                key = key)
            

# URL1

# Fonction for web scraping Vetements-Homme data
def load_vetementHom_data(mul_page):
    # create a empty dataframe df
    df = pd.DataFrame()
    # loop over pages indexes
    for p in range(1, int(mul_page)+1): 
        url1 = f'https://sn.coinafrique.com/categorie/vetements-homme?page={p}'
        V1 = "type habits"
        V2 = "prix"
        V3 = "adresse"
        V4 = "image_lien"
        # get pour la recupération des données depuis url1
        res = get(url1)
        # Stockez le code HTML dans un objet BeautifulSoup contenant un analyseur HTML
        soup = bs(res.text , 'html.parser')
        # Récupérez tous les conteneurs contenant les informations 
        containers = soup.find_all('div', class_='col s6 m4 l3')
        #scraper  les données de tous les containers
        data= []
        for container in containers :
            try :
                V1 = container.find('p', class_ ='ad__card-description').a.text
                V2 = container.find('p', class_ ='ad__card-price').a.text
                V3 = container.find('p', class_ ='ad__card-location').span.text
                V4 = container.find('img', class_='ad__card-img')['src']
                dic = {"type habits" : V1,
                       "prix" : V2,
                       "adresse" : V3,
                       "image_lien" : V4}
                data.append(dic)
            except:
                pass

        DF = pd.DataFrame(data)
        df= pd.concat([df, DF], axis =0).reset_index(drop = True) 
    return df

#URL2

# Fonction for web scraping Chaussures-Homme data
def load_ChaussuresHom_data(mul_page):
    # create a empty dataframe df
    df = pd.DataFrame()
    # loop over pages indexes
    for p in range(1, int(mul_page)+1): 
        url2 = f'https://sn.coinafrique.com/categorie/chaussures-homme?page={p}'
        V1 = "type chaussures"
        V2 = "prix"
        V3 = "adresse"
        V4 = "image_lien"
        # get pour la recupération des données depuis url2
        res = get(url2)
        # Stockez le code HTML dans un objet BeautifulSoup contenant un analyseur HTML
        soup = bs(res.text , 'html.parser')
        # get all containers that contains the informations 
        containers = soup.find_all('div', class_='col s6 m4 l3')
        #scraper  les données de tous les containers
        data= []
        for container in containers :
            try :
                V1 = container.find('p', class_ ='ad__card-description').a.text
                V2 = container.find('p', class_ ='ad__card-price').a.text
                V3 = container.find('p', class_ ='ad__card-location').span.text
                V4 = container.find('img', class_='ad__card-img')['src']
                dic = {"type chaussures" : V1,
                       "prix" : V2,
                       "adresse" : V3,
                       "image_lien" : V4}
                data.append(dic)
            except:
                pass

        DF = pd.DataFrame(data)
        df= pd.concat([df, DF], axis =0).reset_index(drop = True) 
    return df

#URL3

# Fonction for web scraping vetement-enfants data
def load_VetmentEnfant_data(mul_page):
    # create a empty dataframe df
    df = pd.DataFrame()
    # loop over pages indexes
    for p in range(1, int(mul_page)+1): 
        url3 = f'https://sn.coinafrique.com/categorie/vetements-enfants?page={p}'
        V1 = "type habits"
        V2 = "prix"
        V3 = "adresse"
        V4 = "image_lien"
        # get pour la recupération des données depuis url3
        res = get(url3)
        # Stockez le code HTML dans un objet BeautifulSoup contenant un analyseur HTML
        soup = bs(res.text , 'html.parser')
        # get all containers that contains the informations
        containers = soup.find_all('div', class_='col s6 m4 l3')
        #scraper  les données de tous les containers
        data= []
        for container in containers :
            try :
                V1 = container.find('p', class_ ='ad__card-description').a.text
                V2 = container.find('p', class_ ='ad__card-price').a.text
                V3 = container.find('p', class_ ='ad__card-location').span.text
                V4 = container.find('img', class_='ad__card-img')['src']
                dic = {"type habits" : V1,
                       "prix" : V2,
                       "adresse" : V3,
                       "image_lien" : V4}
                data.append(dic)
            except:
                pass

        DF = pd.DataFrame(data)
        df= pd.concat([df, DF], axis =0).reset_index(drop = True) 
    return df

#URL 4

# Fonction for web scraping Chaussures-enfants data
def load_ChaussuresEnfant_data(mul_page):
    # create a empty dataframe df
    df = pd.DataFrame()
    # loop over pages indexes
    for p in range(1, int(mul_page)+1): 
        url4 = f'https://sn.coinafrique.com/categorie/chaussures-enfants?page={p}'
        V1 = "type chaussures"
        V2 = "prix"
        V3 = "adresse"
        V4 = "image_lien"
        # get pour la recupération des données depuis url4
        res = get(url4)
        # Stockez le code HTML dans un objet BeautifulSoup contenant un analyseur HTML
        soup = bs(res.text , 'html.parser')
        # get all containers that contains the informations 
        containers = soup.find_all('div', class_='col s6 m4 l3')
        #scraper  les données de tous les containers
        data= []
        for container in containers :
            try :
                V1 = container.find('p', class_ ='ad__card-description').a.text
                V2 = container.find('p', class_ ='ad__card-price').a.text
                V3 = container.find('p', class_ ='ad__card-location').span.text
                V4 = container.find('img', class_='ad__card-img')['src']
                dic = {"type chaussures" : V1,
                       "prix" : V2,
                       "adresse" : V3,
                       "image_lien" : V4}
                data.append(dic)
            except:
                pass

        DF = pd.DataFrame(data)
        df= pd.concat([df, DF], axis =0).reset_index(drop = True) 
    return df

# option de recherche

st.sidebar.header('User Input ')
Pages = st.sidebar.selectbox('Pages indexes', list([int(p) for p in np.arange(2, 600)]))
Choices = st.sidebar.selectbox('Options', ['scraper des données suivant plusieurs pages', 'télécharger des données déjà scrapées à travers Web Scraper', 'voir un dashboard des données', "remplir un formulaire d'évaluation de l'app"])

#image de fond
add_bg_from_local("image5.jpeg")


if Choices=='scraper des données suivant plusieurs pages':

    Vetement_Homme_data_mul_pag = load_vetementHom_data(Pages)
    Chaussures_Homme_data_mul_pag = load_ChaussuresHom_data(Pages)
    Vetement_Enfants_data_mul_pag = load_VetmentEnfant_data(Pages)
    Chaussures_Enfants_data_mul_pag = load_ChaussuresEnfant_data(Pages)
    
    
    load(Vetement_Homme_data_mul_pag, 'Vetement Homme ', '1', '101')
    load(Chaussures_Homme_data_mul_pag, 'Chaussures Homme ', '2', '102')
    load(Vetement_Enfants_data_mul_pag, 'Vetement Enfants ', '3', '103')
    load(Chaussures_Enfants_data_mul_pag, 'Chaussures Enfants ', '4', '104')


elif Choices == 'télécharger des données déjà scrapées à travers Web Scraper': 
    Vetement_Homme = pd.read_csv('Vetement_Homme.csv')
    Chaussures_Homme = pd.read_csv('Chaussures_Homme.csv')
    Vetement_Enfants = pd.read_csv('Vetement_Enfants.csv')
    Chaussures_Enfants = pd.read_csv('Chaussures_Enfants.csv') 

    load(Vetement_Homme, 'Vetement Homme data', '1', '101')
    load(Chaussures_Homme, 'Chaussures Homme data', '2', '102')
    load(Vetement_Enfants, 'Vetement Enfants data', '3', '103')
    load(Chaussures_Enfants, 'Chaussures Enfants data', '4', '104')


elif  Choices == 'voir un dashboard des données': 
    df1 = pd.read_csv('Chaussures_Homme.csv')
    df2 = pd.read_csv('Vetement_Enfants.csv')

    col1, col2= st.columns(2)

    with col1:
        fig1= plt.figure(figsize=(11,7))
        colors =['skyblue', #bleu ciel
                 'orange', #orange
                 'green', #vert
                 'red'    #rouge
                ]
        plt.bar(df1['type chaussures'].value_counts()[:4].index, df1['type chaussures'].value_counts()[:4].values, color = colors)
        plt.title('Quatre Types Chaussures  les plus vendus')
        plt.xlabel('type chaussures')
        st.pyplot(fig1) # une fonction de matplotlib qui sert à afficher un graphique

    with col2:
        fig2 = plt.figure(figsize=(11,7))
        colors = ['pink', #rose
                 'yellow', #jaune
                 'purple', #violet
                 'brown' # maron
                 ]
        plt.bar(df2['type habits'].value_counts()[:7].index, df2['type habits'].value_counts()[:7].values, color = colors)
        plt.title('Les Types de vetements Enfants les plus vendus')
        plt.xlabel('type habits') # il définit l'axe horizontal
        st.pyplot(fig2)   # une fonction de matplotlib qui sert à afficher un graphique
    
        col3, col4= st.columns(2)

    with col3:
        fig3= plt.figure(figsize=(11,7))
        sns.lineplot(data=df1, x="type chaussures", y="prix") # nous donne une courbe de df1
        plt.title('Variation du prix suivant les chaussures') # titre du courbe
        st.pyplot(fig3)   # une fonction de matplotlib qui sert à afficher un graphique

    with col4:
        fig4 = plt.figure(figsize=(11,7))
        sns.lineplot(data=df2, x="type habits", y="prix") # courbe de df2
        plt.title('Variation du prix suivant les vetements')
        st.pyplot(fig4)   # une fonction de matplotlib qui sert à afficher un graphique


else :
    
    st.markdown("<h3 style='text-align: center;'>Give your Feedback</h3>", unsafe_allow_html=True)

    # centrer les deux boutons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kobo Evaluation Form"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://ee.kobotoolbox.org/x/yqSsJpd9">',
                unsafe_allow_html=True
            )

    with col2:
        if st.button("Google Forms Evaluation"):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=https://docs.google.com/forms/d/e/1FAIpQLSdjTUCqEbcn8dSPYV3hthnsIUIoo_5nUS0SSc1k501ZicQGSQ/viewform?usp=dialog">',
                unsafe_allow_html=True
            )
