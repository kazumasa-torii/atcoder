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
6 3
2 7 1 8 2 8
2 10
3 1
5 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    cn = 100
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    coin = [0] * cn
    dp = [[0] * cn for _ in range(cn)]
    for i in range(m):
        c, y = map(int, input().split())
        coin[c] = y

    dp[0][0] = 0
    for i in range(n):
        for j in range(i):
            dp[i][j] = dp[i-1][j-1] + x[i] + coin[j]
        dp[i][0] = 0
        for j in range(i):
            print(dp[i-1][j])
            dp[i][0] = max(dp[i][0], dp[i-1][j])
    ans = 0

    # for i in range(n):
    #     ans = max(ans, dp[n][i])
    # print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
