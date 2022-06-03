import sys
input = sys.stdin.readline
"""
DPで解く
1.各項目でまず値を取得
1.計算した求めた値を累積和で値を計算して設置
1.累積和で作成された値を確認しながらDPを進めていく

"""
# N, M, K = map(int,input().split())
N, M, K = 4, 9, 3
Mod = 998244353

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,M+1):
    dp[1][i] = 1

for i in range(2,N+1):
    CumSum = [0]*(M+1)

    for x in range(1,M+1):
        CumSum[x] = CumSum[x-1]+dp[i-1][x]
        CumSum[x] %= Mod

    for x in range(1,M+1):
        if K == 0:
            dp[i][x] = CumSum[M]
        else:
            if 1 <= x-K:
                dp[i][x] += CumSum[x-K]
            if x+K <= M:
                dp[i][x] += CumSum[M]-CumSum[x+K-1]

        dp[i][x] %= Mod

ans = 0
for x in range(1,M+1):
    ans += dp[N][x]
    ans %= Mod

print(dp)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 6, 11, 15, 19, 23, 27, 31, 36, 42]
[0, 27, 50, 69, 90, 112, 133, 152, 175, 202]

[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 6, 5, 4, 4, 4, 4, 4, 5, 6],
    [0, 27, 23, 19, 21, 22, 21, 19, 23, 27],
    [0, 133, 112, 90, 96, 100, 96, 90, 112, 133]
]
