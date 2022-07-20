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
2
1 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 10 ** 9 + 7
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    maina = 0
    for i in range(n):
        c[i] -= maina
        maina += 1
    ans = c[0]
    for i in range(1, n):
        ans *= c[i]
        ans %= mod
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
