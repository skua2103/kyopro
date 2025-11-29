N, A, B = map(int, input().split())
S = input()
if B == 0:
    ans = S[A:]
else:
    ans = S[A:-B]

print(ans)
