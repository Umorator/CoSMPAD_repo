

import pandas as pd
import streamlit as st
import altair as alt
from pandas.api.types import is_string_dtype



#path = '/home/rafael/SP_Database/CoSPAD_repo/'
#df = pd.read_csv('CoSPAD_V3.csv')#.set_index('id')
st.set_page_config(
    page_title="Search",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns([1, 1])


col1.title("Search")
#col2.image("/home/rafael/Pictures/theoretical bioph group-1.jpg",width=400)


def plot(df,column):
    order= ['SP(Sec/SPI)', 'TAT(Tat/SPI)', 'LIPO(Sec/SPII)','OTHER']
    if st.button('Display Figure',key=f"r {df[column].unique()}"):
        df = df[df.enzyme_activity != 'NR']
        df.enzyme_activity = df.enzyme_activity.astype(float)
        c = alt.Chart(df).mark_bar().transform_calculate(
            url='https://www.uniprot.org/uniprotkb?query=' + alt.datum['UniprotKB_SP']
        ).encode(
            alt.X('SP name:N',sort='-y',title='SP name'),
            alt.Y('enzyme_activity:Q', title='Enzyme Activity ('+df.Units.unique()+')'),
            alt.Color('SP type:N',scale={"scheme": "dark2"},sort=order),
            order="order:Q",
            href='url:N',tooltip=('SP name:N','Promoter:N','sp_seq:N')
        )

        st.altair_chart(c,use_container_width=True)



@st.cache_data(experimental_allow_widgets=True)
def filter_dataframe(df):
    modification_container = st.container()
    list_filters = ['Species','Host','Protein name','Promoter', 'SP name', 'Reference']

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", list_filters,key='filters')
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            if is_string_dtype(df[column]):
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique())
                df = df[df[column].isin(user_cat_input)]


        st.subheader('Filter(s) Result:')
        if (len(df['Protein name'].unique())) == 1 and (len(df.Host.unique())) == 1:
            plot(df,column)

        st.markdown('This file contains '+str(df.shape[0])+' SPs for '+ str(len(df['UniprotKB/NCBI_POI'].unique()))+' Protein(s) and '+
                str(len(df['Promoter'].unique())) + ' Promoter(s).')
        data_as_csv= df.to_csv(index=False).encode("utf-8")
        col1, col2 = st.columns([1, 1])
        ##col1.download_button(label="Download data as CSV",data=data_as_csv,file_name='CoSMPAD_Result.csv',mime='text/csv',)
        col1.download_button(label="Download data as CSV",data=pd.DataFrame(columns=['UniprotKB/NCBI_POI', 'Reference', 'enzyme_activity']),file_name='CoSMPAD_Result.csv',mime='text/csv',)

        if col2.button('Display Dataframe'):
            st.dataframe(df)



           
                
    return df



#st.dataframe(filter_dataframe(pd.read_csv('CoSPAD_V3.csv')))

filter_dataframe(pd.read_csv('CoSMPAD.csv'))


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
