import streamlit as st
import footer

st.set_page_config(
    page_title="Tutorial",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Tutorial')


col1, col2, col3 = st.columns([0.5, 3, 0.5])

col2.image("Fig_2_Tutorial.png")

footer.display_footer()
