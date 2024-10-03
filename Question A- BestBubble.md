# BestBubble Problem

```md
# BestBubble Problem

## Problem Description
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. The problem with bubble sort is its worst case scenario. When the smallest element is in the last position, it takes more time to sort in ascending order, but less time to sort in descending order.

An array is called beautiful if all the elements of the array are in either ascending or descending order. Given an array of numbers, find the minimum swap operations required to make the array beautiful.

## Constraints
- \( 0 < N < 1000 \)
- \( 0 < Arr[i] < 1000 \)

## Input
- First line contains an integer `N` denoting the number of elements in the array.
- Second line consists of `N` integers separated by spaces denoting the elements of the array.

## Output
- A single integer denoting the least number of swap operations required to make the array beautiful.

## Time Limit
1 second

## Examples

### Example 1:

**Input:**
```
5
4 5 3 2 1
```

**Output:**
```
1
```

**Explanation:**
The number of swaps required to sort the elements in ascending order is 9.  
The number of swaps required to sort the elements in descending order is 1.  
The best way is to sort in descending order and swaps required is 1.

### Example 2:

**Input:**
```
5
4 5 1 2 3
```

**Output:**
```
4
```

**Explanation:**
For ascending order:
- Pass 1 requires 3 swaps.
- Pass 2 requires 1 swap.
Total swaps = 6.

For descending order:
- Pass 1 requires 3 swaps.
- Pass 2 requires 1 swap.
Total swaps = 4.

The best way is to sort in descending order, which requires 4 swaps.

---

## Python Code Solution

```python
def bubble_sort(arr, reverse=False):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1] and not reverse) or (arr[j] < arr[j+1] and reverse):
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

def min_swaps_to_beautiful(arr):
    # Copy array for ascending and descending sorts
    ascending_arr = arr[:]
    descending_arr = arr[:]
    
    # Get swap counts
    ascending_swaps = bubble_sort(ascending_arr, reverse=False)
    descending_swaps = bubble_sort(descending_arr, reverse=True)
    
    # Return the minimum swap count
    return min(ascending_swaps, descending_swaps)

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(min_swaps_to_beautiful(arr))
```

---

### Explanation:
- `bubble_sort(arr, reverse)`: This function sorts the array either in ascending or descending order based on the `reverse` flag. It counts the number of swaps performed during the sorting process.
- `min_swaps_to_beautiful(arr)`: This function creates two copies of the input array: one for sorting in ascending order and another for descending. It returns the minimum of the two swap counts.

### Example:

For input:
```
5
4 5 3 2 1
```

The output will be:
```
1
```

This shows that it takes fewer swaps to sort the array in descending order (1 swap) compared to ascending order (9 swaps).
```
