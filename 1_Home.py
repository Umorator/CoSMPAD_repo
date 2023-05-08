import pandas as pd
import streamlit as st
import plotly.express as px






path = '/home/rafael/SP_Database/'

df = pd.read_csv(path+'Klipp_2023_Database_26042023.csv')
df['Specie'] = [i.split()[0]+' '+i.split()[1] for i in df.Host]


st.set_page_config(
    page_title="Home",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('CoSPAD: A Comparative Secretory Preprotein Activity Database')

col1, col2, col3 = st.columns([0.5, 3, 0.5])

col2.image(path+"cospad_abstract.jpg")

st.title("About")
st.write("CoSPAD encompasses <N> types of experimental information found in <N> proteins by using different signal peptides which aims to serve as a reference for the recombinant protein production community, providing a simple interface for the extraction of data related to the expression of a target protein.")


a = pd.DataFrame(df.Specie.value_counts()).reset_index()
a.columns = ['Specie','Values']

st.title('Statistics')
fig = px.pie(a.head(15), values='Values', names='Specie', title='Expression Specie Distribution')
st.plotly_chart(fig)

b = pd.DataFrame(df['Protein name'].value_counts()).reset_index()
b.columns = ['Proteins','Values']

fig2 = px.pie(b.head(15), values='Values', names='Proteins', title='Proteins Distribution')
st.plotly_chart(fig2)