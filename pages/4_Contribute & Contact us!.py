import streamlit as st
import pandas as pd
import pathlib
import os
import webbrowser


st.set_page_config(
    page_title="Contribute to the Database",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title('Contribute to the Database')
st.write('''
For contributions,
please click the Download Template button
to download the data submission format and send 
your data via email in the specified format. An example is given in the template. Further questions? Please contact us! (Email/Group page):
''')


df = pd.read_csv('Template.csv')
data_as_csv= df.to_csv(index=False).encode("utf-8")

st.download_button(label="Download Template",data=data_as_csv,file_name='Template.csv',mime='text/csv',)

#contact --------------



url = 'https://rumo.biologie.hu-berlin.de/tbp/index.php/en//'


    
st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])

with col2:
    st.markdown('<a href = "mailto: edda.klipp@rz.hu-berlin.de, morantor@hu-berlin.de"> <i class="material-icons" style="font-size: 2.2em;">email</a>',unsafe_allow_html=True)
    #st.write(" Email") 

with col3:
    #if st.button("👩‍🏫"):
        #webbrowser.open_new_tab(url)
    st.markdown('<a href="https://rumo.biologie.hu-berlin.de/tbp/index.php/en//"> <i class="material-icons" style="font-size: 1.6em;">👩‍🏫</a>',unsafe_allow_html=True)
    #st.write("Our Group")

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