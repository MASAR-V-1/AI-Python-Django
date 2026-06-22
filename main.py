from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

user_question = input("How can I help you ?  ")

print("\n Loading...")


chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant."
    ),
    contents=user_question,
)
print("مرحباً بك في شات مَسَار الذكي! (اكتب 'exit' للخروج)\n")

# 3. حلقة تكرارية لاستمرار النقاش دون فقدان الذاكرة
while True:
    user_question = input("أنا: ")
    
    # شرط للخروج من البرنامج
    if user_question.lower() in ['exit', 'quit', 'خروج']:
        print("مع السلامة!")
        break
        
    if not user_question.strip():
        continue
        
    print("\nجاري التفكير...")
    
    # الإرسال عبر الـ chat.send_message هو السر في حفظ الذاكرة والسياق!
    response = chat.send_message(user_question)
    
    print(f"\nمَسَار: {response.text}\n")
    print("-" * 30)
# print("\nThe answer :")
# print(chat.text)
# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, max_tokens=1000)
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.7, max_tokens=1000)

