import streamlit as st

st.set_page_config(page_title="Home",layout='wide',page_icon='./images/home.png')
st.title("YOLO V5 APP")
st.header("Welcome to this app")
st.write("This is still in testing phase and you can help us by giving your valuable feedback to us")
st.write("Idea and development by Prasuk Jain")
#Content
st.markdown("""
            ### Object Detection App ###
            - Automatically detect 20 objects from Image
            - [Click here for app](/YOLO_Web_App/)
            - For more details contact Owner
            
            """)
st.markdown('<a href="mailto:p.jain161202@gmail.com">Contact us !</a>', unsafe_allow_html=True)

