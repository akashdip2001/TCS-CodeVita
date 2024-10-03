```md
# Orchard Problem

## Problem Description
Orchards are a piece of enclosed land planted with different fruit trees in an orderly manner.

Ashok and Anand are friends. They visited an orchard where lemon (`L`) and mango (`M`) trees are planted in rows. The owner planted the trees in random order in the rows. Some trees bear plenty of fruit, while others don’t yield well.

Both Ashok and Anand select a row of trees, represented by a string where `M` denotes a mango tree and `L` denotes a lemon tree. They decide to pick 3 trees such that no two adjacent trees are of the same type (i.e., alternating `L` and `M`). Whoever has more valid ways to select the trees wins. If the number of possibilities is the same for both, it's a draw. If either input is invalid, print "Invalid input."

## Constraints
- \(1 \leq \text{len(str)} \leq 10^5\)

## Input
- First line consists of a string denoting the trees in Ashok's row.
- Second line consists of a string denoting the trees in Anand's row.

## Output
Print the name of the winner: either "Ashok" or "Anand". If it's a draw, print "Draw". If inputs are invalid, print "Invalid input".

## Time Limit
1 second

## Examples

### Example 1:

**Input:**
```
MMLMLLM
LMLLLMLM
```

**Output:**
```
Anand
```

**Explanation:**
- Ashok's possibilities: 12 ways.
- Anand's possibilities: 16 ways.
Since Anand has more possibilities, he is the winner.

### Example 2:

**Input:**
```
MLLM
LMLL
```

**Output:**
```
Draw
```

**Explanation:**
Both Ashok and Anand have 2 valid possibilities each. So, it’s a draw.

---

## Python Code Solution

```python
def count_possibilities(trees):
    # Validating the string
    if not all(c in "ML" for c in trees):
        return -1  # Invalid input if there are characters other than M or L
    
    n = len(trees)
    possibilities = 0
    
    # Checking all possible triplets (non-adjacent and alternating types)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if trees[i] != trees[j] and trees[j] != trees[k]:
                    possibilities += 1
    
    return possibilities

# Input
ashok_row = input().strip()
anand_row = input().strip()

# Checking if input is valid
if len(ashok_row) < 3 or len(anand_row) < 3:
    print("Invalid input")
else:
    ashok_possibilities = count_possibilities(ashok_row)
    anand_possibilities = count_possibilities(anand_row)
    
    if ashok_possibilities == -1 or anand_possibilities == -1:
        print("Invalid input")
    elif ashok_possibilities > anand_possibilities:
        print("Ashok")
    elif anand_possibilities > ashok_possibilities:
        print("Anand")
    else:
        print("Draw")
```

---

### Explanation:
1. **count_possibilities**: This function counts the number of valid ways to pick three trees such that no two adjacent trees are of the same type (`M` and `L` must alternate).
2. **Input validation**: The function checks whether each character in the input string is either `M` or `L`. If there are any other characters or if the length is less than 3, it prints "Invalid input".
3. **Result determination**: Based on the number of possibilities for each player, it prints "Ashok", "Anand", or "Draw".

### Example:

For input:
```
MMLMLLM
LMLLLMLM
```

The output will be:
```
Anand
```

Anand has more possibilities to pick three non-adjacent trees, so he wins.
```
