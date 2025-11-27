# 🧩 RAG Workflow Cheat Sheet 
---

## 1. 📄 Loading Documents

- **What it is:** Ingesting raw data (PDFs, text files, web pages, etc.) into your pipeline.

- **Tools:** PyPDFLoader, TextLoader, UnstructuredLoader, etc.

- **Use-case:** Load a company’s policy PDF so the LLM can answer HR-related queries.

**Code Example:**
```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("company_handbook.pdf")
documents = loader.load()
```

**Parameters to tune:**
- **File type loader** (`PyPDFLoader`, `TextLoader`, `UnstructuredLoader`) → depends on source format.
- **Pre-cleaning options** (remove headers, normalize whitespace) → improves chunk quality.

**Notes:**  
Choose loaders that preserve structure. For PDFs, some loaders extract text line-by-line, others preserve layout.

---

## 2. ✂️ Chunking

- **What it is:** Splitting documents into smaller pieces for embedding.

- **Parameters:**

    - chunk_size: Number of characters/tokens per chunk (e.g., 500–1000).
    - chunk_overlap: Overlap between chunks (e.g., 50–100) to preserve context.

- **Why:** Embedding models have input size limits; smaller chunks improve retrieval accuracy.

- **Use-case:** Split a 50-page research paper into 500-character chunks with 50 overlap so queries don’t miss context across page breaks.
**Code Example:**
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # size of each chunk
    chunk_overlap=100,   # overlap between chunks
    length_function=len  # how length is measured
)
chunks = text_splitter.split_documents(documents)
```

**Parameters to tune:**
- **`chunk_size`** → Larger chunks = more context, but risk exceeding embedding limits.  
- **`chunk_overlap`** → Prevents context loss across boundaries.  
- **`length_function`** → Can be `len` (characters) or token-based (using tokenizer).  
- **Granularity strategy** → Sentence-based vs character-based splitting.

**Notes:**  
Balance between retrieval precision and context completeness. For legal docs, use smaller chunks with overlap; for FAQs, larger chunks may suffice.

---

## 3. 🔢 Embeddings

- **What it is:** Converting text chunks into numerical vectors that capture semantic meaning.

- **Models:**

  - OpenAI (text-embedding-ada-002)

  - HuggingFace (sentence-transformers)

  - IBM watsonx embeddings

- **Parameters**:

  - dimension (size of vector, e.g., 768 or 1536)

  - model choice (trade-off: speed vs accuracy)

- **Use-case:** Represent customer support FAQs as embeddings so queries like “How do I reset my password?” match semantically similar answers.
**Code Example:**
```python
from langchain.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")
vector = embedding_model.embed_query("reset password instructions")
```

**Parameters to tune:**
- **Model choice** → `ada-002` (fast, cheap), `text-embedding-3-large` (higher accuracy).  
- **Embedding dimension** → 512, 768, 1536 depending on model.  
- **Batch size** → Controls throughput when embedding many chunks.  
- **Normalization** → Some DBs require normalized vectors (unit length).

**Notes:**  
Higher dimension = richer representation but heavier storage. Always align DB dimension with embedding model output.

---

## 4. 🗄️ Vector Databases

- **What it is:** Specialized DBs for storing and searching embeddings.

- **How different from traditional DBs:**

  - Traditional DB → exact match (SQL queries).

  - Vector DB → similarity search (nearest neighbors in vector space).

- **Types / Examples:**

  - Local: FAISS, Annoy, Milvus

  - Cloud: Pinecone, Weaviate, ChromaDB

- **Use-case:** Store embeddings of product manuals in Pinecone so engineers can query “error code 404” and retrieve relevant troubleshooting steps.
**Code Example (ChromaDB):**
```python
from langchain.vectorstores import Chroma

vectordb = Chroma.from_documents(documents=chunks, embedding=embedding_model)
```

**Parameters to tune:**
- **Distance metric** → cosine, dot product, Euclidean.  
- **Persistence** → in-memory vs disk-backed.  
- **Index type** (FAISS: Flat, IVF, HNSW) → trade-off between speed and accuracy.  
- **Replication / sharding** (cloud DBs like Pinecone) → scale for large datasets.

**Notes:**  
Cosine similarity is common for text embeddings. IVF/HNSW indexes accelerate search but may approximate results.

---

## 5. 🔍 Retrievers

- **What it is:** A wrapper around the vector DB that defines how to fetch relevant chunks.

- **Types:**

  - **Single-query retriever:** Basic similarity search.

    - **Use-case:** Simple Q&A over one document.

  - **Multi-query retriever:** Expands query into multiple variations.

    - **Use-case:** User asks “AI courses” → expands to “machine learning courses,” “deep learning classes.”

  - **MMR (Maximal Marginal Relevance):** Balances relevance + diversity.

    - **Use-case:** Avoids retrieving 5 nearly identical chunks, ensures broader coverage.

  - **Parent-document retriever:** Retrieves the parent doc when a chunk is matched.

    - **Use-case:** Legal contracts or Research papers where context across clauses matters.

**Code Example:**
```python
retriever = vectordb.as_retriever(
    search_type="mmr",   # retrieval strategy
    search_kwargs={"k": 5, "lambda_mult": 0.5}
)
```

**Parameters to tune:**
- **`k`** → Number of chunks retrieved. Larger `k` = more coverage, but risk of noise.  
- **MMR diversity (`lambda_mult`)** → Controls balance between relevance and diversity.  
- **Multi-query expansion size** → Number of query variations generated.  
- **Parent-document retriever window size** → How much of parent doc is returned.

**Notes:**  
- Use **MMR** when you want diverse evidence (research, multi-topic queries).  
- Use **multi-query retriever** when queries are ambiguous.  
- Use **parent-doc retriever** for structured docs (contracts, manuals).

---

## 6. 🤖 RetrievalQA

- **What it is:** Combines retriever + LLM to answer queries with external knowledge.

- **Components:**

  - Retriever: Supplies relevant chunks.

  - LLM: Generates final answer.

  - Memory (optional): Keeps track of conversation history.

- **Use-case:**

  - Customer support chatbot → retrieves product manual chunks, LLM answers naturally.

  - Research assistant → retrieves academic papers, LLM summarizes findings.

**Code Example:**
```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(model="gpt-4"),
    retriever=retriever,
    return_source_documents=True
)

response = qa_chain.run("What is the parental leave policy?")
```

**Parameters to tune:**
- **LLM choice** → GPT-4 (accuracy), GPT-3.5 (speed/cost).  
- **Return source docs** → Useful for transparency.  
- **Memory type** → ConversationBufferMemory, SummaryMemory.  
- **Temperature** → Controls creativity vs factuality.  
- **Max tokens** → Controls length of generated answer.

**Notes:**  
For factual Q&A, keep temperature low (0–0.3). For brainstorming, increase it. Always return sources for trustworthiness.

---

# ⚙️ Practical Parameters Cheat Sheet

| Step        | Key Parameters | Why They Matter |
|-------------|----------------|-----------------|
| Chunking    | `chunk_size`, `chunk_overlap`, `length_function` | Balance context vs precision |
| Embeddings  | `model`, `dimension`, `batch_size`, `normalize` | Accuracy vs cost/storage |
| Vector DB   | `distance_metric`, `index_type`, `persistence` | Search speed vs accuracy |
| Retriever   | `k`, `lambda_mult`, `multi-query size`, `parent window` | Relevance vs diversity |
| RetrievalQA | `llm`, `temperature`, `max_tokens`, `memory` | Answer quality, transparency |

---

# 🛠️ End-to-End Example (with tuned parameters)

```python
# Load
loader = PyPDFLoader("handbook.pdf")
docs = loader.load()

# Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Embed
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# Vector DB
vectordb = Chroma.from_documents(chunks, embedding_model)

# Retriever (MMR with diversity)
retriever = vectordb.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8, "lambda_mult": 0.7}
)

# RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(model="gpt-4", temperature=0.2),
    retriever=retriever,
    return_source_documents=True
)

answer = qa_chain.run("Explain parental leave policy")
```

---
