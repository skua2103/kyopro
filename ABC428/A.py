S, A, B, X = map(int, input().split())

cycle_count, last_cycle_time = divmod(X, A + B)

total_distance = A * S * cycle_count

if last_cycle_time > A:
    total_distance += A * S
else:
    total_distance += last_cycle_time * S

print(total_distance)