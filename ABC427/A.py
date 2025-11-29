S = input()

# 中央の文字のインデックス（0始まり）
middle_index = len(S) // 2

# 中央の文字を削除した文字列を出力
print(S[:middle_index] + S[middle_index + 1:])