N = int(input())

ans = 0
for i in range(1, N + 1):
    j = i**3
    if i % 2 == 1:
        j *= -1
    ans += j
print(ans)
