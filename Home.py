import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(
    page_title="Home",
    page_icon ="📊"
)


#Image_path = 'C:\\Users\\arthu\\Downloads\\ftc_programacao_python\\Repos\\dashboards\\'
image = Image.open ('logo.png')
st.sidebar.image(image,width=120)

#import dados
df = pd.read_csv('zomato.csv')

def clean_code(df):
    """ Esta funcao tem a responsabilidade de limpar o dataframe

        Tipos de limpeza:
        1. Remover a coluna Switch to order menu pois tem o mesmo valor em todas as linhas
        2. Remover as linhas duplicadas
        3. Remover as NaNs de todas as observações que possuem NaN em alguma variável

        Input: Dataframe
        Output: Dataframe
    """


    # 2. Remover as linhas duplicadas
    df = df.drop_duplicates()

    # 3. Remover as NaNs de todas as observações que possuem NaN em alguma variável
    df = df.dropna()

    return df

# Preenchimento do nome dos países
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
  return COUNTRIES[country_id]

# Criação do Tipo de Categoria de Comida
def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

df['Price Category'] = df['Price range'].apply(create_price_type)


# Definir cores por país:
country_colors ={
"India": 'yellow',
"Australia": 'darkblue',
"Brazil": 'green',
"Canada": 'red',
"Indonesia": 'orange',
"New Zeland": 'purple',
"Philippines": 'brown',
"Qatar": 'gray',
"Singapure": 'lightblue',
"South Africa": 'pink',
"Sri Lanka": 'darkgreen',
"Turkey": 'darkred',
"United Arab Emirates": 'goldenrod',
"England": 'lightgreen',
"United States of America": 'black',
}

# Criação do nome das Cores

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

df['Color Name'] = df['Rating color'].apply(color_name)


import inflection

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

df = rename_columns(df)

# Limpando os dados
df = clean_code(df)

# Categorizar os restaurantes somente por um tipo de culinária:
df["cuisines"] = df.loc[:,"cuisines"].astype(str).apply(lambda x: x.split(",")[0])

# Criar uma nova coluna com os nomes dos países
df["Country"] = df["country_code"].apply(country_name)

#Removendo other em cuisines
df = df[df['cuisines'] != 'Other']

#Removendo Other
df = df[~df['cuisines'].isin(['Others', 'Unknown'])]

#==========================================
#Streamlit Barra Lateral Visão_empresa=========================



st.sidebar.markdown (' # Projeto Portfólio')
st.sidebar.markdown (' ## Análise de dados')
st.sidebar.markdown ("""---""")

st.sidebar.markdown ('## Powered by Arthur Lima')   

st.title ('Fome Zero!')
st.dataframe (df)

st.markdown ('### O Melhor lugar para encontrar seu mais novo restaurante favorito!')

tab1, = st.tabs(['Visão Gerencial'])

with tab1:
    with st.container():
        st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')
        
        col1,col2,col3,col4,col5 = st.columns (5)
with col1:
    rest_uni = df.loc[:,'restaurant_id'].nunique()
    col1.metric ('Restaurantes Cadastrados',rest_uni)

with col2:
    pais_uni = df.loc[:,'Country'].nunique()
    col2.metric ('Países Cadastrados',pais_uni)

with col3:
    cid = df.loc[:,'city'].nunique()
    col3.metric ('Cidades',cid)

with col4:
    total_avaliacao = df['votes'].sum()
    col4.metric ('Total de Avaliações',total_avaliacao)

# ---------------- INDIAN ----------------
with col5:
    culinaria_total = df.loc[:,'cuisines'].nunique()
    col5.metric ('Total de Culinárias oferecidas',culinaria_total)