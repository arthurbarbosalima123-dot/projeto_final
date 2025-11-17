import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config( page_title = 'Visão Países', page_icon='🌍',layout='wide')

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

#Removendo India
df = df[df['Country'] != 'India']

#Removendo India
df = df[df['Country'] != 'Indonesia']

#Removendo India
df = df[df['Country'] != 'United States of America']

#Removendo India
df = df[df['Country'] != 'Philippines']

#Removendo India
df = df[df['Country'] != 'Sri Lanka']

#==========================================
#Streamlit Barra Lateral Visão_empresa=========================

st.header ('Visão Países')


st.sidebar.markdown (' # Projeto Portfólio')
st.sidebar.markdown (' ## Análise de dados')
st.sidebar.markdown ("""---""")

st.sidebar.markdown ('## Powered by Arthur Lima')   

#==========================================
#Layout no Streamlit
###########################################

tab1, = st.tabs(['Visão Gerencial'])

with tab1:
    with st.container():
        st.markdown('##### Quantidade de Restaurantes Registrados por País')
        df_grafi = df.loc[:,['restaurant_id','Country']].groupby('Country').nunique().sort_values('restaurant_id',ascending=False).reset_index()
        df_grafi.head()
    
        fig = px.bar (df_grafi, x='Country', y='restaurant_id')
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('##### Quantidade de Cidades Registrados por País')
        df_city = df.loc[:,['city','Country']].groupby('Country').nunique().sort_values('city',ascending=False).reset_index()

        df_city.head(7)
    
        fig = px.bar (df_city, x='Country', y='city')
        st.plotly_chart(fig, use_container_width=True)

    

    with st.container():
        col1, col2 = st.columns( 2 )
        
        with col1:
            st.markdown('### Média de Avaliações por País')
            df_avali = df.loc[:,['Country','votes']].groupby('Country').mean().sort_values('votes',ascending=False).reset_index()
            

            fig = px.bar (df_avali, x='Country', y='votes')
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.markdown('##### Média de preço de um prato para duas pessoas por País')
            df_for_two = df.loc[:,['Country','average_cost_for_two']].groupby('Country').mean().sort_values('average_cost_for_two',ascending=False).reset_index()

            fig = px.bar (df_for_two, x='Country',y='average_cost_for_two')
            st.plotly_chart(fig, use_container_width=True)





















