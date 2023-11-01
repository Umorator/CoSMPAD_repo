import streamlit as st
import os
import base64


st.title("Imprint")
st.write('Humboldt-Universität zu Berlin, Institute of Biology, Theoretical Biophysics, 10099 Berlin, Germany')
st.write('Prof. Dr. Edda Klipp - edda.klipp@hu-berlin.de, M.Sc. Rafael Moran - morantor@hu-berlin.de')


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" width="110" height="110" border="0"/>
        </a>'''
    return html_code

col1, col2, col3, col4, col5 = st.columns([1, 0.5,0.5, 0.5, 1])

hu_berlin_html = get_img_with_href('Huberlin-logo.png', 'https://www.hu-berlin.de/de')
tbp_html = get_img_with_href('TBP_logo.png', 'https://rumo.biologie.hu-berlin.de/tbp/index.php/en//')


col2.markdown(tbp_html, unsafe_allow_html=True)

col4.markdown(hu_berlin_html, unsafe_allow_html=True)


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



