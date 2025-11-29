N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0 # 足場1のコストは0
for i in range(N):
    for j in range(i + 1, i + K + 1):
        if j >= N:
            break
        else:
            dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))

print(dp[-1])
