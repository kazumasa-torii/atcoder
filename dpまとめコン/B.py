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
40 10 20 70 80 10 20 70 80 60

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    INF = int(1e18)
    dp = [INF] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i] = min(dp[i], abs(li[i] - li[i-j]) + dp[i-j])
    print(dp[-1])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
