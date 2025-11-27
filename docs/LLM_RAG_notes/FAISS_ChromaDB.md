# 📌 Vector Search Reference Notes

## 🔹 FAISS (Facebook AI Similarity Search)
- **Type**: Library (not a database)
- **Strengths**:
  - High-performance similarity search on single machine (CPU/GPU)
  - Multiple indexing options (flexibility + control)
  - Great for millions of vectors
- **Limitations**:
  - No metadata storage
  - No built-in distributed scaling
  - Requires coding to integrate

### 🗂 Index Options in FAISS
| Index Type | How It Works | Pros | Cons / Trade-offs |
|------------|--------------|------|-------------------|
| **Flat Index** | Brute force: compares query to every vector | Exact, highest accuracy | Very slow for large datasets |
| **IVF (Inverted File Index)** | Clusters vectors, searches only nearest clusters | Much faster, scalable | Approximate, may miss close neighbors |
| **LSH (Locality-Sensitive Hashing)** | Hash functions bucket similar vectors | Memory-efficient, good for high-dimensional sparse data (e.g., text embeddings) | Lower accuracy, not always fastest |
| **HNSW (Hierarchical Navigable Small World)** | Multi-layer graph search | Fast, high recall (~90–99%), tunable | Approximate, memory-heavy, less ideal for dynamic datasets |

---

## 🔹 ChromaDB
- **Type**: Full vector database
- **Strengths**:
  - Stores vectors + metadata (tags, descriptions)
  - Easy integration with LangChain and AI prototyping
  - Service-based, convenient setup
- **Limitations**:
  - Only supports **HNSW** indexing
  - Less control compared to FAISS
- **Best for**: Rapid prototyping, metadata filtering, ease of use

---

## 🔹 HNSW (Hierarchical Navigable Small World Graph)
- **Concept**: Multi-layer graph search (highways → main roads → local streets analogy)
- **Search process**:
  - Start at sparse top layer → greedy search
  - Move down layers until reaching dense bottom layer
- **Index building**:
  - Each point gets random height
  - Connected to closest neighbors at each level
- **Performance**:
  - Recall: ~90–99% (approximate, not exact)
  - Tunable parameters: connections, breadth of search
- **Trade-offs**:
  - Best for mostly-static datasets
  - Memory-heavy if tuned for high accuracy
  - Not ideal for frequent insertions/deletions
  - Approximate results (not guaranteed exact)

---

## 🔹 Milvus
- **Type**: Distributed vector database
- **Strengths**:
  - Production-ready scaling
  - Hybrid search (structured + vector)
  - Uses FAISS and HNSW under the hood
- **Best for**: Large-scale, distributed, production deployments

---

## ⚖️ Quick Comparison Table

| Feature              | FAISS (Library) | ChromaDB (DB) | HNSW (Index) | Milvus (DB) |
|----------------------|-----------------|---------------|--------------|-------------|
| **Nature**           | Toolkit/library | Full database | Index algo   | Distributed DB |
| **Metadata support** | ❌              | ✅            | ❌           | ✅          |
| **Index options**    | Flat, IVF, LSH, HNSW | Only HNSW | N/A          | Multiple (via FAISS/HNSW) |
| **Ease of use**      | Low (code req.) | High          | N/A          | Medium (setup needed) |
| **Performance**      | Very high local | Good, convenient | Fast approx | Scalable, production |
| **Scaling**          | Single machine  | Limited       | N/A          | Distributed |
| **Best for**         | Control + speed | Prototyping   | Approx search | Enterprise scale |

---

✅ **Key Takeaway**:  
- **FAISS** → control + speed, multiple index choices (Flat, IVF, LSH, HNSW)  
- **ChromaDB** → convenience + metadata, prototyping  
- **HNSW** → fast approximate search, static datasets  
- **Milvus** → distributed, production-ready  

---
