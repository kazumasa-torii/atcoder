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
chchokudai

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 10 ** 9 + 7
    s = input().strip()
    n = len(s)
    t = 'chokudai'
    dp = [[0] * 9 for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(n):
        for j in range(8):
            dp[i+1][j+1] = dp[i][j+1]
            if s[i] == t[j]:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
    print(dp[n][8])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
"""
chokudai
"""
