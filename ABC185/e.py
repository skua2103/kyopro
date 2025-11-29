N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(
            dp[i-1][j],
            dp[i][j-1],
            dp[i-1][j-1] + (2 if A[i-1] == B[j-1] else 1)
        )

print(N + M - dp[N][M])
