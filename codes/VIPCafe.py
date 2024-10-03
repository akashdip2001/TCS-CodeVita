def orders_until_served(orders, K):
    friend_index = K - 1
    friend_priority = orders[friend_index]
    count = 0

    while True:
        served = False
        max_priority = max(orders)

        for i in range(len(orders)):
            if orders[i] == max_priority:
                count += 1
                if i == friend_index:
                    return count
                else:
                    orders.pop(i)
                    for j in range(i):
                        orders[j] += 1
                served = True
                break

        if not served:
            break

# Input
N = int(input().strip())
orders = list(map(int, input().strip().split()))
K = int(input().strip())
print(orders_until_served(orders, K))
