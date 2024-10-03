def longest_zeros(ashok_row, anand_row):
    def count_possibilities(row):
        n = len(row)
        possibilities = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if row[i] != row[j] and row[j] != row[k] and row[i] != row[k]:
                        possibilities += 1
        return possibilities

    ashok_possibilities = count_possibilities(ashok_row)
    anand_possibilities = count_possibilities(anand_row)

    if ashok_possibilities > anand_possibilities:
        return "Ashok"
    elif anand_possibilities > ashok_possibilities:
        return "Anand"
    else:
        return "Draw"

# Input
ashok_row = input().strip()
anand_row = input().strip()
print(longest_zeros(ashok_row, anand_row))
