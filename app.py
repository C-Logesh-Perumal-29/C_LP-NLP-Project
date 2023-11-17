import streamlit as st
import pyttsx3
from PIL import Image,ImageOps

img = Image.open("Icon.png")
st.set_page_config(page_title="Text to Speech",page_icon=img,layout="wide")

# Hide Menu_Bar & Footer :

hide_menu_style = """
    <style>
    #MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    </style>
"""
st.markdown(hide_menu_style , unsafe_allow_html=True)

# Set the background image :

Background_image = """
<style>
[data-testid="stAppViewContainer"] > .main
{
background-image: url("https://img.freepik.com/free-photo/abstract-orange-background-layout-designstudioroom-web-template-business-report-with-smooth-circle-gradient-color_1258-102207.jpg?size=626&ext=jpg&ga=GA1.1.2087154549.1663432512&semt=ais");

background-size : 100%
background-position : top left;
background-position: center;
background-size: cover;
background-repeat : repeat;
background-repeat: round;
background-attachment : local;
background-image: url("https://img.freepik.com/free-photo/abstract-orange-background-layout-designstudioroom-web-template-business-report-with-smooth-circle-gradient-color_1258-102207.jpg?size=626&ext=jpg&ga=GA1.1.2087154549.1663432512&semt=ais");
background-position: right bottom;
background-repeat: no-repeat;
}  

[data-testid="stHeader"]
{
background-color : rgba(0,0,0,0);
}
</style>                                
"""
st.markdown(Background_image,unsafe_allow_html=True)

col1,col2 = st.columns([1,5])

with col1:
    img = Image.open("1.jpg")
    st.image(img)

with col2:
    title_html = f'<p style="color:#03045e; text-align:center;font-family:Eras Bold ITC;font-size:76px;">Text to Speech Web Application</p>'
    st.markdown(title_html, unsafe_allow_html=True)
    
def text_to_speech(text, voice_id):
    engine = pyttsx3.init()

    # Set the voice based on the selected voice_id
    voices = get_available_voices()
    engine.setProperty('voice', voices[voice_id].id)

    engine.say(text)
    engine.runAndWait()

def get_available_voices():
    return pyttsx3.init().getProperty('voices')

def main():

    # Input text box for user input
    text_input = st.text_area("Enter text:", "Hello, how are you today?")

    # Select box for choosing the voice
    voices = get_available_voices()
    voice_id = st.selectbox("Select Voice:", range(len(voices)), format_func=lambda x: voices[x].name)

    # Button to trigger text-to-speech conversion
    if st.button("Convert to Speech"):
        text_to_speech(text_input, voice_id)

if __name__ == "__main__":
    main()
