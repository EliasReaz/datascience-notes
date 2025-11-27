
# 📝 TF‑IDF Reference Note

TF‑IDF emphasizes **word relevancy**. In document search, it helps identify which documents are most relevant to a user’s query by highlighting words that are distinctive to specific documents rather than common across all.

## 🔎 Why TF‑IDF is Useful in Search

- Balances frequency and distinctiveness: Common words like “the” or “and” are down‑weighted, while rare but meaningful words like “climate” or “inflation” are up‑weighted.

- Improves ranking: Documents where query terms have high TF‑IDF scores are ranked higher because those terms are both frequent and distinctive in those documents.

- Contextual relevance: A word’s importance is judged relative to the entire corpus, so search results reflect not just raw frequency but discriminative power.

## 1. Core Definitions
- **Term Frequency (TF):**  
  Frequency of a word within a single document. High if the word appears often in that document.
- **Document Frequency (DF):**  
  Number of documents in the corpus that contain the word at least once.  
  - High DF → word appears in many documents.  
  - Low DF → word appears in few documents.
- **Inverse Document Frequency (IDF):**  
  Measures rarity across documents:  
  \[
  IDF = \log\left(\frac{N}{DF}\right)
  \]  
  where \(N\) = total number of documents.  
  - Low DF → High IDF.  
  - High DF → Low IDF.
- **TF‑IDF Score:**  
  \[
  TF\text{-}IDF = TF \times IDF
  \]  
  Highlights words that are frequent in one document but rare across the corpus.

---

## 2. Interpretation
- **High TF‑IDF Score:**  
  - Word is frequent in a specific document.  
  - Word is rare across other documents.  
  - Meaning → the word is **distinctive or signature** for that document.
- **Low TF‑IDF Score:**  
  - Word appears across many documents.  
  - Meaning → the word is **common background noise** (e.g., “the”, “and”).

---

## 3. Examples
### 📚 Case A: 5 Books
- Word “climate” appears 50 times in Book A, absent in others.  
  - TF (Book A) = high.  
  - DF = 1 → IDF = high.  
  - TF‑IDF (Book A) = high.  
  - TF‑IDF (Books B–E) = 0.

### 📄 Case B: 1 Book with 5 Pages
- Treat each page as a document.  
- If “climate” appears only on Page 1:  
  - DF = 1 (out of 5).  
  - IDF = high.  
  - TF‑IDF (Page 1) = high.  
  - TF‑IDF (Pages 2–5) = 0.

### 📰 Case C: News Articles
- Corpus = 100 articles.  
- Word “inflation” appears in 80 articles.  
  - DF = 80 → IDF = low.  
  - Even if TF is high in one article, TF‑IDF score is lower because the word is common.

---

## 4. Rule of Thumb
  
- **High score → specific to one document.**  
- **Low score → common across all documents.**

- **High TF‑IDF score** → query word is highly relevant to that document.

- **Low TF‑IDF score** → query word is common across many documents (e.g. the, and), less useful for distinguishing relevance.

- **Granularity matters:**  
  - If you treat _each book as a document_ → TF‑IDF highlights words distinctive to each book.  
  - If you treat _each page as a document_ → TF‑IDF highlights words distinctive to each page.

---

## 📊 TF‑IDF Example Table

| Document | Term Frequency (TF) of “climate” | Document Frequency (DF) across corpus | Inverse Document Frequency (IDF) | TF‑IDF Score | Interpretation |
|----------|----------------------------------|---------------------------------------|----------------------------------|--------------|----------------|
| Book A   | 30                               | DF = 2 (appears in Book A & Book B)   | log(5/2) ≈ 0.92                  | 27.6         | High → “climate” is distinctive for Book A |
| Book B   | 2                                | DF = 2                                | log(5/2) ≈ 0.92                  | 1.84         | Low → word appears but not strongly distinctive |
| Book C   | 0                                | DF = 2                                | log(5/2) ≈ 0.92                  | 0            | Absent → no relevance |
| Book D   | 0                                | DF = 2                                | log(5/2) ≈ 0.92                  | 0            | Absent → no relevance |
| Book E   | 0                                | DF = 2                                | log(5/2) ≈ 0.92                  | 0            | Absent → no relevance |

---

### 🔎 Key Takeaways
- **Book A:** High TF × High IDF → high TF‑IDF score → “climate” is a **signature word** for Book A.  
- **Book B:** Low TF × High IDF → low TF‑IDF score → “climate” is present but not distinctive.  
- **Books C–E:** TF = 0 → TF‑IDF = 0 → “climate” is irrelevant.  

---

✅ This table shows how the **same word gets different TF‑IDF scores depending on the document**. It’s high where the word is frequent and rare elsewhere, and low where the word is common or absent.
