import streamlit as st
import webbrowser




#col1, col2, col3 = st.columns([1, 1, 1])




st.title('Contact information')
#col2.image("/home/rafael/Pictures/theoretical bioph group-1.jpg",width=400)
st.write(
    """
    For any questions related to this work, please contact Us (Email/Group page):
    """
)



url = 'https://rumo.biologie.hu-berlin.de/tbp/index.php/en//'


    
st.markdown('<style>' + open('/home/rafael/SP_Database/icon.css').read() + '</style>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])

with col2:
    st.markdown('<a href = "mailto: edda.klipp@rz.hu-berlin.de"> <i class="material-icons" style="font-size: 2.2em;">email</a>',unsafe_allow_html=True)
    #st.write(" Email") 

with col3:
    if st.button("👩‍🏫"):
        webbrowser.open_new_tab(url)
    #st.write("Our Group")



