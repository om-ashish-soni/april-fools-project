import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Page Title and Description
st.set_page_config(
    page_title="World's Best Text to Reel Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("World's Best Text to Reel Generator")
st.markdown("Generate amazing animated reels from your text!")

# Sidebar
st.sidebar.header("Settings")
text_color = st.sidebar.color_picker("Choose Text Color", "#ffffff")
bg_color = st.sidebar.color_picker("Choose Background Color", "#0f4c81")
font_size = st.sidebar.slider("Choose Font Size", 20, 100, 40)
animation_speed = st.sidebar.slider("Choose Animation Speed", 0.1, 2.0, 1.0)
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️")

# Input Text Area
st.subheader("Enter your text:")
input_text = st.text_area("", height=150)

# Function to generate reel based on input text
def generate_reel(text, text_color, bg_color, font_size, animation_speed):
    # Here you would have your logic to generate a reel from the input text
    # For the sake of example, let's just echo the input text
    return f"ऐसा कोई टूल नहीं होता , आप April Fool बन चुके हो",'https://i.pinimg.com/originals/89/d8/2d/89d82d75214fbc07a468580938fff8e3.gif'



# Button to generate the reel
if st.button("Generate Reel"):
    if input_text:
        reel_text, reel_image = generate_reel(input_text, text_color, bg_color, font_size, animation_speed)
        st.success(reel_text)
        if reel_image is not None:
            st.image(reel_image, use_column_width=True)
    else:
        st.warning("Please enter some text to generate a reel.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️")

