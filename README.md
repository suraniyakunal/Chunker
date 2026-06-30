# Notes RAG — Retrieval-Augmented Generation over My AI Engineering Notes

A small, fully self-built RAG (Retrieval-Augmented Generation) system that
answers questions using my own [ai-engineering-notes](https://github.com/suraniyakunal/ai-engineering-notes)
as its knowledge base — instead of re-reading old notes, I can query them
directly and get a grounded, source-backed answer.

Built from scratch (no boilerplate templates) to actually understand every
piece of a RAG pipeline: loading, chunking, embedding, vector storage,
retrieval, and grounded generation — using a free-tier LLM stack only.

---

## What it does

1. Loads every markdown file from a notes repository.
2. Splits each file into overlapping chunks, preserving source metadata
   (file, topic folder, chunk index).
3. Generates embeddings for each chunk using Google's Gemini embedding model.
4. Stores chunks + embeddings in a local Chroma vector database.
5. On a query: retrieves the most relevant chunks via similarity search,
   then passes them to Gemini's chat model with a strict instruction to
   answer **only** from the provided context — reducing hallucination and
   making "I don't know" a valid, expected answer when the notes don't
   cover something.

**Example:**

```
Query: "What's the tradeoff between RAG and fine-tuning?"

Answer: The tradeoff between RAG and fine-tuning is that RAG is ideal for
dynamic knowledge, frequently changing information, access to private
documents, reducing hallucinations, and needing the latest information.
Fine-tuning, on the other hand, is better for learning new behaviors,
adopting a specific writing style, needing consistent behavior across
prompts, following a specific format, and task-specific behavior.
```

---

## Architecture

```
ai-engineering-notes/ (markdown files)
        │
        ▼
   loader.py        — reads .md files, attaches metadata (source, topic, filename)
        │
        ▼
   splitter.py       — RecursiveCharacterTextSplitter, chunk_size=1000, overlap=200
        │
        ▼
   embeddings.py     — Gemini gemini-embedding-001 (3072-dim vectors)
        │
        ▼
   vectorstore.py    — Chroma: stores chunks + embeddings, runs similarity search
        │
        ▼
   ingest.py         — orchestrates the full pipeline, clears + rebuilds the
                        vector store on each run (idempotent)
        │
        ▼
   generation.py     — retrieves relevant chunks for a query, grounds a
                        Gemini chat prompt in them, returns the answer
```

Each file has exactly one responsibility — `ingest.py` is the only file
that knows about the full pipeline; every other file can be tested and
understood in isolation.

---

## Tech stack

- **Python**
- **LangChain** (document loading, text splitting, provider integrations)
- **Google Gemini API** (free tier) — `gemini-embedding-001` for embeddings,
  `gemini-2.5-flash` for generation
- **Chroma** — local vector database
- **python-dotenv** — environment variable management

No paid APIs. No local LLM inference (kept lightweight for low-resource
hardware).

---

## Setup

```bash
git clone <this-repo-url>
cd backend

python -m venv venv
source venv/bin/activate

pip install langchain langchain-community langchain-google-genai langchain-chroma chromadb python-dotenv
```

Create a `.env` file in `backend/`:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get a free key at [aistudio.google.com](https://aistudio.google.com) — no
credit card required.

Clone your notes (or any markdown corpus) into `backend/data/`:

```bash
cd data
git clone https://github.com/suraniyakunal/ai-engineering-notes.git
```

---

## Usage

Run ingestion (loads, chunks, embeds, and stores everything — safe to
re-run anytime, rebuilds cleanly):

```bash
python app/rag/ingest.py
```

Query the system:

```bash
python app/rag/generation.py
```

(Edit the `query` variable in `generation.py`'s test block, or extend it
into a CLI loop — see Roadmap below.)

---

## Design decisions

Full reasoning log in [`design-decisions.md`](./design-decisions.md).
A few highlights:

- **Chunk size 1000 / overlap 200**: notes are explanatory and longer-form
  than something like resume bullet points, so a larger chunk size keeps
  related ideas together; overlap preserves context across chunk
  boundaries.
- **Retrieval quality is bottlenecked by corpus coverage, not just
  pipeline correctness.** An early test query returned irrelevant results
  — not because of a bug, but because no chunk in the (then 6-file) corpus
  actually covered that topic. Confirmed by adding relevant notes and
  re-querying successfully. A RAG system can fail silently (return
  low-relevance results without erroring) when the answer simply isn't in
  the data — worth designing for.
- **`ingest.py` clears the existing vector store before rebuilding.**
  Without this, re-running ingestion appends duplicate chunks to Chroma
  instead of replacing them — discovered via a real duplicate-result bug
  during testing.
- **Generation prompt explicitly restricts answers to retrieved context**,
  and instructs the model to say so when context is insufficient, rather
  than guessing — a deliberate hallucination guardrail.

---

## Roadmap

- [ ] Simple CLI loop for interactive querying
- [ ] Deploy a minimal Streamlit/web interface
- [ ] Tune chunk size based on measured retrieval quality, not just defaults
- [ ] Extend with an agent layer (LangGraph) — decide when to retrieve vs.
      answer directly, add tool-calling (e.g. web search fallback)

---

## Notes

This project is built and understood line-by-line — every file was written
with explanations for each piece, not generated wholesale. All design
decisions above were genuinely hit, diagnosed, and fixed during
development, not written in retrospect.
