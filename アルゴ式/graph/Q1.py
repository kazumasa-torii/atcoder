"""
考え方として必要なのは、
* すでに通ったところをメモしておくlist
* graphのデータ構造
* graphのデータ構造を使った探索方法
ここらへんが理解できていない気がする
どう動作するのかを理解して動きを理解する。
"""

import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4 4
0 1
2 1
3 0
1 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    
    # 各頂点が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    dist = [-1] * N

    # k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
    nodes = [[] for i in range(N)]

    # 頂点 0 を始点とする
    dist[0] = 0
    nodes[0] = [0]

    # k 手目の探索をする
    for k in range(1, N):
        # k-1 手目に探索された各頂点 v に対して
        for v in nodes[k - 1]:
            # 頂点 v から 1 手で行ける頂点 next_v を探索
            for next_v in G[v]:
                # 頂点 next_v が探索済みであれば何もしない
                if dist[next_v] != -1:
                    continue

                # 頂点 next_v を探索する
                dist[next_v] = dist[v] + 1
                nodes[k].append(next_v)
    # k = 0, 1, ..., N-1 手目に探索された頂点を出力
    for k in range(N):
        # 頂点番号を小さい順に
        nodes[k].sort()

        # 出力
        print(*nodes[k])


    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
