N, M, T = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]

d = N
for i in range(M):
    d -= L[i][0] - L[i-1][1] if i > 0 else L[i][0]
    if d <= 0:
        break
    d += (L[i][1] - L[i][0])
    if d > N:
        d = N
d -= T - L[M-1][1]

if d > 0:
    print("Yes")
else:
    print("No")
