# 📖 Glossary

This glossary covers the most common terms you'll encounter while learning Large Language Models (LLMs), AI Engineering, Retrieval-Augmented Generation (RAG), and AI Agents.

---

# A

## Attention

A mechanism in transformer models that allows the model to focus on the most relevant parts of the input while generating the next token.

Instead of treating every word equally, attention assigns different importance to each word depending on the current context.

### Example

Sentence:

> The dog chased the cat because **it** was scared.

Attention helps the model understand that **"it"** refers to **the cat**.

---

# C

## Chunk

A smaller section of a larger document.

Since embedding models have context limits, large documents are split into chunks before being embedded.

### Example

Original document

```
A 100-page PDF
```

Chunks

```
Chunk 1 → Pages 1–3
Chunk 2 → Pages 4–6
Chunk 3 → Pages 7–9
...
```

Good chunking improves retrieval quality.

---

## Chunk Overlap

A technique where part of one chunk is repeated in the next chunk.

This preserves context that might otherwise be lost during splitting.

### Example

Chunk 1

```
Machine Learning is a subset of AI.
Deep Learning is a subset...
```

Chunk 2

```
Deep Learning is a subset...
Neural Networks...
```

The repeated text helps maintain continuity.

---

## Context Window

The maximum amount of information an LLM can process in a single request.

Measured in **tokens**, not words.

### Examples

- 8K tokens
- 32K tokens
- 128K tokens
- 1M tokens

A larger context window allows the model to reason over longer documents and conversations.

---

## Cosine Similarity

A mathematical measure used to determine how similar two vectors are.

It compares the **direction** of vectors rather than their magnitude.

### Score Range

| Score | Meaning |
|--------|---------|
| 1 | Exactly similar |
| 0 | Unrelated |
| -1 | Opposite direction |

Cosine similarity is commonly used during semantic search.

---

# D

## Dense Vector

A numerical representation of data where every dimension contains a value.

Example

```
[0.14, -0.82, 0.55, ...]
```

Embeddings are dense vectors.

---

# E

## Embedding

A numerical representation of text that captures semantic meaning.

Instead of storing words directly, the model converts them into vectors.

### Example

Text

```
Artificial Intelligence
```

Embedding

```
[0.42, -0.71, 0.18, ...]
```

Texts with similar meanings produce vectors that are close together in vector space.

---

## Embedding Model

A model specifically trained to convert text into embeddings.

Unlike chat models, embedding models are optimized for semantic similarity.

### Examples

- text-embedding-3-small
- text-embedding-3-large
- BAAI/bge-small-en
- all-MiniLM-L6-v2

---

# F

## Fine-Tuning

The process of training a pre-trained model on additional task-specific data.

Unlike RAG, fine-tuning changes the model's internal weights.

Use fine-tuning when you want the model to consistently learn a new behavior or style.

---

# H

## Hallucination

When an LLM confidently generates information that is incorrect, fabricated, or unsupported.

### Example

Inventing a fake research paper or citing a nonexistent source.

Hallucinations are one of the primary reasons RAG systems are used.

---

# I

## Inference

The process of using a trained model to generate predictions or responses.

Training builds the model.

Inference uses the model.

---

# L

## LLM (Large Language Model)

An AI model trained on massive amounts of text to understand and generate human language.

LLMs are capable of:

- Answering questions
- Writing code
- Summarizing text
- Translation
- Reasoning
- Content generation

### Popular Examples

- GPT
- Claude
- Gemini
- Llama
- Mistral

---

# M

## Metadata

Additional information stored alongside a document.

Metadata helps filter or organize search results.

### Example

```json
{
  "author": "Kunal",
  "source": "Documentation",
  "topic": "RAG",
  "created_at": "2026-06-30"
}
```

Metadata is frequently used in vector databases.

---

# P

## Prompt

The instructions provided to an LLM.

### Example

```
Explain Retrieval-Augmented Generation like I'm a beginner.
```

The quality of a prompt can significantly influence the output.

---

## Prompt Engineering

The practice of designing prompts that produce better, more reliable responses from an LLM.

Common techniques include:

- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Chain-of-thought prompting
- Role prompting

---

# R

## RAG (Retrieval-Augmented Generation)

A technique that combines information retrieval with language generation.

Instead of relying only on the model's training data, relevant documents are retrieved first and then supplied as context to the LLM.

### Workflow

```
User Question
      ↓
Create Query Embedding
      ↓
Vector Search
      ↓
Retrieve Relevant Chunks
      ↓
Provide Context to LLM
      ↓
Generate Answer
```

RAG improves factual accuracy and reduces hallucinations.

---

## Retrieval

The process of finding relevant information from a knowledge base.

Retrieval is typically performed using embeddings and vector similarity search.

---

## Reranking

An optional step performed after retrieval.

A reranker evaluates the retrieved documents again and sorts them by relevance.

This often improves answer quality by selecting the best context.

---

# S

## Semantic Search

Searching based on meaning instead of exact keyword matches.

### Example

Query

```
How do airplanes stay in the air?
```

Retrieved Document

```
Aircraft generate lift using their wings...
```

Even though the word "airplane" doesn't appear exactly, the meanings are similar.

---

## Similarity Search

Finding vectors that are closest to a query vector.

Most vector databases perform similarity search using:

- Cosine Similarity
- Dot Product
- Euclidean Distance

---

# T

## Token

The smallest unit processed by an LLM.

Tokens are not always full words.

### Example

The word

```
Unbelievable
```

may be tokenized as

```
Un
believ
able
```

depending on the tokenizer.

---

## Tokenization

The process of converting text into tokens before the model processes it.

Different models may use different tokenizers.

---

# V

## Vector

A list of numbers representing semantic meaning.

Example

```
[0.33, -0.18, 0.72, ...]
```

Vectors allow machines to compare concepts mathematically.

---

## Vector Database

A database optimized for storing and searching embeddings.

Instead of searching text directly, it searches vectors based on similarity.

### Popular Vector Databases

- Pinecone
- Chroma
- Qdrant
- Weaviate
- Milvus

---

# Z

## Zero-Shot Prompting

Asking a model to perform a task without providing any examples.

### Example

Prompt

```
Translate the following sentence to French.

Hello, how are you?
```

The model completes the task using its pre-trained knowledge.

---

# Summary

Understanding these terms provides the foundation for working with:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- AI Agents
- Vector Databases
- Semantic Search
- Prompt Engineering

As you progress into AI Engineering, you'll encounter these concepts repeatedly across frameworks like LangChain, LangGraph, LlamaIndex, and production AI systems.
