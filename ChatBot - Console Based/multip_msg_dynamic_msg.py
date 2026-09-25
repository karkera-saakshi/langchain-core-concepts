from langchain.messages import SystemMessage, AIMessage, HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

domain = input("Please enter the domain you want the AI act for: ")
topic = input("Please enter your topic: ")

prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a " + domain+ " expert"),
    ('human', "Teach me "+ topic)
])

msg = prompt.invoke({
    "domain": domain,
    "topic": topic
})

result = model.invoke(msg)

print(result.text)