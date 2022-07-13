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
3
1 1 2
2 2 3
3 2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    I = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        l *= 2
        r *= 2
        if t%2 == 0:
            r -= 1
        if t >= 3:
            l += 1
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] > R[j]: continue
            if L[j] > R[i]: continue
            ans += 1
    print(ans)

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
