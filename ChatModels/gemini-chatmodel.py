import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash')

result = model.invoke("What is the capital of India?")

print(result)