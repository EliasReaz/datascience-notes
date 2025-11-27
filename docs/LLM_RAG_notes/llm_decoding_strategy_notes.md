## 🏗️ Workflow 
### **Select a Foundation Model**
- Examples: `mistralai/mistral-small`, `meta-llama/Llama-3`, `gpt-j`, etc.
- Consider:
  - **Size vs. latency** (small models for speed, large for accuracy).
  - **Domain fit** (general-purpose vs. fine-tuned).
  - **Hosting** (IBM Watsonx, Hugging Face, Azure, local inference).

---

### **Configure Model Parameters**
- Common parameters:
  - `MAX_NEW_TOKENS`: controls output length.
  - `TEMPERATURE`: randomness/creativity.
  - `TOP_K` / `TOP_P`: sampling constraints.
  - `DECODING_METHOD`: greedy, sample, beam search.
- Credentials & project setup (e.g., Watsonx API keys, project IDs).

---

### **Wrap with LangChain (or Orchestration Layer)**
- Purpose: abstract the raw model into a **LangChain LLM interface**.
- Benefits:
  - Unified API across different providers.
  - Easy chaining with tools (retrievers, agents, memory).
  - Plug-and-play with pipelines (QA bots, RAG, structured workflows).
- Example:
```python
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.foundation_models import ModelInference, GenParams

model = ModelInference(
    model_id="mistralai/mistral-small",
    params={
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5,
    },
    credentials={"url": "https://us-south.ml.cloud.ibm.com"},
    project_id="skills-network"
)

llm = WatsonxLLM(model=model)
```

---

### **Integrate into Workflow**
- **Prompt engineering**: design input prompts.
- **Chains/Agents**: combine LLM with retrievers, tools, memory.
- **Evaluation**: test determinism vs. creativity depending on decoding.

---

### 🔑 Decoding Strategies (After Wrapping)
*(same section as before, now positioned after the setup)*

| Method            | How it Works | Pros | Cons | Best Use Cases |
|-------------------|--------------|------|------|----------------|
| **Greedy**        | Always picks highest-probability token | Deterministic, reproducible | Bland, repetitive | Structured extraction, factual QA |
| **Sampling**      | Randomly samples with temperature | Creative, diverse | Non-deterministic | Brainstorming, storytelling |
| **Top-k**         | Samples from top *k* tokens | Balance diversity/coherence | Needs tuning | Creative writing |
| **Top-p**         | Samples from cumulative probability mass | Adaptive diversity | Needs tuning | Dialogue, open-ended tasks |
| **Beam Search**   | Explores multiple sequences | Higher-quality | Expensive, less diverse | Translation, summarization |

---

## 📌 Rule of Thumb
- **Foundation model choice** → determines baseline capability.
- **LangChain wrapping** → enables orchestration and workflow hygiene.
- **Decoding strategy** → tailors output style (deterministic vs. creative).

---

## 🎯 Quick Takeaway
Think of it as a **three-layer stack**:
1. **Foundation model** (raw capability).  
2. **Wrapper (LangChain LLM)** (workflow orchestration).  
3. **Decoding strategy** (output style).  

---

## ⚙️ Parameter Interactions
- **Temperature**
  - `0` → collapses sampling into greedy decoding.
  - `>0` → introduces randomness.
- **DECODING_METHOD**
  - `"greedy"` → forces deterministic decoding.
  - `"sample"` → uses temperature/top-k/top-p.
- **Max Tokens**
  - Controls length, independent of decoding method.

---

## 📌 Rule of Thumb
- Use **Greedy** when:
  - You need **deterministic, reproducible outputs**.
  - Tasks are **factual, structured, or extractive**.
- Use **Sampling** when:
  - You want **creative, varied outputs**.
  - Tasks are **open-ended, conversational, or generative**.

---

## 🛠️ Example Configurations

### Greedy Decoding
```python
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0,
    GenParams.DECODING_METHOD: "greedy"
}
```

### Sampling with Temperature
```python
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.7,
    GenParams.DECODING_METHOD: "sample"
}
```

---

## 🎯 Quick Takeaway
- **Greedy = reproducibility**  
- **Sampling = creativity**  
- Explicitly set `DECODING_METHOD` when you want control.  
- If you don’t set it, the system defaults to sampling (since you provided `temperature > 0`).  

---
