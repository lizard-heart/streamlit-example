import streamlit as st
import numpy as np
import cv2
from PIL import Image
import tempfile
import os
import time
import model

st.title("YOLO Demo")
st.header("Drag and drop any image or video to test the YOLO model")

uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "mp4", "mov"])
if uploaded_file is not None:
  if uploaded_file.type.startswith("image"):
    image = Image.open(uploaded_file)
    st.image(model.detect_image(image))
  else:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    path = f'/content/user/{uploaded_file.name}'
    detected_path = f'/content/user/{uploaded_file.name.partition(".")[0]}_detected.{uploaded_file.name.partition(".")[2]}'

    try:
      model.detect_video(tfile.name, path)

      progress = st.empty()
      progress.text('Encoding...')
      os.system(f"ffmpeg -y -i {path} -vcodec libx264 {detected_path}")
      time.sleep(1)
      progress.empty()

      os.remove(path)
      st.video(detected_path)
      os.remove(detected_path)
    except:
      st.write("ERROR")
      os.remove(path)
      os.remove(detected_path)
