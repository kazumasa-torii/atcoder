import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##.

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    dx = [-1, 0, 0, 0]
    dy = [0, -1, 1, 1]
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    memo = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == ".":continue 
            # 隣接したマスの黒い場所があるか判定
            for k in range(4):
                di = i + dx[k]
                dj = j + dy[k]
                if di < 0 or dj < 0: continue
                if di >= h or dj >= w: continue
                if maps[di][dj] == ".":continue
                memo[di][dj] = True
                memo[i][j] = True
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "#" and not memo[i][j]: exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')