N = int(input())
T = list(map(int, input().split()))

sorted_indices = sorted(range(N), key=lambda i: T[i])

print(sorted_indices[0] + 1, sorted_indices[1] + 1, sorted_indices[2] + 1)
