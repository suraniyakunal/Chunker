from langchain_chroma import Chroma


def build_vectorstore(chunks, persist_directory="chroma_db"):
    from embeddings import get_embedding_model

    embedding_model = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    return vectorstore


if __name__ == "__main__":
    from loader import load_documents
    from splitter import split_documents

    docs = load_documents("data/ai-engineering-notes")
    chunks = split_documents(docs)

    vectorstore = build_vectorstore(chunks)

    results = vectorstore.similarity_search("What are the tradeoffs in llm?", k=3)

    for r in results:
        print(r.metadata)
        print(r.page_content[:200])
        print("---")
