"""
dp
遷移がすべてを制する

1. dp[i][j] = Aiまで決めてj個すでに選んでいるときの ΣB*i の Max が遷移
1. 1行目は0ですべて初期化
1. それ以降は現時点の数にプラスして次の数字に係数をかけたものか、次の行の同じ列の数字を比較したものを追加する
1. 最終行の一番大きな数字を出力する
"""
import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    INF = -int(1e19)
    dp = [[INF] * (n+1) for _ in range(m+1)]
    dp[0] = [0] * (n+1)
    for i in range(m):
        for j in range(n):
            if dp[i][j] == INF:continue
            dp[i+1][j+1] = max(dp[i][j]+(i+1)*a[j], dp[i+1][j])
    print(max(dp[-1]))
    return

if __name__ == '__main__':
    main()