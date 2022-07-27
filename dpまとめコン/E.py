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

_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    INF = int(1e18)
    n, w = map(int, input().split())
    li = []
    v = []
    for _ in range(n):
        a, b = map(int, input().split())
        li.append([a, b])
        v.append(b)
    limit = sum(v) + 10
    dp = [[INF] * limit for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(limit):
            if dp[i][j] == INF: continue
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][j+li[i][1]] = min(dp[i+1][j+li[i][1]], dp[i][j] + li[i][0])
    for i in range(limit-1, -1, -1):
        if dp[-1][i] != INF and dp[-1][i] <= w:
            print(i)
            exit()
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
