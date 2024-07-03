import streamlit as st
import os
from streamlit_option_menu import option_menu
from PIL import Image

from gemini_utility import (load_gem_model,
                            gemini_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)




working_directory = os.path.dirname(os.path.abspath(__file__))


# setting the pade configuration
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🌠",
    layout="centered"
)

with st.sidebar:

    selected = option_menu(

        menu_title="Gemini AI",
        options=["Chatbot", "Image captioning", "Embed Text", "Ask me anything"],
        menu_icon='robot', icons=["chat-left", "image-fill", "braces", "person-raised-hand"],
        default_index=0

    )

# function to translate role bwn gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role


if selected == "Chatbot":

    model = load_gem_model()
    # initialize chat session in streamlit
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # streamlit page_title
    st.title("🤖 Chatbot")

    # Disply the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)


    # input field for user message
    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Diplay the geimini pro response

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)



# Image Captioning page

if selected == 'Image captioning':

    # streamlit page title
    st.title(" Image Captioner")

    uploaded_image = st.file_uploader(" Upload an image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1,col2 = st.columns(2)

        with col1:
            resized_image = image.resize(((800,500)))
            st.image(resized_image)

        deafult_prompt = " write a creative short caption for this to be posted on instagram "

        # getting the response

        caption = gemini_pro_vision_response(deafult_prompt,image)

        with col2:
            st.info(caption)


# Text Embedding

if selected == "Embed Text":
    st.title(" 🖹 embed text")

    # Text to enter
    input_text = st.text_area(label='',placeholder='Enter the text to get the embeddings')

    if st.button('Get Embedding'):
        response = embedding_model_response(input_text)
        st.markdown(response)



# Ask me anything

if selected == "Ask me anything":

    st.title("Ask me anything ")

    # text box to enter prompt

    user_prompt = st.text_area(label="",placeholder="ask me")

    if st.button("Get an answer"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)

