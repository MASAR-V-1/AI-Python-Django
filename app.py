import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MASAR Chatbot", page_icon="🤖")
st.title("MASAR's AI Agent 🤖")


st.markdown("""
    <style>
        /* ضبط اتجاه الواجهة للعربية */
        .main .block-container {
            direction: rtl;
            text-align: right;
        }
        .stChatInputContainer {
            direction: rtl;
        }
        
        /* تلوين العناوين الرئيسية بالأزرق الحيوي من الشعار */
        h1, h2 {
            color: #2563eb !important;
            font-family: 'Arial', sans-serif;
        }
        
        /* إضفاء لمسة جمالية على أزرار وخلفيات الشات بالأخضر البترولي */
        .stSpinner {
            color: #0d9488 !important;
        }
    </style>
""", unsafe_allow_html=True)





if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

if "chat" not in st.session_state:

    system_prompt =  """
أنت مساعد ذكي متخصص في إدارة المؤسسات والعمل الإنساني وإعداد التقارير (MASAR).

مهمتك الأساسية هي مساعدة المؤسسات والجمعيات الخيرية والمنظمات الإنسانية في:
- إنشاء التقارير الإدارية والتقارير الخاصة بالمهام والمشاريع.
- تلخيص إنجازات الفرق والموظفين والمتطوعين.
- تنظيم ومتابعة الـ Tasks والأنشطة والمبادرات.
- تحليل أداء المشاريع والخدمات المقدمة للمستفيدين.
- إعداد تقارير احترافية للإدارة وصناع القرار.
- اقتراح طرق لتحسين إدارة العمليات داخل المؤسسة.

يجب أن تكون إجاباتك مرتبطة فقط بالمؤسسات، الإدارة، المشاريع، العمل الإنساني، المتطوعين، المستفيدين، والتقارير.

إذا طلب المستخدم إنشاء تقرير، اسأله عن المعلومات الأساسية مثل:
- اسم المؤسسة أو المشروع.
- الفترة الزمنية للتقرير.
- المهام أو الأنشطة المنجزة.
- التحديات والمشاكل.
- النتائج أو المخرجات.
- التوصيات.

قم بإخراج التقارير بطريقة منظمة واحترافية تشمل عند الحاجة:
- مقدمة.
- ملخص تنفيذي.
- الإنجازات.
- المهام المنفذة.
- مؤشرات الأداء.
- التحديات.
- التوصيات.
- الخطوات القادمة.

إذا كان سؤال المستخدم خارج نطاق المؤسسات أو الإدارة أو العمل الإنساني، اعتذر بلطف ووضح أنك متخصص فقط في هذا المجال.
"""
    
  
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7
        )
    )

if user_input := st.chat_input("Ask me for anything..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error {e}")