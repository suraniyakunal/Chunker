from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(docs)

    for idx, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = idx

    return chunks


if __name__ == "__main__":
    from loader import load_documents

    docs = load_documents("data/ai-engineering-notes")
    chunks = split_documents(docs)

    print(len(chunks))
    print(chunks[0].page_content)
    print(chunks[0].metadata)
