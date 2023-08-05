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

col2.image("abstract.png")

st.title("About")
st.write('''CoSMPAD encompasses more than 20 types of experimental information previously
 reported for 50 proteins that were secreted using different signal peptides.
   CoSMPAD aims to serve as a reference for the recombinant protein research community,
     and can also be used to make predictive models by analysing the impact of different
       determinants on the expression of secreted proteins.
''')

#Species distribution -----------------------------------
st.title('Statistics')

col1, col2, col3 = st.columns([0.3, 1, 0.3])

a = pd.DataFrame(df.Species.value_counts()).reset_index()
a.columns = ['Species','Values']


fig = px.pie(a, values='Values', names='Species', title='Species Distribution')
fig.update_traces(textposition='inside')
col2.plotly_chart(fig)

#Protein distribution ------------------------------------
col1, col2, col3 = st.columns([0.3, 1, 0.3])

b = pd.DataFrame(df['Protein name'].value_counts()).reset_index()
b.columns = ['Proteins','Values']

fig2 = px.pie(b, values='Values', names='Proteins', title='Protein Distribution')
fig2.update_traces(textposition='inside')

col2.plotly_chart(fig2)


#Promoter distribution ------------------------------------
col1, col2, col3 = st.columns([0.3, 1, 0.3])

c = pd.DataFrame(df['Promoter'].value_counts()).reset_index()
c.columns = ['Promoter','Values']

fig3 = px.pie(c, values='Values', names='Promoter', title='Promoter Distribution')
fig3.update_traces(textposition='inside')
col2.plotly_chart(fig3)


#SP type distribution ------------------------------------
col1, col2, col3 = st.columns([0.3, 1, 0.3])

d = pd.DataFrame(df['SP type'].value_counts()).reset_index()
d.columns = ['SP type','Values']

fig4 = px.pie(d, values='Values', names='SP type', title='SP type Distribution')
fig4.update_traces(textposition='inside')

col2.plotly_chart(fig4)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><p>Humboldt-Universität zu Berlin, Institute of Biology,
Theoretical Biophysics, 10099 Berlin, Germany <a  <a style='display: block;
 text-align: center;' href="https://www.hu-berlin.de/en/hu-en/imprint/data-protection-statement" target="_blank">Data Privacy Statement</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
