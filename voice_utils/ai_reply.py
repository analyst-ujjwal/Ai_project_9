import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Please set it in your .env file.")

# ✅ LLaMA 70B – best for conversational reasoning
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",  
    temperature=0.6,
    max_tokens=600
)

def generate_ai_reply(user_text: str) -> str:
    """Generate conversational reply using Groq LLaMA."""
    messages = [HumanMessage(content=f"User said: {user_text}. Respond naturally and concisely.")]
    response = llm.invoke(messages)
    return response.content
