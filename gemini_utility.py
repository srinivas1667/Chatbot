import os
import json

import google.generativeai as genai

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# loading the api key
GAK = config_data["GOOGLE_API_KEY"]

# configuring google.generatveai with API key
genai.configure(api_key=GAK)

# function to load gemini-pro-model for chatbot
def load_gem_model():
    gemini_pro_model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    return gemini_pro_model


# function for image captioning
def gemini_pro_vision_response(prompt,image):
    gemini_pro_vision_model = genai.GenerativeModel(model_name="gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt,image])
    result = response.text
    return result

# funciton to get embeddings for text

def embedding_model_response(input_text):
    embedding_model = 'models/embedding-001'
    embedding = genai.embed_content(model=embedding_model,content=input_text,task_type="retrieval_document")

    embedding_list = embedding['embedding']
    return embedding_list


# function to get a response to a question

def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result








