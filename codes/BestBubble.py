def count_swaps(arr, ascending=True):
    n = len(arr)
    swaps = 0
    sorted_arr = sorted(arr, reverse=not ascending)  # Sort either ascending or descending
    
    # Bubble sort logic to count swaps
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swaps += 1
    return swaps

def min_swaps_to_beautiful(arr):
    arr_copy1 = arr[:]
    arr_copy2 = arr[:]
    
    # Count swaps for ascending order
    ascending_swaps = count_swaps(arr_copy1, ascending=True)
    
    # Count swaps for descending order
    descending_swaps = count_swaps(arr_copy2, ascending=False)
    
    # Return the minimum of the two swap counts
    return min(ascending_swaps, descending_swaps)

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output the minimum number of swaps
print(min_swaps_to_beautiful(arr))
