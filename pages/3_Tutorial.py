import streamlit as st


st.set_page_config(
    page_title="Tutorial",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Tutorial')


col1, col2, col3 = st.columns([0.5, 3, 0.5])

col2.image("CoSMPAD_vertical.png")

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
<p>Developed by Theoretical biophysics group - Humboldt-Universität zu Berlin</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)