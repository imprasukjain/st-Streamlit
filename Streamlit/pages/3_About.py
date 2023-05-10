import streamlit as st

st.set_page_config(page_title='About',layout='wide',page_icon='./images/about.png')
st.header("Hope You like this Small project")
st.subheader("Let's Connect!!!!")

st.markdown('<a href = "https://github.com/imprasukjain">Github</a>',unsafe_allow_html=True)
st.markdown('<a href = "https://www.linkedin.com/in/prasuk-jain-4bb922226/">LinkedIn</a>',unsafe_allow_html=True)

Button = st.button(label="Show the Code")
if Button:
    st.markdown('<a href = "https://github.com/imprasukjain/st-Streamlit">Repository Link</a>',
                unsafe_allow_html=True)
    st.write("Don't forgot to star the repo.......")

