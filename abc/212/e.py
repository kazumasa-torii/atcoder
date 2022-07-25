"""
ちょっといまいちわからない
そもそも全部を取得できるやり方がいまいち理解できないのでそこを考える

1. 動的計画法で解けるが辺の数が多すぎて遷移が追いつかないので言い換えを行う
1. 一旦使えない道のことは忘れて前としから移動できることにして全都市の木見合わせ数を計算する
1. 同じ都市から同じ都市に直接移動出来ないのでその分を引く
1. 使えないM個の変それぞれに付いて組み合わせ数を引く
"""

import sys
input = sys.stdin.readline
def main():
    mod = 998244353
    n, m , k = map(int, input().split())
    to = [[] for _ in range(n)]

    for i in range(m):
        a, b = map(lambda x: int(x) - 1,  input().split())
        to[a].append(b)
        to[b].append(a)

    dp = [0] * n
    dp[0] = 1

    for _ in range(k):
        prev = [0] * n
        # swapして以前のデータをprevに入れておく
        prev, dp = dp, prev
        # 使えない辺はないと仮定して全部の辺数を調べる
        total = 0
        for i in range(n):total += prev[i]
        print(prev)
        for i in range(n):
            dp[i] = total
            # 行けない辺の場所分引いてく
            for u in to[i]: dp[i] -= prev[u]
            # 同じ都市は直接行けないのでその分も引く
            dp[i] -= prev[i]
            dp[i] %= mod
    print(dp[0])
    return

if __name__ == '__main__':
    main()

