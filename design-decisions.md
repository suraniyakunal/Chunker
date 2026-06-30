# Design Decisions

A running log of structural decisions made while building this project, why
they were made, and what they trade off. Written as the decisions were
actually made — not reconstructed afterward.

---

## Chunking strategy: RecursiveCharacterTextSplitter, chunk_size=1000, chunk_overlap=200

**Decision:** Use LangChain's `RecursiveCharacterTextSplitter` rather than a
fixed-size or purely character-based splitter, with a 1000-character chunk
size and 200-character overlap.

**Why:** Recursive splitting tries to break text at paragraph boundaries
first, then sentences, then lines, then words, then characters — only
falling back to a "blind" cut when necessary. This preserves semantic
meaning far better than chunking at a fixed character count regardless of
content structure.

The size (1000/200) is larger than a typical "resume bullet point" chunk
size (e.g. 500/100) because technical notes contain longer explanatory
paragraphs — cutting too aggressively risks splitting an idea mid-thought.

**Trade-off:** Larger chunks mean fewer, cheaper embedding calls, but each
chunk has somewhat less retrieval precision than smaller chunks would. This
is a starting heuristic, not a tuned final value — would benefit from
measuring retrieval quality at a few different sizes (500/800/1000/1500)
against a fixed set of test queries.

---

## Finding: retrieval quality is bottlenecked by corpus coverage, not pipeline correctness

**What happened:** First real test query ("What is cosine similarity?")
against a 6-file corpus returned three results, all from the same unrelated
file (`what-problems-llm-solved.md`) — none of which actually answered the
question.

**Diagnosis process:** Rather than assuming the pipeline was broken,
checked which source files the results came from. All three pointed to the
same file, suggesting the database simply had no chunk that better matched
the query — not a retrieval logic bug.

**Confirmation:** Added a new, focused notes file (`tradeoffs.md`) covering
a topic not previously in the corpus, re-ingested, and re-queried with a
question relevant to the new content. Retrieval correctly returned
on-topic, on-file results.

**Takeaway:** A RAG pipeline can be functioning correctly end-to-end and
still produce low-relevance results — silently, with no error — if the
underlying corpus doesn't actually contain the answer. Retrieval quality is
a function of both the pipeline *and* the data; debugging "bad answers"
requires checking both before assuming the code is at fault.

---

## Fix: clear the vector store before rebuilding (idempotent ingestion)

**What happened:** After running `vectorstore.py` multiple times during
testing, a query returned the same chunk_id twice in the top-3 results.

**Diagnosis:** `Chroma.from_documents()` appends new embeddings to the
existing `persist_directory` rather than replacing its contents. Repeated
test runs had been quietly accumulating duplicate copies of the same
chunks.

**Fix:** `ingest.py` now deletes the existing `chroma_db/` directory (if
present) before rebuilding, via `shutil.rmtree()`. This makes ingestion
idempotent — safe to re-run any number of times without accumulating
duplicates, which matters in particular as the notes corpus grows and
ingestion needs to be re-run regularly.

---

## Generation prompt: restrict answers strictly to retrieved context

**Decision:** The prompt sent to Gemini's chat model explicitly instructs
it to answer *only* using the provided context, and to say so clearly if
the context doesn't contain enough information — rather than allowing it to
fall back on its own general knowledge.

**Why:** Without this constraint, the system stops being a RAG system in
any meaningful sense — it becomes a general-purpose chatbot that happens to
have some extra reading material. The entire value of RAG (grounded,
source-traceable, low-hallucination answers) depends on enforcing this
boundary explicitly in the prompt; it isn't automatic just because context
was retrieved and included.

**Trade-off:** This means the system will sometimes correctly say "I don't
know" rather than giving a plausible-sounding but ungrounded answer — which
is the intended behavior for this use case, even though it makes the system
"less helpful" in the narrow sense of always producing an answer.

---

## Provider choice: Google Gemini free tier (not OpenAI)

**Decision:** Use Gemini for both embeddings (`gemini-embedding-001`) and
generation (`gemini-2.5-flash`), rather than OpenAI.

**Why:** No budget for paid APIs. Gemini's free tier is usable for both
embeddings and chat generation without a credit card, keeping the entire
project buildable and runnable at zero cost.

**Trade-off:** Free-tier rate limits (requests per minute / per day) are
real constraints during development — repeated rapid testing can trigger
429 errors. This is a known, expected limitation of building on a free
tier, not a pipeline bug.
