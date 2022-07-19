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
7 1000000000000
99 8 2 4 43 5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
from copy import deepcopy
def main():
    n, k = map(int, input().split())
    hand = k // n
    amari = k % n
    a = list(map(int, input().split()))
    b = deepcopy(a)
    b.sort()
    num = defaultdict(int)
    for i in b:
        num[i] = hand
    while amari > 0:
        for _, i in enumerate(num):
            if amari == 0:
                break
            num[i] += 1
            amari -= 1
    for i in range(n):
        print(num[a[i]])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
