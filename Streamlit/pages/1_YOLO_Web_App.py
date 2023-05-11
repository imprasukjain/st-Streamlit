import streamlit as st
from Yolo_Prediction_file import YOLO_Pred
import os
from PIL import Image
import numpy as np

st.set_page_config(page_title='YOLO Web App',layout='wide',page_icon='./images/object.png')

st.title("Welcome to Object Detection App")
st.write("Loading Your Model....")
with st.spinner("Please wait for your model to load"):
    yolo = YOLO_Pred(onnx_model='./model/best.onnx',data_yaml='Streamlit/model/data.yaml')
    st.success("Model Loaded Successfully")

#Upload_Image
def Upload_Image():
    image_file = st.file_uploader(label="Upload Your Image Here")
    if image_file is not None:
        size = image_file.size/(1024**2)
        file_details = {"File name":image_file.name,
                        "File size":"{:,.2f} MB".format(size),
                        "File-type":image_file.type}
        #st.json(file_details)
        if file_details['File-type'] in ('image/png','image/jpeg'):
            st.success("File Uploaded")
            path = os.path.join('./Uploads', image_file.name)
            with open(path, mode='wb') as f:
                f.write(image_file.getbuffer())
            return {"Image":image_file,
                    "File_details":file_details}
        else:
            st.error("Invalid File type")
            return None

def main():
    obj = Upload_Image()
    if obj:
        prediction = False
        image_obj = Image.open(obj['Image'])

        col1,col2 = st.columns(2)

        with col1:
            st.info("Image Preview")
            st.image(image_obj)

        with col2:
            st.subheader("File Details")
            st.json(obj['File_details'])
            button = st.button(label="Get Prediction")
            if button:
                with st.spinner("Processing"):
                    image_array = np.array(image_obj)
                    pred_image = yolo.predictions(image_array)
                    pred_image_obj = Image.fromarray(pred_image)
                    prediction = True

        if prediction:
            st.subheader("Predicted Image from YOLO V5 Model")
            st.image(pred_image_obj)



if __name__ =='__main__':
    main()
