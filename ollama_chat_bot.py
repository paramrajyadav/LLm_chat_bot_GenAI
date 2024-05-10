import streamlit as st
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"



prompt=ChatPromptTemplate.from_messages(

    [
        ("system","you are a helpful assistant.Please provide response to the user question"),
        ( "user","Question: {question}")
    ]
)


# streamlit Framework

st.title("Langchain Demo with Ollama_Gemma:2B API")
input_text=st.text_input("Search the topic you want")

# Open AI LLM call

# llm=ChatOpenAI(model="gpt-3.5-turbo")
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


