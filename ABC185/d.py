N, M = map(int, input().split())

if M == 0:
    print(1)
else:
    A = list(map(int, input().split()))
    A.sort()

    l = []
    if A[0] != 1:
        l.append(A[0] - 1)

    for i in range(1, M):
        if A[i] - A[i - 1] > 1:
            l.append(A[i] - A[i - 1] - 1)

    if A[-1] != N:
        l.append(N - A[-1])

    if len(l) == 0:
        print(0)
    else:
        k = min(l)
        ans = 0
        for x in l:
            ans += (x + k - 1) // k
        print(ans)