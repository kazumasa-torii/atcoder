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
3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if i+1 >= H:
                continue
            if j+1 >= W:
                continue
            # マイナス
            if A[i][j] > B[i][j]:
                ab = abs(A[i][j] - B[i][j])
                A[i][j] -= ab
                A[i+1][j] -= ab
                A[i][j+1] -= ab
                A[i+1][j+1] -= ab
            # プラス
            elif A[i][j] < B[i][j]:
                ab = abs(A[i][j] - B[i][j])
                A[i][j] += ab
                A[i+1][j] += ab
                A[i][j+1] += ab
                A[i+1][j+1] += ab
            elif A[i][j] == B[i][j]:
                continue
            cnt += ab
    if A == B:
        print('Yes')
        print(cnt)
    else:
        print('No')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
