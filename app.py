import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def connect_data_csv():
     # Set the option for pandas Styler
    pd.set_option("styler.render.max_elements", 4333280)
    st.header("Streamlit Connect Tutorial")

    data = pd.read_csv("data/s&p500.csv")
    st.dataframe(data)

    # st.dataframe(data.style.highlight_max(axis=0))

# Display some text in streamlit
def display_write():
    st.header("Streamlit Text Display")
    st.title("Title of my app")
    st.header("Header of my app")
    st.subheader("Sub-Header of my app")
    st.text("Any Text Here")
    st.caption("Any Info Here")

    code = """def hello():
    print("Hello, Streamlit)"""
    st.code(code, language='python')

    st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"HTML text green"}</h1>',unsafe_allow_html=True)

def display_media():
    st.header('Streamlit display media tutorial')

    st.subheader("Image Tutorial")
    image = Image.open("images/404error.jpg")
    st.image(image, caption='@joekillelea', width=200)

    st.subheader('Audio Tutorial')
    audio_file = open('audio/intro.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/intro.mp3')

    st.subheader("Video Tutorial")
    video_file = open("video/beach-video.mp4", 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/beach-video.mp4')
    
def layout():
    st.header('Streamlit Layout Tutorial')

    # Sidebar
    st.sidebar.title('Sidebar Title')
    st.sidebar.write('You can add components by applying here')
    st.sidebar.metric(label="Sidebar temperature", value="25 degrees", delta="2.1")

    # Columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("First Column is a Cat!!")
        st.image("https://static.streamlit.io/examples/cat.jpg")



    with col2:
        st.header("Second Column is a Owl!!")
        st.image("https://static.streamlit.io/examples/owl.jpg")







if __name__ == "__main__":
    st.set_page_config(
        page_title = "Streamlit",
        layout="centered"
    )

    st.title("Streamlit basic app")

    connect_data_csv()
    display_write()
    display_media()
    layout()
