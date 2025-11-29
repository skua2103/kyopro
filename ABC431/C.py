N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

j = 0
robot_count = 0
for i in range(N):
    while j < M:
        if H[i] <= B[j]:
            robot_count += 1
            j += 1
            break
        j += 1
    if j == M:
        break

if robot_count >= K:
    print("Yes")
else:
    print("No")
