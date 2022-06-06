"""
A C G T
0 1 2 3
に対応付されている

ACG = 021 がアウト
その他の条件は下記の通り

i j k l
  0 2 1
  0 1 2
  2 0 1
0   2 1
0 2   1
dp[最後の前の前の文字][最後の前の文字][最後の文字] := 長さ n の文字列が何通り作れるか
ただし実装時には、直前の結果のみひつようなのでDPも一次元にて対応する
"""

MOD = 10 ** 9 + 7
n = int(input())
dp = [[[1] * 4 for _ in [0] * 4] for _ in [0] * 4]
dp[0][2][1] = 0
dp[0][1][2] = 0
dp[2][0][1] = 0
for _ in range(n - 3):
    ndp = [[[0] * 4 for _ in [0] * 4] for _ in [0] * 4]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (i, k, l) == (0, 2, 1) or (i, j, l) == (0, 2, 1):
                        pass
                    else:
                        ndp[j][k][l] += dp[i][j][k]
    dp = ndp
    dp[0][2][1] = 0
    dp[0][1][2] = 0
    dp[2][0][1] = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                dp[j][k][l] %= MOD
print(sum(z for x in dp for y in x for z in y) % MOD)
