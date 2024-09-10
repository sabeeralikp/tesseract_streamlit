import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import numpy as np


def pdf_2_image(pdf_file):
    images = convert_from_bytes(pdf_file)
    return images


def get_language(lang):
    if lang == "English":
        return "mala"
    elif lang == "Malayalam":
        return "mal"
    elif lang == "Hindi":
        return "hin"
    else:
        return "mal"


st.title("Optical Character Recognition")
selected_language = st.selectbox(
    "Select Language of File", options=["English", "Malayalam", "Hindi"]
)
upload_file = st.file_uploader(
    "choose pdf or image", type=["jpeg", "jpg", "png", "pdf"]
)

condition = st.button("convert")
if condition:
    if upload_file is not None:
        text = ""
        if upload_file.type == "application/pdf":
            images = pdf_2_image(upload_file.getbuffer())
            for image in images:
                col1, col2 = st.columns(2)
                image = np.array(image)
                with col1:
                    st.image(image)
                with col2:
                    text = pytesseract.image_to_string(
                        image, lang=get_language(selected_language)
                    )
                    st.text(text)
                    with open("text.txt", "a+") as f:
                        f.write(text)

        else:
            col1, col2 = st.columns(2)
            with col1:
                st.image(upload_file.read())
            with col2:
                image = Image.open(upload_file)
                text = pytesseract.image_to_string(
                    image, lang=get_language(selected_language)
                )
                st.text(text)
                with open("text.txt", "w+") as f:
                    f.write(text)

    else:
        st.warning("No file given")
else:
    st.warning("Please upload a file")
