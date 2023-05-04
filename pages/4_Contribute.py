import streamlit as st
import pandas as pd
import pathlib
import os



st.title('Contribute to the Database')
st.write('''
For contributions,
please click the Download Template button
to download the data submission format and upload
your data in the specified format. An example is given in the template.
''')


df = pd.read_csv('/home/rafael/SP_Database/Template.csv')
data_as_csv= df.to_csv(index=False).encode("utf-8")

st.download_button(label="Download Template",data=data_as_csv,file_name='Template.csv',mime='text/csv',)


uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = uploaded_file.getvalue().decode('utf-8').splitlines()         
#upload_state = st.text_area("Upload State", "", key="upload_state")

def upload():
    if uploaded_file is None:
        new_title = '<p style="font-family:sans-serif; color:Red; font-size: 24px;">Error: Upload a file first!</p>'
        st.markdown(new_title, unsafe_allow_html=True)
    else:
        data = uploaded_file.getvalue().decode('utf-8')
        parent_path = pathlib.Path(__file__).parent.parent.resolve()           
        save_path = os.path.join(parent_path, "data")
        complete_name = os.path.join(save_path, uploaded_file.name)
        destination_file = open(complete_name, "w")
        destination_file.write(data)
        destination_file.close()
        new_title = '<p style="font-family:sans-serif; color:Green; font-size: 24px;">Your data has been submitted. Thank you!</p>'
        st.markdown(new_title, unsafe_allow_html=True)
st.button("Submit", on_click=upload)
