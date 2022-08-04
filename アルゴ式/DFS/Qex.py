"""
実装は読みやすくしないとミスが出てくる
* 分かりづらくなるなら関数に分ける
* 関数に関しては単一責任をもたせるようにする

1. 表を作り黒なのか白なのか判定させる
1. 表をもとにグラフを作る
1. グラフをもとに頂点vから行ける場所をDFSを行う
1. すでに探索済みの場合は、スキップ
1. 未探索の場所から開始出来たらカウントを行う
"""

import sys
import time
from io import StringIO

_INPUT = """\
3 5
#.#.#
.###.
#.#.#
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    # 周囲 4 マスを探索するときに使う、差分を表す配列
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # マス (x, y) がグリッド内のマスであるかを判定する
    def isValid(x, y):
        if 0 <= x < H and 0 <= y < W: return True
        else: return False

    # マス (x, y) の頂点番号(隣接している頂点を格納する場所)
    # 縦方向分掛けて、横方向を足すみたいな感じ
    def getNum(x, y):
        return (x * W + y)

    # 頂点 v を始点とした深さ優先探索
    def dfs(v):
        # 頂点 v を探索済みにする
        seen[v] = True
        # G[v] に含まれる頂点 v2 について、
        for v2 in G[v]:
            # v2 がすでに探索済みならば、スキップする
            if seen[v2]: continue
            # v2 始点で深さ優先探索を行う (関数を再帰させる)
            dfs(v2)
        return

    # main
    # 入力を受け取る
    H, W = map(int, input().split())
    grid = [[0 for _ in range(W)] for _ in range(H)]    # grid[x][y]：マス (x, y) が白なら 0 、黒なら 1
    for x in range(H):
        S = input()
        for y in range(W):
            if S[y] == "#": grid[x][y] = 1
            elif S[y] == ".": grid[x][y] = 0


    G = [[] for _ in range(H * W)]  # グラフを表現する隣接リスト
    # グリッドの情報からグラフを作る
    for x in range(H):
        for y in range(W):
            # マス (x, y) が白マスなら、何もしない
            if grid[x][y] == 0: continue

            v = getNum(x, y)  # マス (x, y) に対応する頂点番号
            # マス (x, y) の上下左右のマスを探索
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # マス (nx, ny) が盤内にあり、黒マスならば、対応する頂点同士を辺で結ぶ
                if isValid(nx, ny):
                    if grid[nx][ny] == 0: continue

                    nv = getNum(nx, ny)   # マス (nx, ny) に対応する頂点番号
                    # 頂点 v から頂点 nv への辺を張る
                    G[v].append(nv)
                    # ダブルカウントされないよう、頂点 nv から頂点 v への辺は張らない

    seen = [False for _ in range(H * W)]    # seen[v]：頂点 v が探索済みなら true, そうでないなら false
    ans = 0 # 答えとなる変数
    for x in range(H):
        for y in range(W):
            # マス (x, y) が白マスなら、何もしない
            if grid[x][y] == 0: continue

            v = getNum(x, y)
            # 頂点 v がすでに訪問済みであれば、スキップ
            if seen[v]: continue
            # そうでなければ、頂点 v を含む連結成分は未探索
            # 深さ優先探索で新たに訪問し、答えを 1 増やす
            dfs(v)
            ans += 1
    # 答えを出力する
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
