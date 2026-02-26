import sys

input = sys.stdin.readline


class BIT:
    # インスタンス内のデータの初期化
    def __init__(self, n):
        self.n = n  # 数列の長さ
        self.bit = [0] * (n + 1)  # BITでデータを格納する箱の準備

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta  # リストaの中身を用意した箱に格納していく
            i += i & (-i)

    def query2(self, i):
        sum = 0
        while i > 0:
            sum += self.bit[i]
            i -= i & (-i)
        return sum

    def range_query2(self, l, r):
        return self.query2(r) - self.query2(l - 1)


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    bit = BIT(n)
    for i, v in enumerate(a):
        bit.update(i + 1, v)  # 1-indexed で初期化

    out = []
    for _ in range(q):
        line = list(map(int, input().split()))
        if line[0] == 1:
            x = line[1] - 1  # 0-indexed
            # a[x] と a[x+1] を交換
            diff = a[x + 1] - a[x]
            bit.update(x + 1, diff)  # a[x] を a[x+1] の値に
            bit.update(x + 2, -diff)  # a[x+1] を a[x] の値に
            a[x], a[x + 1] = a[x + 1], a[x]
        else:
            l, r = line[1], line[2]
            out.append(bit.range_query2(l, r))

    print("\n".join(map(str, out)))


main()
