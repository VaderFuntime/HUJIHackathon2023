import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Display the header with dark gray background and white text
st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
    }
    </style>
    <div style="background-color: #303030; padding: 10px;">
        <h1 style="color: white; text-align: center; font-size: 48px; font-weight: bold;">
            תא וידויים
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

def process_button_click():
    # Call your function here to get the URL and text
    # Replace the following placeholders with the actual URL and text
    image_url = "http://www.google.com.au/images/nav_logo7.png"  # Replace with the actual image URL
    text = "Text"  # Replace with the actual text

    # Download the image from the URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Display the image and text in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Image", use_column_width=True)
    with col2:
        st.write(text)

# Display the form with a button and an initial image
button_alignment_style = """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
    }
    </style>
"""

initial_image_url = "https://media.istockphoto.com/id/1049784606/photo/confession-of-sins-room-inside-of-jesuitenkirche-church.jpg?s=612x612&w=0&k=20&c=i7NGtaIeRKo16_B2m1jOj7YuNqm7wr2vLlRUE56r41A="

st.markdown(button_alignment_style, unsafe_allow_html=True)

submitted = st.button("תתוודה", key="submit_button")

if submitted:
    process_button_click()
else:
    st.markdown(
        f'<div class="image-container"><img src="{initial_image_url}" style="width: 500px;"></div>',
        unsafe_allow_html=True
    )
