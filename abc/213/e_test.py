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
8 8
.#######
########
########
########
########
########
########
#######.

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

# mov3の内包表記で二重ループを書きたくなかったので
from itertools import product
from collections import deque
def main():
    # 上下左右1マス移動と、上下左右3マス以内移動の方法をあらかじめ作っておく
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    mov1 = tuple((r, c) for r, c in zip(dr, dc))
    mov3 = tuple((r, c) for r, c in product(range(-2, 3), repeat=2) if 1 <= abs(r) + abs(c) <= 3)

    def solve():
        dist = [[10 ** 7] * W for _ in range(H)]
        dist[0][0] = 0
        deq = deque()
        deq.appendleft((0, 0, 0))

        while deq:
            cost, r, c = deq.popleft()

            for ar, ac in mov1:
                nr, nc = r + ar, c + ac
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == "." and cost < dist[nr][nc]:
                        dist[nr][nc] = cost
                        deq.appendleft((cost, nr, nc))

            for ar, ac in mov3:
                nr, nc = r + ar, c + ac
                if 0 <= nr < H and 0 <= nc < W:
                    if cost + 1 < dist[nr][nc]:
                        dist[nr][nc] = cost + 1
                        deq.append((cost + 1, nr, nc))
        return dist[-1][-1]

    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        _r = input()
        grid.append(_r)

    print(solve())


if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')