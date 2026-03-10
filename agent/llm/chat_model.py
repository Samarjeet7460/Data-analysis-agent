"""
IMPORTANT!

this file contain the llm for building the agent brain (reasoning + planning).
the default propmt is in prompt/system_prompt.py folder.


how to run:

import the model into your file.
ex: from agent.llm.chat_model import model

after importing the model, run:
response = model.invoke("your_question_here").content

the response variable stores the model generated resposnse 

"""



from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from prompts.system_prompts import system_prompt

try:
    load_dotenv()
except Exception as e:
    raise RuntimeError(f"Failed to load environment variables: {e}")

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL_NAME = os.getenv('MODEL_NAME')

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")
if not MODEL_NAME:
    raise ValueError("MODEL_NAME environment variable is not set")

try:
    llm = ChatGroq(api_key=GROQ_API_KEY, model_name=MODEL_NAME, temperature=0.7, max_tokens=2048)
except Exception as e:
    raise RuntimeError(f"Failed to initialize ChatGroq model: {e}")

try:
    model = system_prompt | llm 
except Exception as e:
    raise RuntimeError(f"Failed to invoke model: {e}")


# how to run:
# response = model.invoke("hello, how are you").content
# print(response)