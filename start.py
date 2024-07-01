import streamlit as st
import time

if 'wide' not in st.session_state:
    st.set_page_config(layout='wide',
                       page_title='OAZIS',
                       initial_sidebar_state='auto')
    st.session_state['wide'] = ''
st.logo(r'reqdimages/cozentusLogo.png')
with st.container():
    st.image(r'reqdimages/cozentusLogo.png',use_column_width=True)