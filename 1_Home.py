import pandas as pd
import streamlit as st
import plotly.express as px




#path = '/home/rafael/SP_Database/CoSPAD_repo/'

df = pd.read_csv('CoSPAD_V3.csv')#.set_index('id')


st.set_page_config(
    page_title="Home",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

#st.title('CoMSPAD: A Comparative Microbial Secretory Preprotein Activity Database')

col1, col2, col3 = st.columns([0.5, 3, 0.5])

col2.image("cospad_abstract.jpg")

st.title("About")
st.write("CoMSPAD encompasses more than 20 types of experimental information found for 45 proteins by using different signal peptides. It aims to serve as a reference for the recombinant protein research community, and could also be used to make predictive models by analysing the impact of these factors on protein secretion.")


#Species distribution -----------------------------------

a = pd.DataFrame(df.Species.value_counts()).reset_index()
a.columns = ['Species','Values']

st.title('Statistics')
fig = px.pie(a, values='Values', names='Species', title='Expression Species Distribution')
st.plotly_chart(fig)

#Protein distribution ------------------------------------

b = pd.DataFrame(df['Protein name'].value_counts()).reset_index()
b.columns = ['Proteins','Values']

fig2 = px.pie(b, values='Values', names='Proteins', title='Proteins Distribution')
st.plotly_chart(fig2)

#Promoter distribution ------------------------------------

c = pd.DataFrame(df['Promoter'].value_counts()).reset_index()
c.columns = ['Promoter','Values']

fig3 = px.pie(c, values='Values', names='Promoter', title='Promoter Distribution')
st.plotly_chart(fig3)


#SP type distribution ------------------------------------
d = pd.DataFrame(df['SP type'].value_counts()).reset_index()
d.columns = ['SP type','Values']

fig4 = px.pie(d, values='Values', names='SP type', title='SP type Distribution')
st.plotly_chart(fig4)