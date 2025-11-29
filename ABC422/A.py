S = input()

world, stage = map(int, S.split("-"))

# 次のステージを計算
if stage == 8:
    world = world + 1
    stage = 1
else:
    stage = stage + 1
# 結果を出力
print(f"{world}-{stage}")
