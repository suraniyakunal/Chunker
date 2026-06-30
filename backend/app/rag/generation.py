from langchain_google_genai import ChatGoogleGenerativeAI


def get_chat_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
    )


def generate_answer(query, retrieved_chunks):
    chat_model = get_chat_model()

    context = "\n\n---\n\n".join(chunk.page_content for chunk in retrieved_chunks)

    prompt = f"""Answer the question using only the context below.
    If the context doesn't contain enough information, say so clearly instead of guessing
    Context:
     {context}

    Question: {query}

    Answer:"""

    response = chat_model.invoke(prompt)
    return response.content


if __name__ == "__main__":
    from vectorstore import build_vectorstore
    from loader import load_documents
    from splitter import split_documents

    docs = load_documents("data/ai-engineering-notes")
    chunks = split_documents(docs)
    vectorstore = build_vectorstore(chunks)

    query = "What's the tradeoff between RAG and fine-tuning"
    retrieved = vectorstore.similarity_search(query, k=3)

    answer = generate_answer(query, retrieved)
    print(answer)
