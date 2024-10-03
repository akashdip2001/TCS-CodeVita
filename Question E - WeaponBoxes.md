```md
# WeaponBoxes Problem

## Problem Description

In a military camp in India, soldiers need weapons, and boxes of varying weights containing these weapons have arrived from different countries. The commander wants to prioritize the boxes with more weight. The commander follows a specific process to manage the boxes:

1. In each cycle, the commander selects the first `N` boxes from the line.
2. He compares the first two boxes and sends the box with the lower weight to the end of the line.
3. This process continues until one box remains from those `N` boxes.
4. The process halts when the same box remains unshifted to the end of the line for `K` consecutive cycles.

Additionally, the total cost for the laborers is calculated as the sum of weights of all shifted boxes except those that have triangular number weights.

### Constraints

- \(1 \leq \text{weight of each box} \leq 10^5\)
- \(1 \leq \text{number of boxes} \leq 10^4\)
- \(1 \leq N, K \leq 10^3\)
- All elements in the array are distinct.

### Input

- First line: Array of integers denoting the weights of all the boxes.
- Second line: Two space-separated integers `N` and `K`, denoting the number of boxes selected in each cycle and the number of consecutive times a box should remain unshifted to halt the process.

### Output

- Print the total amount of money the commander has to give to the workers.

## Time Limit

1 second

---

## Example 1

### Input

```
7 3 6 9 10 2 4 11 5 12 17 1
3 2
```

### Output

```
22
```

### Explanation

In each cycle, select 3 boxes and follow the steps:

1. Compare weights of boxes: 7 and 3 → send 3 to the end.
2. Compare weights of boxes: 7 and 6 → send 6 to the end.
3. Compare weights of boxes: 7 and 9 → send 7 to the end.
4. Continue this until the cycle halts after the box with weight 10 remains unshifted for 2 cycles.

The total amount to be paid for labor is the sum of non-triangular weights of all shifted boxes: \(7 + 9 + 2 + 4 = 22\).

---

## Example 2

### Input

```
6 2 8 14 5 1 3
2 2
```

### Output

```
15
```

### Explanation

1. Compare weights of boxes: 6 and 2 → send 2 to the end.
2. Compare weights of boxes: 6 and 8 → send 6 to the end.
3. Continue until box 14 remains unshifted for 2 cycles.

The total amount to be paid for labor is \(2 + 8 + 5 = 15\).

---

## Python Code Solution

```python
def is_triangular(n):
    # Check if n is a triangular number
    x = (8 * n + 1) ** 0.5
    return x.is_integer() and (x - 1) % 2 == 0

def sum_non_triangular(weights):
    # Calculate the sum of weights that are not triangular
    return sum(weight for weight in weights if not is_triangular(weight))

def weapon_boxes(weights, N, K):
    from collections import deque
    
    boxes = deque(weights)
    count_unshifted = {box: 0 for box in boxes}
    total_shifted_weight = 0
    
    while True:
        current_cycle = []
        for _ in range(N):
            if boxes:
                current_cycle.append(boxes.popleft())
        
        # Processing the current cycle
        for i in range(len(current_cycle) - 1):
            if current_cycle[i] < current_cycle[i + 1]:
                total_shifted_weight += current_cycle[i]
                boxes.append(current_cycle[i])
            else:
                total_shifted_weight += current_cycle[i + 1]
                boxes.append(current_cycle[i + 1])

        last_box = current_cycle[-1]
        count_unshifted[last_box] += 1
        
        # If the last box is unshifted for K consecutive cycles, stop
        if count_unshifted[last_box] == K:
            break
            
    return sum_non_triangular(boxes) + total_shifted_weight

# Input reading
weights = list(map(int, input().split()))
N, K = map(int, input().split())

# Output
print(weapon_boxes(weights, N, K))
```

---

### Explanation of the Code

1. **Triangular Number Check**: The function `is_triangular(n)` checks if a number is a triangular number using its mathematical properties.
2. **Non-Triangular Sum**: The function `sum_non_triangular(weights)` calculates the total weight of boxes that are not triangular numbers.
3. **Main Logic**: The `weapon_boxes` function processes the weights through cycles until a box remains unshifted for `K` cycles, keeping track of total shifted weights and the count of unshifted boxes.
4. **Input Handling**: The weights and parameters are read from input, and the result is printed.

### Complexity

This solution is efficient given the constraints, as it processes the boxes through a manageable number of cycles, making it suitable for \(N\) and \(K\) up to \(1000\) and the maximum weights of \(10^5\).

---

```
