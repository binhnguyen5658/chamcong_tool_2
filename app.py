import streamlit as st
import pandas as pd
from cc_func import transform_file
import base64
from io import StringIO, BytesIO

# --- function to download file excel --- 
def generate_excel_download_link(df):
    towrite = BytesIO()
    df.to_excel(towrite, index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="checkin_data.xlsx">Checkin data</a>'
    return st.markdown(href, unsafe_allow_html=True)
# ---------------------------------------

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_page_config(page_title='Chấm Công Tool', layout='centered')

st.title('Tool xử lý file chấm công')

st.subheader('Upload File')

uploaded_file = st.file_uploader(label='Choose file', type='xlsx')

if uploaded_file:
    st.markdown('---')
    # --- input section ---
    df =  pd.read_excel(uploaded_file, engine='openpyxl',header=None)

    # --- process and show preview section ---
    df_clean = transform_file(df)

    st.subheader('Preview 10 rows in result file')
    st.dataframe(df_clean.head(10))

    # --- Download file ---

    st.subheader('Download File')

    # @st.cache
    # def convert_df(df):
    #     # IMPORTANT: Cache the conversion to prevent computation on every rerun
    #     return df.to_csv(index=False)

    # file = convert_df(df_clean)

    # button = st.download_button(
    #     label='Download file',
    #     data=file,
    #     file_name='Checkin_data.csv',
    #     mime='text/csv',
    # )

    generate_excel_download_link(df_clean)








