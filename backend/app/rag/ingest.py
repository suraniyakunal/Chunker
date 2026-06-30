import shutil
from pathlib import Path

from loader import load_documents
from splitter import split_documents
from vectorstore import build_vectorstore

DATA_DIR = "data/ai-engineering-notes"
PERSIST_DIR = "chroma_db"


def run_ingestion():
    if Path(PERSIST_DIR).exists():
        print(f"Removing existing vectorstore at {PERSIST_DIR}")
        shutil.rmtree(PERSIST_DIR)

    print("Loading Documents")
    docs = load_documents(DATA_DIR)
    print(f"Loaded {len(docs)} Documents")

    print("Splitting into chunks")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    print("Embedding Documents")
    build_vectorstore(chunks, persist_directory=PERSIST_DIR)
    print("Ingestion complete.")


if __name__ == "__main__":
    run_ingestion()
