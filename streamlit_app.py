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
