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
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    now = 0
    si = [0] * (n-m+1)
    for i in range(m): now += a[i]*(i+1)
    si[0] = now
    for i in range(n-m+1):
        si[i] = si[i-1] + m * a[m+i-1] - (acc[m+i-1]-acc[i-1])
    return max(si)

if __name__ == '__main__':
    print(main())
    print(f'[Sec] {str(time.time() - StartTime)}')
