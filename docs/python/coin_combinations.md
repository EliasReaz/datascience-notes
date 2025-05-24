# Count the Number of Ways to Make a Target Amount Using Coins

Suppose you want to find how many ways you can make a **target amount** using a given list of **coin denominations**.

### Example:

```python
target_amount = 4
coins = [2, 3]
```

### Initialization

We initialize a list called `ways` to store the number of ways to make each amount from `0` to `target_amount`.

* `ways[0] = 1` → There's exactly one way to make amount `0`: using no coins.
* The rest are initialized to `0`.

So initially: ways = [1, 0, 0, 0, 0]

### Step-by-Step Iteration (coin = 2)

Loop from `coin` to `target_amount`, updating `ways[amount]` using:

```python
ways[amount] = ways[amount] + ways[amount - coin]
```

| Amount | Calculation                                    | Updated `ways`       |
| ------ | ---------------------------------------------- | -------------------- |
| 2      | ways\[2] = ways\[2] + ways\[0] = 0 + 1 = **1** | \[1, 0, **1**, 0, 0] |
| 3      | ways\[3] = ways\[3] + ways\[1] = 0 + 0 = **0** | \[1, 0, 1, **0**, 0] |
| 4      | ways\[4] = ways\[4] + ways\[2] = 0 + 1 = **1** | \[1, 0, 1, 0, **1**] |

### Python Code

```python
def coin_combinations(target_amount, coins):
    # Initialize array to store number of ways for each amount
    ways = [0] * (target_amount + 1)
    
    # Base case: one way to make amount 0
    ways[0] = 1
    
    # Loop through each coin
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            ways[amount] += ways[amount - coin]
            
    return ways[target_amount]

# Example usage:
if __name__ == "__main__":
    print(coin_combinations(4, [1, 2, 3]))  # Output: 4
    # Ways: [1,1,1,1], [1,1,2], [2,2], [1,3]
    
    print(coin_combinations(5, [1, 2, 5]))  # Output: 4
    # Ways: [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]
```
