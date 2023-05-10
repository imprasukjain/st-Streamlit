import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from Yolo_Prediction_file import YOLO_Pred

st.set_page_config(page_title='Real Time Object Detection',layout='wide',page_icon='./images/camera.png')

yolo = YOLO_Pred(onnx_model='./model/best.onnx', data_yaml='./model/data.yaml')
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    #flipped = img[::-1,:,:]
    img_pred = yolo.predictions(img)



    return av.VideoFrame.from_ndarray(img_pred, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback,media_stream_constraints={"video":True,"audio":False})