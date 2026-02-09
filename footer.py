import streamlit as st
import base64

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def display_footer():
    logo_base64 = get_image_as_base64("Huberlin-logo.png")  # Adjust the path as needed
    footer = f"""
    <style>
    a:link , a:visited{{
        color: blue;
        background-color: transparent;
        text-decoration: underline;
    }}

    a:hover,  a:active {{
        color: red;
        background-color: transparent;
        text-decoration: underline;
    }}

    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding-left: 13%;  /* Adjust as needed */
    }}

    .logo {{
        position: absolute;
        right: 12%;
        bottom: 10px;
        width: auto;
        height: 50px;
    }}
    </style>
    <div class="footer">
        <p>Humboldt-Universität zu Berlin, Institute of Biology, Theoretical Biophysics, 10099 Berlin, Germany</p>
        <a href="https://www.hu-berlin.de/en/hu-en/imprint/data-protection-statement" target="_blank">Data Privacy Statement</a>
        <img src="data:image/png;base64,{logo_base64}" class="logo" alt="HU Logo">
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
