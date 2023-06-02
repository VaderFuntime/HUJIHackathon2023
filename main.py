import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import conf_and_img_generator

def process_button_click():
    # Call your function here to get the URL and text
    # Replace the following placeholders with the actual URL and text

    conf, img_url = conf_and_img_generator.generate_conf_and_img()

    # Download the image from the URL
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))

    # Display the image and text in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, use_column_width=True)
    with col2:
        st.markdown(f'<div style="text-align: right;">{conf}</div>', unsafe_allow_html=True)

# Display the header with dark gray background and white text
st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
    }
    </style>
    
    <div style="background-color: #303030; padding: 10px;">
        <h1 style="color: white; text-align: center; font-size: 48px; font-weight: bold;">
            HujiPT
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)



# Display the form with a button and an initial image
initial_image_url = "https://i.ibb.co/yhF1DrT/logo.png"

submitted = st.button("מה אומר", key="submit_button")
st.markdown('<style>div.stButton > button{width: 100%;}</style>', unsafe_allow_html=True)

if submitted:
    process_button_click()
else:
    st.markdown(
        f'<div class="image-container"><img src="{initial_image_url}" style="width: 500px;"></div>',
        unsafe_allow_html=True
    )



