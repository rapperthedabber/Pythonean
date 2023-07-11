#Make something great! 
import streamlit as st
st.set_page_config(page_title = 'my Webpage', layout = 'wide')
#Header Section

with st.container():
    st.title('Jerry Python Journey')
    st.subheader('Hi, I am Jerry')
    st.write('I am a software developer and currently learning python to enhance my learning and career')


with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Skills: ')
        st.write('JavaScript, React, TypeScript, Html, Css, MongoDB, Nextjs, Netlifty, Heroku')

    with right_column:
        st.header('Interesting Facts: ')
        st.write('I am a political science major')