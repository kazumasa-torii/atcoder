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
1 1
1000000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import gcd
def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, x)
    gcdList = []
    for i in range(1, n+1):
        gcdList.append(abs(a[i] - a[i-1]))
    ans = gcdList[0]
    for i in range(1, len(gcdList)):
        ans = gcd(ans, gcdList[i])
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
