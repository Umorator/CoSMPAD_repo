import streamlit as st
import os
import base64
import footer

st.title("Imprint")
st.write('Humboldt-Universität zu Berlin, Institute of Biology, Theoretical Biophysics, 10099 Berlin, Germany')
st.write('Prof. Dr. Edda Klipp - edda.klipp@hu-berlin.de, M.Sc. Rafael Moran - morantor@hu-berlin.de')

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path, target_url, width=110, height=110):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" style="display: inline-block; margin: 20px; vertical-align: middle;">
            <img src="data:image/{img_format};base64,{bin_str}" width="{width}" height="{height}" border="0"/>
        </a>'''
    return html_code


col1, col2, col3, col4, col5 = st.columns([1, 0.5, 0.5, 0.5, 1])

# Reduced size for TBP logo
tbp_html = get_img_with_href('TBP_logo.png', 'https://rumo.biologie.hu-berlin.de/tbp/index.php/en/', width=100, height=100)
hu_berlin_html = get_img_with_href('Huberlin-logo.png', 'https://www.hu-berlin.de/de')

col2.markdown(tbp_html, unsafe_allow_html=True)
col4.markdown(hu_berlin_html, unsafe_allow_html=True)

footer.display_footer()
