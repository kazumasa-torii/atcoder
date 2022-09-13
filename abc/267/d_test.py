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
10 4
-3 1 -4 1 -5 9 -2 6 -5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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
    print(f'[Sec] {str(time.time() - StartTime)}')