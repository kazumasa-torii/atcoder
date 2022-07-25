"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法,鳩の巣原理

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
5 3 100
1 2
4 5
2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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
        next = [0] * n
        next, dp = dp, next

        total = 0

        for i in range(n):total += next[i]
        for i in range(n):
            dp[i] = total
            for u in to[i]: dp[i] -= next[u]
            dp[i] -= next[i]
            dp[i] %= mod
    print(dp[0])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
