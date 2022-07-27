import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
3 3
0 0 2 1
WWW
WBW
WWW

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    # 四方向への移動を表すベクトル
    # 0: 下、1: 右、2: 上、3: 左
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    h, w = map(int, input().split())
    sx , sy, gx, gy = map(int, input().split())
    s = [input() for i in range(h)]

    # 各マス (x, y) が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    dist = [[-1] * W for i in range(H)]

    # todo リストを表すキュー
    q = deque()

    dist[sx][sy] = 0
    q.append((sx,sy))

    # DFSを開始
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            x2, y2 = x+dx, y+dy

            # listの範囲外の場合と通れない通路ならスキップ
            if x2 < 0 or x2 >= h: continue
            if y2 < 0 or y2 >= w: continue
            if s[x2][y2] == "B": continue

            # 探索済みならスキップ
            if dist[x2][y2] != -1: continue

            # 各マスを探索する
            dist[x2][y2] = dist[x][y] + 1
            q.append((x2, y2))

    print(dist[gx][gy])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
