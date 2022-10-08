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
5 6
-2 -2 -5 -7 -15

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(m):
        for j in range(n, 0, -1):
            a[j] += j
        tmp = set(a[1:])
        if 0 not in tmp: break
        elif 1 not in tmp: print(1)
        elif 2 not in tmp: print(2)
        elif 3 not in tmp: print(3)
        elif 4 not in tmp: print(4)
        elif 5 not in tmp: print(5)
        elif 6 not in tmp: print(6)
        elif 7 not in tmp: print(7)
        elif 8 not in tmp: print(8)
        elif 9 not in tmp: print(9)
    for k in range(m-i):
        print(0)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
