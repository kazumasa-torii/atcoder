"""
ピラミッドの中心の座標を決め打ち、全探索を行うのが楽。
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
2 3 5
2 1 5
1 2 5
3 2 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    height_dat = [list(map(int, input().split())) for _ in range(N)]

    # 後の処理の中で仮の高さを決定するための、
    # h = 0 でない座標を一つ見つけておく。
    for x, y, h in height_dat:
        if h == 0: continue
        px, py, ph = x, y, h
        break

    # ピラミッドの中心を、(cx, cy), 仮の高さを ch とする。
    for cx in range(101):
        for cy in range(101):
            # まずは仮の高さを決定する。
            ch = ph + abs(px - cx) + abs(py - cy)
            # 改めて、全ての情報に合致するかを確認。
            for x, y, h in height_dat:
                predict = max(0, ch - abs(x - cx) - abs(y - cy))
                if h != predict: break
            # すべての情報に合致すれば、出力
            else: print(cx, cy, ch)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
