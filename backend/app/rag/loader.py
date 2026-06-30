from pathlib import Path
from langchain_core.documents import Document

files = list(Path("data/ai-engineering-notes/").rglob("*.md"))


def load_documents(folder: str):
    docs = []
    notes_root = Path(folder)

    for file_path in notes_root.rglob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        metadata = {
            "source": str(file_path.relative_to(notes_root)),
            "topic": file_path.parent.name,
            "filename": file_path.name,
        }

        docs.append(Document(page_content=text, metadata=metadata))

    return docs


if __name__ == "__main__":
    docs = load_documents("data/ai-engineering-notes")
    print(len(docs))
    print(docs[0].metadata)
