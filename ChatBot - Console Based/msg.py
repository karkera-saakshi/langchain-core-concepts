from langchain.messages import SystemMessage, AIMessage, HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

msg = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain and its usefulness")
]

result = model.invoke(msg)
msg.append(AIMessage(content=result.text))

print(msg)