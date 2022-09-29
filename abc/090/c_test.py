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
1 7

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    if n == 1 and m == 1: exit(print(1))
    elif n == 1: exit(print(m-2))
    n -= 2
    m -= 2
    print(n*m)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')