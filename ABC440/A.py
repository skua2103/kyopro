X, Y = map(int, input().split())

ans = X
for _ in range(Y):
    ans = ans * 2

print(ans)
