def is_good_string(s):
    n = len(s)
    if n < 2:
        return False

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return False
    return True

# Input
s = input().strip()
print("Yes" if is_good_string(s) else "No")
