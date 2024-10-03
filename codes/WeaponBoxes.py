def is_triangular(n):
    if n < 0:
        return False
    x = (8 * n + 1) ** 0.5
    return x * x == (8 * n + 1)

def calculate_payment(boxes, N, K):
    length = len(boxes)
    cycles = 0
    unshifted_count = [0] * length
    unshifted = [False] * length

    while True:
        cycles += 1
        remaining = boxes[:N]
        next_queue = []
        
        # This will hold the indexes of boxes
        indexes = list(range(N))

        # Compare boxes and shift
        for i in range(0, N, 2):
            if i + 1 < N:
                if remaining[i] < remaining[i + 1]:
                    next_queue.append(remaining[i + 1])
                    unshifted_count[boxes.index(remaining[i])] += 1
                else:
                    next_queue.append(remaining[i])
                    unshifted_count[boxes.index(remaining[i + 1])] += 1
        
        # Update boxes: remove first N and append shifted boxes
        boxes = boxes[N:] + next_queue
        
        # Check unshifted count
        if any(unshifted_count[i] >= K for i in range(length)):
            break

    # Calculate the payment
    payment = sum(box for i, box in enumerate(boxes) if not is_triangular(box))
    return payment

# Input
weights = list(map(int, input().strip().split()))
N, K = map(int, input().strip().split())
print(calculate_payment(weights, N, K))
