from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
    )


if __name__ == "__main__":
    model = get_embedding_model()
    vector = model.embed_query("What is cosine similarity")
    print(len(vector))
    print(vector[:5])
