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
10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k, q = map(int, input().split())
    ans = [int(input()) for _ in range(q)]
    syo = k - q
    p = [syo for _ in range(n)]
    for i in ans:
        p[i-1] += 1

    for i in p:
        if i >= 1: print('Yes')
        else: print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
