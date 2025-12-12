## 🤖 Machine Learning + LLM Fundamentals Quiz

### I. Machine Learning Fundamentals

1.  **What is the primary difference between supervised learning and unsupervised learning?**
    * **Answer:** **Supervised learning** uses **labeled data** (input-output pairs) to train a model to predict the output for new inputs. **Unsupervised learning** uses **unlabeled data** to find patterns, structures, or relationships within the data, such as clustering or dimensionality reduction.

2.  **Define the term "overfitting" and state one common technique used to mitigate it.**
    * **Answer:** **Overfitting** occurs when a model learns the training data and noise too well, resulting in high accuracy on the training set but poor generalization (low accuracy) on unseen data (test set).
    * **Mitigation Technique:** Regularization (L1 or L2), Dropout, Early Stopping, or Cross-Validation. 

[Image of overfitting and underfitting in machine learning]


3.  **In the context of classification, what do the terms Precision and Recall measure?**
    * **Answer:**
        * **Precision** measures the proportion of **positive predictions that were actually correct** (out of all positive predictions made by the model).
        * **Recall** measures the proportion of **actual positive cases that were correctly identified** (out of all actual positive cases).

### II. Transformer Architecture

4.  **What is the core, groundbreaking mechanism that allows the Transformer model to process sequences without relying on recurrence (like RNNs or LSTMs)?**
    * **Answer:** The **Self-Attention mechanism** (specifically, Scaled Dot-Product Attention). 

5.  **Explain the purpose of Positional Encoding in the Transformer architecture.**
    * **Answer:** Since the self-attention mechanism processes all tokens simultaneously without an inherent order, **Positional Encoding** is added to the input embeddings to inject **information about the position (or order) of each token** in the sequence.

6.  **A single Transformer block consists of two main sub-layers. What are they?**
    * **Answer:**
        1.  A **Multi-Head Self-Attention** mechanism.
        2.  A simple, position-wise **Feed-Forward Network (FFN)**. (Note: Each sub-layer is typically followed by a Residual Connection and Layer Normalization).

### III. LLM Fundamentals

7.  **What does the acronym LLM stand for, and what is the primary learning paradigm used to train these models?**
    * **Answer:** **LLM** stands for **Large Language Model**. The primary learning paradigm is **Self-Supervised Learning** on massive amounts of text data, usually through a **next-word prediction** (causal language modeling) or **masked language modeling** objective.

8.  **In an LLM, what is "In-Context Learning" (ICL), and how is it achieved?**
    * **Answer:** **In-Context Learning (ICL)** is the ability of a pre-trained LLM (like GPT-3 or Gemini) to learn a new task and generate desired output simply by being provided with a few examples or instructions within the **prompt itself**, without requiring a formal weight update (fine-tuning). It is a property that emerges from the scale of the model and data.

9.  **What are the three common modes or forms of attention masks used in different LLM training or use cases (e.g., in a decoder, encoder, or encoder-decoder setup)?**
    * **Answer:**
        1.  **Full/Bidirectional Mask (Encoder):** Allows a token to attend to all other tokens (before and after it) in the sequence.
        2.  **Causal/Look-ahead Mask (Decoder/Generative LLMs):** Prevents a token from attending to any subsequent tokens, ensuring that the prediction of a word is only based on the words that came before it.
        3.  **Cross-Attention (Encoder-Decoder):** Allows the tokens in the decoder to attend to *all* tokens in the encoder's output.

---

