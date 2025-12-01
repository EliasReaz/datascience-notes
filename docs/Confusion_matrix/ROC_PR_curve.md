## 📊 Annotated Confusion Matrix (ROC plot)

- The x-axis is the False Positive Rate (FPR), also known as 1 - Specificity.
- The y-axis is the True Positive Rate (TPR), also known as Sensitivity or Recall

```
                Predicted Positive   Predicted Negative
Actual Positive    TP                  FN
                  ↑                   ↑
                  |                   |
                  |                   └── Missed positives → lowers Recall (TPR)
                  └── True Positives → boosts Recall (TPR)

Actual Negative    FP                  TN
                  ↑                   ↑
                  |                   |
                  |                   └── True Negatives → boosts Specificity
                  └── False Positives → raises False Positive Rate (FPR)
```

### Key Metrics
- **TPR (Recall, Sensitivity)** = $$\frac{TP}{TP + FN}$$  
  → Fraction of actual positives correctly identified. 

- **FPR (False Positive Rate)** = $$\frac{FP}{FP + TN}$$  
  → Fraction of actual negatives wrongly flagged as positive.  
- **ROC Curve** = Plot of TPR vs FPR across thresholds.  
- **AUC (Area Under Curve)** = Single number summarizing ROC; closer to 1 = better classifier.  

---

### 🔍 Why TPR vs FPR Matters
- **Trade‑off visualization:**  
  Every threshold you set for a classifier changes both **TPR (sensitivity)** and **FPR (false alarm rate)**. Plotting them against each other shows the *trade‑off* — you can’t usually maximize both at the same time.
  
- **Threshold independence:**  
  Accuracy at a single threshold can be misleading. By plotting TPR vs FPR across *all thresholds*, you see the classifier’s overall behavior, not just one arbitrary cutoff.

- **Comparing models:**  
  ROC curves let you compare different classifiers. A curve closer to the top‑left corner (high TPR, low FPR) indicates a better model. The **Area Under the Curve (AUC)** is a single summary metric of this performance.

- **Application sensitivity:**  
  - In **medical diagnosis**, you want high TPR (catch all true cases), even if FPR rises.  
  - In **fraud detection**, you want low FPR (avoid false alarms), even if TPR drops.  
  The ROC curve helps you *choose the right threshold* depending on the domain’s tolerance for false positives vs false negatives.

---

### ⚖️ Analogy
Think of it like a **security checkpoint**:
- **TPR** = how many actual threats you catch.  
- **FPR** = how many innocent travelers you wrongly flag.  
Plotting TPR vs FPR shows whether your scanner is *too strict* (flags everyone) or *too lenient* (misses threats). The ROC curve helps balance these extremes.

---

### 📊 Key Insight
The importance lies in **understanding the balance between sensitivity and specificity**. Without this curve, you’d only see performance at one threshold, missing the bigger picture of how the model behaves across all possible decision boundaries.

---
## 🧪 Worked Examples

### 1. **Medical Diagnosis (Disease Test)**
- Suppose 100 patients: 40 sick, 60 healthy.  
- Test results: TP=35, FN=5, FP=10, TN=50.  

Metrics:
- TPR (Recall) = 35 / (35+5) = **87.5%**  
- FPR = 10 / (10+50) = **16.7%**  
- ROC Curve: If threshold is lowered, TPR ↑ but FPR ↑ too.  
- AUC: If classifier is strong, curve hugs top-left; here maybe ~0.9.  

Interpretation: Good recall (few sick missed), but some false alarms.

---

### 2. **Customer Churn Prediction**
- Dataset: 200 customers, 50 churned, 150 stayed.  
- Model predicts: TP=40 churners correctly, FN=10 missed churners, FP=30 wrongly flagged, TN=120 correctly retained.  

Metrics:
- TPR = 40 / (40+10) = **80%**  
- FPR = 30 / (30+120) = **20%**  
- ROC: Adjusting threshold changes balance between catching churners vs wrongly alarming loyal customers.  
- AUC: ~0.85 indicates decent discrimination.  

Interpretation: Model is good at catching churn, but 20% of loyal customers wrongly flagged could waste retention budget.

---

### 3. **Loan Default Prediction**
- Dataset: 500 applicants, 100 defaulters, 400 non-defaulters.  
- Model predicts: TP=70 defaulters correctly, FN=30 missed, FP=40 wrongly flagged, TN=360 correctly cleared.  

Metrics:
- TPR = 70 / (70+30) = **70%**  
- FPR = 40 / (40+360) = **10%**  
- ROC: Lower threshold → more defaults caught but more false alarms.  
- AUC: ~0.88 shows strong separation.  

Interpretation: Bank balances risk: catching most defaulters while keeping false alarms low.

---

## 📝 Cheat Sheet Summary

- **TPR (Recall)** → “How many actual positives did we catch?”  
- **FPR** → “How many actual negatives did we wrongly flag?”  
- **ROC Curve** → Trade-off between TPR and FPR at different thresholds.  
- **AUC** → Overall classifier quality (closer to 1 = better).  

---


**QUESTION**: **Difference between ROC and Precision-Rcall curves**

**Quick Answer:**  
The **ROC curve** plots *True Positive Rate (Recall)* vs *False Positive Rate*, while the **Precision-Recall (PR) curve** plots *Precision* vs *Recall*. ROC is more informative when classes are balanced, whereas PR curves are more useful for **imbalanced datasets**, since they highlight how well a model identifies the minority (positive) class.



---

### 📊 ROC Curve (Receiver Operating Characteristic)
- **Axes:**  
  - X-axis → False Positive Rate (FPR = FP / (FP + TN))  
  - Y-axis → True Positive Rate (TPR = Recall = TP / (TP + FN))  
- **Interpretation:**  
  - Shows trade-off between sensitivity (recall) and specificity (1 − FPR).  
  - A diagonal line represents random guessing; curves above it indicate better performance.  
- **Best Use Case:**  
  - Balanced datasets where both positive and negative classes are equally important.  
  - Good for evaluating overall discrimination ability across thresholds.

---

### 🎯 Precision-Recall Curve
- **Axes:**  
  - X-axis → Recall (TP / (TP + FN))  
  - Y-axis → Precision (TP / (TP + FP))  
- **Interpretation:**  
  - Focuses on the trade-off between precision (how many predicted positives are correct) and recall (how many actual positives are captured).  
  - High precision with high recall indicates strong performance.  
- **Best Use Case:**  
  - Imbalanced datasets (e.g., fraud detection, rare disease diagnosis).  
  - More sensitive to performance on the minority class, unlike ROC which can be overly optimistic when negatives dominate.

---

### 🔑 Key Differences
| Aspect | ROC Curve | Precision-Recall Curve |
|--------|-----------|-------------------------|
| X-axis | False Positive Rate | Recall |
| Y-axis | True Positive Rate (Recall) | Precision |
| Focus | Overall discrimination ability | Positive class performance |
| Best for | Balanced datasets | Imbalanced datasets |
| Risk | Can look good even if positives are poorly predicted | Highlights poor precision/recall clearly |

Sources: 

---

👉 Think of it this way: **ROC tells you how well your model separates classes overall**, while **PR tells you how well your model finds the rare positives without drowning in false alarms**.  

