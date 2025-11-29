X = int(input())  # ロボット本体の重さ
N = int(input())  # パーツの種類数
W = [0] + list(map(int, input().split()))
Q = int(input())

total_W = X
attached = set()
for i in range(1, Q + 1):
    P = int(input())

    if P in attached:
        total_W -= W[P]
        attached.remove(P)
    else:
        total_W += W[P]
        attached.add(P)
    print(total_W)
