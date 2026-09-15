from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-2-preview',
    output_dimensionality=128

)

result = embedding.embed_query("Capital of India is Delhi")

print(result)