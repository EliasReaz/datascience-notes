# A/B Testing

A/B testing is a statistical method used to determine whether a new variant (e.g., a website design, pricing model, or treatment) results in a measurable improvement over an existing version (the control).

It helps answer questions such as:

- Does the new website design increase **conversion rates** for an e-commerce store?
- Does a new drug improve **recovery rates** in a clinical trial?
- Does offering free shipping increase **average order value** in a retail business?
- Does a personalized email campaign increase **click-through rates** in a marketing platform?
- Does a redesigned onboarding flow reduce **user churn** for a SaaS product?
- Does a new pricing model improve **subscription upgrades** in a fintech app?

---

## Steps to Conduct an A/B Test

### 1. Formulate Hypotheses and Set Significance Level

- **Null Hypothesis (H₀):** There is no difference between the control and variant.
- **Alternative Hypothesis (H₁):** There is a statistically significant difference.
- Set the **significance level** (α), typically 0.05.

### 2. Random Assignment and Isolation

- Randomly assign users into:
  - **Group A (Control):** Existing version
  - **Group B (Treatment/Variant):** New version
- Ensure both groups are balanced in key features (e.g., device type, geography, traffic source).

- Isolation ensures that users in one group (A or B) do not influence the behavior or outcomes of users in the other group.
  - **Why isolation matters:** Without isolation, results may be biased due to **spillover effects**, where the treatment indirectly impacts the control group (or vice versa).
  - **Example:** Suppose you're testing a new referral program (Treatment B). If a user in Group B refers a user in Group A, the latter might behave like a Treatment user, contaminating the control group and invalidating the results.
  - **Best practice:** Assign at the user level (not session level), and avoid shared environments (e.g., shared devices or accounts) when possible.
  - Ensure users in both groups are using the **same operating system** (e.g., only iOS or only Android) to eliminate platform-related variability.

### 3. Ensure Adequate Sample Size and Power

- Before running an A/B test, make sure you have **enough users** (sample size) to detect a meaningful difference.
- **Effect size (lift):** This is the minimum improvement you want to be able to detect — for example, a 5% increase in conversion rate.
- **Baseline conversion rate:** The current conversion rate without any changes (Control group).
- **Power:** The chance of correctly detecting a real effect (usually set at 80% or higher). If power is too low, you might miss real improvements.
- **Why it matters:** If your sample size is too small, the test may not detect true differences — leading to false negatives.

#### How to calculate sample size simply in Python with `statsmodels`:

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Baseline conversion rate (control)
p1 = 0.10  # e.g., 10%
# Expected conversion rate after change (treatment)
p2 = 0.12  # e.g., 12%, which is a 2% absolute lift

# Calculate effect size (Cohen's h)
effect_size = proportion_effectsize(p2, p1)

# Set power and significance level (alpha)
power = 0.8        # 80% chance to detect effect
alpha = 0.05       # 5% chance of false positive (Type I error)

# Initialize power analysis object
analysis = NormalIndPower()

# Calculate required sample size per group
sample_size = analysis.solve_power(effect_size=effect_size, power=power, alpha=alpha, ratio=1)

print(f"Sample size needed per group: {int(sample_size)}")
```

### 4. Run the Test for Sufficient Duration

- The test should run long enough to:
  - Cover natural behavior cycles (weekends, holidays)
  - Avoid early stopping or "peeking"
  
### 5. Analyze Results Using p-value

- Calculate the **p-value**.
- If **p < α**, reject the null hypothesis and conclude the effect is statistically significant.

### 6. Check Guardrail Metrics

- Monitor secondary metrics such as:
  - Bounce rate
  - Customer complaints
  - Load times
- Ensure there are no unintended negative impacts.

### 7. Decide Whether to Roll Out

- If the result is:
  - **Statistically significant**
  - **Practically meaningful**
  - **No harm to guardrails**
  
Then, proceed with deploying the new version.

---

## Additional Notes

- **Multiple Testing:** Adjust for multiple comparisons (e.g., Bonferroni correction).
- **Effect Size vs. Statistical Significance:** Small p-values do not always mean large or meaningful effects.
- **Practical Significance:** Consider the business impact beyond statistical metrics.

---

## Summary Table

| Concept                   | Description                                                   | Example                                                       |
|---------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Null Hypothesis (H₀)      | No difference between control and variant                     | "Conversion rate in group A = group B"                        |
| Alternative Hypothesis (H₁) | Statistically significant difference exists                 | "Conversion rate in group B > group A"                        |
| α (Significance Level)     | Probability of false positive (Type I error), typically 0.05 | If p-value < 0.05, reject H₀                                  |
| Power                      | Probability of detecting a true effect, typically 80%        | 80% chance of detecting a 5% lift if it exists                |
| Effect Size (Lift)         | The measurable difference between variant and control        | Group A: 10% CR, Group B: 12% CR → Effect size = 2%           |
| Guardrail Metrics          | Secondary metrics to monitor for unintended consequences     | Bounce rate, time on site, refund requests, site load time    |

---
