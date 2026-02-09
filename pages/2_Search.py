import pandas as pd
import streamlit as st
import altair as alt
from pandas.api.types import is_string_dtype
import footer
import os

st.set_page_config(
    page_title="Search",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns([1, 1])
col1.title("Search")


def plot(df, column):
    order = ['SP(Sec/SPI)', 'TAT(Tat/SPI)', 'LIPO(Sec/SPII)', 'OTHER']
    if st.button('Display Figure', key=f"r {df[column].unique()}"):
        df = df[df.enzyme_activity != 'NR']
        df.enzyme_activity = df.enzyme_activity.astype(float)
        c = alt.Chart(df).mark_bar().transform_calculate(
            url='https://www.uniprot.org/uniprotkb?query=' + alt.datum['UniprotKB_SP']
        ).encode(
            alt.X('SP name:N', sort='-y', title='SP name'),
            alt.Y('enzyme_activity:Q', title='Enzyme Activity (' + df.Units.unique() + ')'),
            alt.Color('SP type:N', scale={"scheme": "dark2"}, sort=order),
            order="order:Q",
            href='url:N',
            tooltip=('SP name:N', 'Promoter:N', 'sp_seq:N')
        )
        st.altair_chart(c, use_container_width=True)


# --- Cached function only does filtering logic ---
@st.cache_data
def filter_dataframe_cached(df, filters_dict):
    for column, selected_values in filters_dict.items():
        if selected_values:
            df = df[df[column].isin(selected_values)]
    return df


# --- Main App ---
df = pd.read_csv('CoSMPAD.csv')
modification_container = st.container()
list_filters = ['Species', 'Host', 'Protein name', 'Promoter', 'SP name', 'Reference']

# Step 1: Select columns to filter
with modification_container:
    to_filter_columns = st.multiselect("Filter dataframe on", list_filters, key='filters')

# Step 2: For each selected column, select values
filters_dict = {}
for column in to_filter_columns:
    if is_string_dtype(df[column]):
        filters_dict[column] = st.multiselect(f"Values for {column}", df[column].unique())

# Step 3: Filter dataframe using cached function
filtered_df = filter_dataframe_cached(df, filters_dict)
st.session_state['filtered_df'] = filtered_df

# Step 4: Show summary
st.subheader('Filter(s) Result:')
st.markdown(
    f"This file contains {filtered_df.shape[0]} SPs for "
    f"{len(filtered_df['UniprotKB/NCBI_POI'].unique())} Protein(s) and "
    f"{len(filtered_df['Promoter'].unique())} Promoter(s)."
)

# Step 5: Display plot if applicable
if len(filtered_df['Protein name'].unique()) == 1 and len(filtered_df.Host.unique()) == 1:
    plot(filtered_df, column)

# --- Buttons ---
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download data as CSV",
        data=csv_data,
        file_name='CoSMPAD_Result.csv',
        mime='text/csv'
    )

with col2:
    if st.button("Download features"):
        st.session_state['show_feature_options'] = True

with col3:
    if st.button("Display Dataframe"):
        st.session_state['show_dataframe'] = not st.session_state.get('show_dataframe', False)

# Display dataframe if button clicked
if st.session_state.get('show_dataframe', False):
    st.write("")
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        st.dataframe(filtered_df, use_container_width=True)
    st.write("")

# --- Feature selection logic (unchanged) ---
if st.session_state.get('show_feature_options', False):
    st.markdown("#### Select number of amino acids after SP to download features")
    st.markdown("""
    These datasets contain precomputed features extracted from protein regions following the signal peptide (SP).  
    The number (25, 50, 75, 100) refers to how many amino acids **after the SP** were used for the feature extraction.
    """)

    aa_choices = [25, 50, 75, 100]
    aa_cols = st.columns(4)

    for aa, col in zip(aa_choices, aa_cols):
        with col:
            if st.button(str(aa), key=f"aa_select_{aa}"):
                # --- Build path to feature file ---
                CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
                REPO_ROOT = os.path.dirname(CURRENT_DIR)
                path = os.path.join(REPO_ROOT, "Features_database", f"sp_plus{aa}.csv")

                if os.path.exists(path):
                    df_feat = pd.read_csv(path)
                    filtered_df = st.session_state.get('filtered_df', pd.DataFrame())

                    if not filtered_df.empty:
                        common_columns = set(filtered_df.columns) & set(df_feat.columns)
                        for col_name in common_columns:
                            df_feat = df_feat[df_feat[col_name].isin(filtered_df[col_name].unique())]

                        # --- Trigger immediate download ---
                        csv_data = df_feat.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label=f"Download sp_plus{aa}.csv",
                            data=csv_data,
                            file_name=f"sp_plus{aa}_filtered.csv",
                            mime="text/csv",
                            key=f"download_{aa}"
                        )
                    else:
                        st.error("No filtered data available for matching.")
                else:
                    st.error(f"File sp_plus{aa}.csv not found at {path}.")


footer.display_footer()
