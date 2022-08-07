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
10 -5 -3
9 -6 10 -1 2 10 -1 7 -15 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    # accumulate[i] = A[0] + A[1] + ... + A[i-1]
    accumulate = [0]

    for element in A:
        accumulate.append(accumulate[-1] + element)

    # left[l] = l * L - accumulate[l]
    left = [l * L - accumulate[l] for l in range(N+1)]

    # (N-r) * R + accumulate[r]
    right = [(N-r) * R + accumulate[r] for r in range(N+1)]

    rightmin = right
    for i in range(N-1, -1, -1):
        rightmin[i] = min(rightmin[i], rightmin[i+1])

    ans = L * N

    for l in range(N+1):
        tmp = left[l] + rightmin[l]
        ans = min(ans, tmp)

    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
