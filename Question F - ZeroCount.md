```md
# ZeroCount Problem

## Problem Description

You are given a binary string \( B \) of length \( L \) which contains \( K \) ones and the remaining are zeros. The goal is to place the \( K \) ones in the binary string such that the longest contiguous block of zeros is minimized. Once the binary string is constructed, you are required to print the length of the longest contiguous block of zeros.

### Constraints

- \( 0 \leq K \leq L \)
- \( 1 \leq L \leq 10^6 \)

### Input

- A single line consisting of two space-separated integers \( L \) and \( K \).

### Output

- Print a single integer representing the length of the longest contiguous block of zeros.

## Time Limit

1 second

---

## Examples

### Example 1

#### Input

```
3 1
```

#### Output

```
1
```

### Explanation

In this case, \( B \) is of length 3 and contains 1 one. The possible strings that can be constructed are `010`, `001`, and `100`. The maximum length of consecutive zeros is 2 in the latter two cases. However, the optimal configuration is `010`, where the output is 1.

---

### Example 2

#### Input

```
3 3
```

#### Output

```
0
```

### Explanation

In this case, \( B \) is of length 3 and contains all three ones. Therefore, there are no blocks of zeros, leading to an output of 0.

---

## Python Code Solution

```python
def longest_consecutive_zeros(L, K):
    # If K is 0, all are zeros
    if K == 0:
        return L

    # If K equals L, all are ones
    if K == L:
        return 0

    # Calculate the number of zeros
    zeros = L - K
    
    # Calculate the gaps
    # There are K + 1 gaps between K ones
    gaps = K + 1
    
    # The maximum length of zeros in each gap
    max_zeros_per_gap = zeros // gaps
    additional_zeros = zeros % gaps
    
    # If there are extra zeros, the longest block will be max_zeros_per_gap + 1
    if additional_zeros > 0:
        return max_zeros_per_gap + 1
    else:
        return max_zeros_per_gap

# Input reading
L, K = map(int, input().split())

# Output
print(longest_consecutive_zeros(L, K))
```

---

### Explanation of the Code

1. **Edge Cases**:
   - If \( K \) is 0, then all \( L \) characters are zeros, and the longest consecutive zeros will be \( L \).
   - If \( K \) equals \( L \), then there are no zeros, and the output is 0.

2. **Calculation**:
   - Calculate the number of zeros as \( L - K \).
   - The number of gaps created by \( K \) ones is \( K + 1 \).
   - Determine how many zeros can be evenly distributed across the gaps using integer division and the modulus operator.

3. **Output**:
   - If there are extra zeros after distribution, the longest block of zeros will be one more than the evenly distributed length.
   - Otherwise, return the evenly distributed length.

### Complexity

The solution runs in \( O(1) \) time, as it performs a constant number of operations regardless of the size of \( L \) and \( K \).

---

```
