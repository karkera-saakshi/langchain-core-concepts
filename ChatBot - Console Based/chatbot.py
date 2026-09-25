from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash')

while True:
    user_input = input("You: ")
    print("DEBUG: input received")
    if user_input == "exit":
        print("exiting")
        break;
    result = model.invoke(user_input)
    print(result.text);