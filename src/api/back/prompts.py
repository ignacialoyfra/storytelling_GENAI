from langchain.prompts import PromptTemplate
import os
import sys
from .templates import *
prompt_creative = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

prompt_dark = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

prompt_funny = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

prompt_romantic = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

prompt_melancholic = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

prompt_inspirational = PromptTemplate(
    input_variables=["brand","description"],
    template=template_creative
)

