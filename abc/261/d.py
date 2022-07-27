"""
要するにDP

1. 全探索しないと行けないかつ全ては網羅出来ない場合は、基本DPを疑う
1. パラメータを保持する内容を選定する（今回は、i回目のコイントスとカウンタとしてjを保持する）
1. dp[i][j]はi回目のコイントスでカウンタがjの時にもらえる最大値
1. 初期値は限りなく小さい数値にする スタートはdp[i][j]は0
1. コイントスで表が出た場合の繊維はjと等しいようならボーナスが存在するかで変わる
1. 存在する場合は、その時のYiの値をyとすると
dp[i][j] = max(dp[i][j], dp[i-1][j-1] + x[i-1] + b[j])

存在しない場合は、
dp[i][j] = max(dp[i][j], dp[i-1][j-1] + x[i-1])
1. 裏が出た場合は dp[i][0] = max(dp[i-1])
"""
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    limit = n+1
    x = list(map(int, input().split()))
    b = [0 for i in range(limit)]
    for i in range(m):
        c, y = map(int, input().split())
        b[c] = y

    INF = int(1e18)
    dp = [[-INF] * (limit) for _ in range(limit)]
    dp[0][0] = 0
    mx = 0

    for i in range(1, limit):
        dp[i][0] = mx
        mx = 0
        for j in range(1, limit):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + x[i-1] + b[j])
            mx = max(dp[i][j], mx)
    print(max(dp[-1]))
    return

if __name__ == '__main__':
    main()
