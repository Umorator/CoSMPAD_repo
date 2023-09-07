import streamlit as st


st.title("Imprint")
st.write('Humboldt-Universität zu Berlin, Institute of Biology, Theoretical Biophysics, 10099 Berlin, Germany')
st.write('Prof. Dr. Edda Klipp - edda.klipp@hu-berlin.de, M.Sc. Rafael Moran - morantor@hu-berlin.de')

#col1.markdown("[![Foo](https://www.ipsa.org/sites/default/files/news-announcements/event/image-144660.png)](https://www.hu-berlin.de/de)")

col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])


col2.markdown('''
    <a href="https://rumo.biologie.hu-berlin.de/tbp/index.php/en//">
        <img src="https://ibin.co/7RXg5krCOXmy.jpg" width="105" height="80" border="0" />
    </a>''',
    unsafe_allow_html=True
)


col3.markdown('''
    <a href="https://www.hu-berlin.de/de">
        <img src="https://www.ipsa.org/sites/default/files/news-announcements/event/image-144660.png" width="150" height="100" border="0" />
    </a>''',
    unsafe_allow_html=True
)


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



