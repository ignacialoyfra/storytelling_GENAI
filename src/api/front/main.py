from click import prompt
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.api.back.prompts import prompt_creative, prompt_dark, prompt_funny, prompt_inspirational, prompt_melancholic, prompt_romantic
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI
from src.api.back.model import model, tokenizer


st.set_page_config(
    page_title="Storytelling",                 
    layout="wide",
    page_icon=":sparkles:",                      
    initial_sidebar_state="expanded"    
)
st.header("Sube tu imagen y crea tu propio Storytelling ✨🌺🌃")
st.subheader("Deja fluir tu imaginación con un tono de creatividad :art:")
input_id = "user_input"
menu = ["Creativo","Oscuro","Divertido","Romántico","Melancólico","Inspirador"]
choice = st.selectbox("Selección de tono del storytelling",menu,placeholder="Selección")
temp = st.slider("Temperatura del modelo",min_value=0.0,max_value=1.0,value=0.5,step=0.01)
model_openai = OpenAI(temperature=temp)
user_input = st.text_input("Ingresa el nombre de tu producto/marca:",key=input_id)
uploaded_file = st.file_uploader("Sube tú imagen", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    enc_image = model.encode_image(image)
    response_description_image = model.answer_question(enc_image, "Describe this image.", tokenizer)
    st.success("Descripción de la imagen obtenida exitosamente")
    st.write(response_description_image)
    
else:
    st.write("No ha subido ninguna imagen")
    
    
if st.button("Crear Storytelling"):
    # Mostrar el valor ingresado cuando se presione el botón
    st.write(f"Has ingresado: {user_input}")
    if choice == "Creativo":
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_creative,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
    
    elif choice == "Oscuro":
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_dark,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
        
    elif choice == "Divertido":
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_funny,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
        
    elif choice == "Romántico":
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_romantic,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
    
    
    elif choice == "Melancólico":
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_melancholic,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
    
    else:
        chain_creative = LLMChain(llm = model_openai, prompt= prompt_inspirational,output_parser=StrOutputParser())
        response_creative = chain_creative.run(brand=user_input,description=response_description_image)
        st.write(response_creative)
        
          

