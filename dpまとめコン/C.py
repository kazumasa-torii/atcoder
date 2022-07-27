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
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    A = 0
    B = 0
    C = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if i == 0:
            A += a
            B += b
            C += c
            continue
        ab = max(A, B)
        bc = max(C, B)
        ac = max(A, C)
        A = bc + a
        B = ac + b
        C = ab + c
    print(max(A, B, C))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
