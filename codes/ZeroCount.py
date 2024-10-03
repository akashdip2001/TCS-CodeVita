def longest_consecutive_zeros(L, K):
    if K == 0:
        return L
    if K >= L:
        return 0

    Z = L - K
    gaps = K + 1

    base_zeros = Z // gaps
    extra_zeros = Z % gaps

    # Length of longest consecutive zeros
    return base_zeros + (1 if extra_zeros > 0 else 0)

# Input
L, K = map(int, input().strip().split())
print(longest_consecutive_zeros(L, K))
