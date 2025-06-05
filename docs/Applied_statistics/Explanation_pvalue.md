# Explanation of p-value in statistical inferences

## What does a p-value mean?

- A p-value is the probability of obtaining test results _at least as extreme as_ the observed results, under the assumption that the null hypothesis (H₀) is true.
- A p-value helps us figure out how surprising our results are if we assume the null hypothesis (H₀) is true.
- When we say "**at least as extreme**" we're asking: if the null hypothesis were true, what's the probability of getting results that are **this unusual or even more unusual** than what we actually observed?
- Think of it this way: your observed data gives you a certain amount of "evidence against" the null hypothesis. The p-value asks, **What's the chance of getting this much evidence against the null hypothesis, or even stronger evidence, if the null hypothesis is actually true**?
- Let's say we think a coin is fair (H₀: The coin is fair - the chance of heads is 50%). We toss it 100 times and get only 5 heads. That seems strange, right?
- The p-value tells us: "If the coin really is fair, what’s the chance we’d see something as extreme as 5 heads (or fewer)?"
- That’s a **one-tailed** test - looking just at one end (very few heads).
- A **two-tailed** test would ask: "What’s the chance of getting something really extreme on **either** end - like 5 or fewer heads **or** 95 or more heads?"
- If the p-value is really small (say, less than 0.05), that means our _result is pretty unusual under the assumption of fairness_. So we might start to _doubt_ the coin is actually fair.

> Note 1: A small p-value doesn’t _prove_ the coin is unfair - it just means what we saw would be unlikely _if_ it were fair.

> Note 2: A small p-value does **not mean H₀ is false**. It means the observed data would be unlikely under H₀. It means we **fail to reject** H$_o$.

```pyhton
import scipy.stats as stats

# Set the parameters
n = 100          # Number of coin tosses
p = 0.5          # Probability of heads under the null hypothesis (fair coin)
k = 5            # Observed number of heads (very low!)

# ================================================
# One-tailed p-value:
# We want the probability of getting k or fewer heads if the coin is fair.
# That's why we use CDF (Cumulative Distribution Function) — it adds up
# the probability of 0, 1, 2, ..., up to k heads.
# If we used PDF, it would only give the probability of *exactly* 5 heads.
# ================================================
p_value_one_tail = stats.binom.cdf(k, n, p)
print("One-tailed p-value (5 or fewer heads):", p_value_one_tail)

# ================================================
# Two-tailed p-value:
# We want to find how extreme the result is on *both* sides of the expected value (which is 50 heads).
# Getting only 5 heads is 45 less than expected → delta = 45
# So, we also look at the *other* extreme: 50 + 45 = 95 heads or more
# CDF gives cumulative up to a value, so for 95 or more, we subtract CDF(94) from 1.
# ================================================

expected = n * p                   # Expected number of heads = 50
delta = abs(k - expected)         # How far away our result (5) is from expected (50)

# Left tail: probability of getting <= 5 heads (already calculated, but let's redo for clarity)
p_low = stats.binom.cdf(expected - delta, n, p)  # same as stats.binom.cdf(5, 100, 0.5)

# Right tail: probability of getting >= 95 heads
# Since CDF gives probability of <= x, we subtract from 1 to get >= 95
p_high = 1 - stats.binom.cdf(expected + delta - 1, n, p)  # 1 - CDF(94)

# Add both tails to get the total two-tailed p-value
p_value_two_tail = p_low + p_high
print("Two-tailed p-value (5 or fewer OR 95 or more heads):", p_value_two_tail)
```
