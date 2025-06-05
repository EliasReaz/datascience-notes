# Find the Integer Square Root Without Using `sqrt()`

## ✅ The Problem

Write a function in Python to find the **square root of a non-negative integer**, **rounded down** to the nearest whole number.

- ❌ You **cannot** use the built-in `math.sqrt()` function.
- ✅ The result should be the **largest whole number** whose square is less than or equal to the input.

### Example

| Input | Expected Output | Why?                  |
|-------|------------------|------------------------|
| 9     | 3                | 3 × 3 = 9              |
| 15    | 3                | 3 × 3 = 9 < 15, 4×4=16 is too big |
| 16    | 4                | 4 × 4 = 16             |
| 24    | 4                | 4 × 4 = 16 < 24, 5×5=25 is too big |

---

## 🛠️ The Idea: Use Binary Search

### Why Binary Search?

We're looking for a number between 1 and `n` that, when squared, is less than or equal to `n`.  
This makes it a perfect job for **binary search**, which quickly narrows down a range.

---

## 🔄 Step-by-Step Logic

### Initialize

- `left = 1`
- `right = n // 2` (because no square root of `n` is larger than `n/2`, unless `n` is 0 or 1)

### Loop While `left <= right`

1. `mid = (left + right) // 2`
2. Check `mid * mid`:
   - ✅ If it's **equal to `n`**, return `mid` (exact square root!)
   - ➕ If it's **less than `n`**, it might be the answer - try bigger numbers: `left = mid + 1`
   - ➖ If it's **more than `n`**, it's too big - try smaller numbers: `right = mid - 1`

### When the loop ends

- Return `right`. This is the **biggest number** such that `right * right <= n`

---

## 🧪 Python Code

```python
def integer_sqrt(n):
    if n < 2:
        return n  # Handles 0 and 1 directly

    left, right = 1, n // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return right  # right is the floor of the square root
```

```python
print(integer_sqrt(0))   # 0
print(integer_sqrt(1))   # 1
print(integer_sqrt(9))   # 3
print(integer_sqrt(15))  # 3
print(integer_sqrt(16))  # 4
print(integer_sqrt(24))  # 4
print(integer_sqrt(25))  # 5
print(integer_sqrt(100)) # 10
```
