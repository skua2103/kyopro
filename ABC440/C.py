T = int(input())
for i in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    buckets = [0] * (2 * W)
    for i in range(N):
        buckets[(i + 1) % (2 * W)] += C[i]

    extended_buckets = buckets + buckets
    current_sum = sum(extended_buckets[:W])
    min_cost = current_sum

    for start in range(1, 2 * W):
        current_sum = (
            current_sum - extended_buckets[start - 1] + extended_buckets[start + W - 1]
        )

        min_cost = min(current_sum, min_cost)

    print(min_cost)
