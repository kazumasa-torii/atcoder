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
5
7 46 11 20 11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import gcd
def main():
    def lcm(a, b):
        return a * b // gcd (a, b)
    n = int(input())
    a = list(map(int, input().split()))
    tmp = lcm(a[0], a[1])
    for i in range(2, n):
        tmp = lcm(tmp, a[i])
    ans = 0
    tmp -= 1
    for i in a:
        ans = ans + (tmp%i)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
