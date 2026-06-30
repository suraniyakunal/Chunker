# 💼 Interview Questions

This document contains frequently asked interview questions on **Large Language Models (LLMs)**. The questions range from beginner to advanced and are designed to help you prepare for AI Engineering, Machine Learning, and Generative AI interviews.

---

# Beginner Level

## 1. What is a Large Language Model (LLM)?

**Answer**

A Large Language Model (LLM) is a deep learning model trained on massive amounts of text data to understand and generate human language.

LLMs can perform tasks such as:

- Answering questions
- Summarizing text
- Writing code
- Translating languages
- Generating content
- Reasoning over information

Examples include:

- GPT
- Gemini
- Claude
- Llama
- Mistral

---

## 2. How is an LLM different from a traditional Machine Learning model?

**Answer**

Traditional ML models are usually trained for a specific task, such as spam detection or image classification.

LLMs are general-purpose models that learn patterns from vast amounts of text and can perform many language tasks using prompts without retraining.

| Traditional ML | LLM |
|----------------|-----|
| Task-specific | General-purpose |
| Structured input | Natural language input |
| Usually predicts labels | Generates text |
| Requires retraining for new tasks | Can perform new tasks using prompts |

---

## 3. What is a token?

**Answer**

A token is the smallest unit of text processed by an LLM.

A token may represent:

- A word
- Part of a word
- A punctuation mark
- A number
- A special symbol

### Example

Text:

```text
Artificial Intelligence is amazing!
```

Possible tokens:

```text
["Artificial", "Intelligence", "is", "amazing", "!"]
```

Models operate on tokens, not characters or words.

---

## 4. What is tokenization?

**Answer**

Tokenization is the process of converting raw text into tokens before it is processed by the model.

Different LLMs may use different tokenizers, so the same sentence can produce a different number of tokens depending on the model.

---

## 5. What is an embedding?

**Answer**

An embedding is a numerical representation (vector) of text that captures its semantic meaning.

Example:

```text
"Machine Learning"
```

↓

```text
[0.21, -0.44, 0.73, ...]
```

Embeddings allow machines to compare meanings rather than exact words.

---

## 6. What is a context window?

**Answer**

A context window is the maximum amount of information an LLM can process in a single request.

It is measured in tokens.

Examples:

- 8K tokens
- 32K tokens
- 128K tokens
- 1M tokens

A larger context window allows the model to understand longer conversations and documents.

---

# Intermediate Level

## 7. How does an LLM generate text?

**Answer**

An LLM generates text by repeatedly predicting the most probable next token.

The simplified process is:

```text
Input Prompt
      │
      ▼
Tokenization
      │
      ▼
Embeddings
      │
      ▼
Transformer Layers
      │
      ▼
Probability Distribution
      │
      ▼
Next Token
      │
      ▼
Repeat
```

This continues until the model reaches a stopping condition.

---

## 8. What is the Transformer architecture?

**Answer**

The Transformer is the neural network architecture used by most modern LLMs.

Its key innovation is the **self-attention mechanism**, which allows every token to consider every other token when building context.

Benefits include:

- Better long-range understanding
- Faster parallel processing
- Improved scalability

---

## 9. What is self-attention?

**Answer**

Self-attention enables a token to determine which other tokens are most relevant when understanding the input.

Example:

```text
The dog chased the cat because it was scared.
```

The model learns that:

```text
it
```

refers to:

```text
the cat
```

Self-attention is one of the primary reasons transformers outperform older sequence models.

---

## 10. What is positional encoding?

**Answer**

Transformers process all tokens simultaneously, so they need positional information to understand word order.

Positional encoding provides this information.

Without it, the following sentences would appear identical:

```text
The dog chased the cat.
```

```text
The cat chased the dog.
```

---

## 11. Why do LLMs hallucinate?

**Answer**

LLMs generate text by predicting likely next tokens rather than verifying facts.

If the required information is missing or uncertain, the model may produce an answer that sounds plausible but is incorrect.

Common causes include:

- Missing knowledge
- Ambiguous prompts
- Lack of external context
- Outdated training data

---

## 12. How can hallucinations be reduced?

**Answer**

Several techniques help reduce hallucinations:

- Retrieval-Augmented Generation (RAG)
- Better prompt engineering
- Providing additional context
- Tool calling
- Fine-tuning for specialized tasks
- Human review in critical applications

---

# Advanced Level

## 13. What is Retrieval-Augmented Generation (RAG)?

**Answer**

Retrieval-Augmented Generation combines information retrieval with text generation.

Instead of relying only on the model's internal knowledge, relevant documents are retrieved and supplied as context.

Workflow:

```text
User Question
      │
      ▼
Embedding
      │
      ▼
Vector Search
      │
      ▼
Relevant Chunks
      │
      ▼
LLM
      │
      ▼
Final Response
```

RAG improves factual accuracy and keeps responses grounded in external knowledge.

---

## 14. When would you choose RAG over Fine-Tuning?

**Answer**

Choose **RAG** when:

- Information changes frequently
- You need access to private documents
- You want to reduce hallucinations
- Knowledge must remain up to date

Choose **Fine-Tuning** when:

- You want the model to adopt a specific writing style
- You need consistent behavior across prompts
- The task requires learning new patterns rather than retrieving facts

---

## 15. What is a vector database?

**Answer**

A vector database stores embeddings and performs similarity search.

Instead of searching for exact words, it searches for semantically similar vectors.

Popular vector databases include:

- Chroma
- Pinecone
- Qdrant
- Weaviate
- Milvus

---

## 16. What is cosine similarity?

**Answer**

Cosine similarity measures how similar two vectors are based on the angle between them.

Its values range from:

- **1** → Identical direction (highly similar)
- **0** → Unrelated
- **-1** → Opposite direction

It is commonly used to rank search results in semantic search systems.

---

## 17. What is semantic search?

**Answer**

Semantic search retrieves documents based on meaning rather than exact keyword matches.

Example:

Query:

```text
How do airplanes fly?
```

Possible retrieved document:

```text
Aircraft generate lift using their wings...
```

Even though the words differ, the meanings are closely related.

---

## 18. What is the difference between training and inference?

**Answer**

| Training | Inference |
|----------|-----------|
| Learns from data | Uses the trained model |
| Updates model weights | Does not change weights |
| Computationally expensive | Faster and cheaper |
| Happens during model development | Happens every time a user sends a prompt |

Most AI engineers focus on inference rather than training foundation models.

---

## 19. What factors affect LLM performance?

**Answer**

Performance depends on several factors, including:

- Model size
- Training data quality
- Context window size
- Prompt quality
- Retrieval quality (for RAG)
- Decoding parameters (temperature, top-p, etc.)
- Available context

Optimizing these factors leads to more accurate and reliable outputs.

---

## 20. What are the limitations of LLMs?

**Answer**

Some common limitations include:

- Hallucinations
- Limited reasoning in certain scenarios
- High computational cost
- Context window limitations
- Outdated knowledge (without retrieval)
- Bias inherited from training data
- Non-deterministic outputs

Understanding these limitations helps engineers design systems that mitigate them using techniques like RAG, tool use, and human oversight.

---

# Interview Tips

- Focus on explaining concepts clearly rather than memorizing definitions.
- Use diagrams or workflows when discussing architectures like Transformers or RAG.
- Relate theoretical concepts to real-world applications whenever possible.
- If you don't know an answer, explain your reasoning instead of guessing.
- Practice implementing concepts (such as embeddings, vector search, and RAG) to reinforce your understanding.

---

# Key Takeaways

After studying these questions, you should be able to explain:

- What LLMs are and how they work
- How tokenization and embeddings function
- The role of transformers and self-attention
- Why hallucinations occur
- How RAG improves factual accuracy
- The purpose of vector databases and semantic search
- When to use RAG versus fine-tuning
- Common strengths and limitations of modern LLMs

These topics form the foundation of most entry-level and intermediate AI Engineering interviews.
