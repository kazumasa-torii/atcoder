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
3 2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    A, B, C = map(int, input().split())
    ans = str()
    if A == 0 and B == 0:
        ans = '='
    elif A == 0:
        ans = '<'
    elif B == 0:
        ans = '>'
    elif C % 2 == 0:
        if A < 0:
            A *= -1
        if B < 0:
            B *= -1
    if A < B:
        ans = '<'
    elif A > B:
        ans = '>'
    elif A == B:
        ans = '='


    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
