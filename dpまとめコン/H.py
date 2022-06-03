"""
地図で行ける通り数は前の通り数の上と左の合計から算出されるから
dpに行ける状態数を記載して求めやすくする
1 1 1
1 2 3
1 3 6
みたいに状態を保存して進めていくようにする
"""
H, W = map(int, input().split())
tiz = [list(input()) for _ in range(H)]
mod = 10 ** 9 + 7

# 前の段階を記録するために作成
dp = [[0] * (W) for _ in range(H)]
# 初期値は１
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if tiz[i][j] == '#':
            continue
        # 各ステップごとにmodを取っておいて最終の値を少なく計算していく
        if i - 1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod
print(dp[H-1][W-1])
