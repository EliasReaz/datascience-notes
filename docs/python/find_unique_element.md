# Python: Two-Pointer Technique to Find Unique Elements

## Objective

Use two-pointer movement to identify unique elements from a sorted list of integers.

## Problem Statement

Given a **sorted** list of integers, return a list of unique elements (i.e., remove duplicates) using the **two-pointer** technique.

## Example

- Input nums = [1, 1, 2, 2, 3, 4, 4, 5]

- Output nums = [1, 2, 3, 4, 5]

### Code Snippet

```python

def remove_duplicates(nums):
    if not nums:
        return []

    i = 0  # slow pointer, keep track of the last unique number's index

    for j in range(1, len(nums)):  # fast pointer, iterate through the list
    
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return nums[:i+1]
```

### Execution Steps

| Step | i | j | num[i] | num[j] | num[j] != num[i] | Action | nums |
|------|---|---|--------|--------|------------------|--------|------|
| 0    | 0 | 1 |   1    |   1    |        False      |        |[1,1,2,2,3,4,4,5]|
| 1    | 0 | 2 |   1    |   2    |        True       | i += 1 |[1,2,2,2,3,4,4,5]|
| 2    | 1 | 3 |   2    |   2    |        True       | i += 1 |[1,2,3,2,3,4,4,5]|
| 3    | 2 | 4 |   3    |   3    |        True       | i += 1 |[1,2,3,4,3,4,4,5]|
| 4    | 3 | 5 |   4    |   4    |        True       | i += 1 |[1,2,3,4,5,4,4,5]|
| 5    | 4 | 6 |   5    |   5    |        True       | i += 1 |[1,2,3,4,5,5,4,5]|

### How it works

1. **Initialization**: Start with two pointers, `i` (slow) and `j` (fast). `i` keeps track of the last unique element's index, while `j` iterates through the list.
2. **Comparison**: For each element at index `j`, check if it is different from the element at index `i`. If it is, increment `i` and update `nums[i]` with `nums[j]`.  
3. **Result**: The unique elements are now at the beginning of the list, and the length of the unique elements is `i + 1`.
4. **Return**: Return the list of unique elements by slicing `nums` up to `i + 1`.
