L = int(input())

n = 1
m = 1
for i in range(L - 1, L - 1 - 11, -1):
    n *= i
    m *= (L - i)
print(n // m)