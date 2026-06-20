from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
from google import genai

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=API_KEY)

user_question = input("How can I help you ?  ")

print("\n Loading...")


response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=user_question,
)

print("\nThe answer :")
print(response.text)
# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, max_tokens=1000)
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.7, max_tokens=1000)
