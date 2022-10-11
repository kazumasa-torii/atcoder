"""
何通りを肌感覚で理解して全探索できるか判断する
基本は、幅優先探索でできるだけ長い距離を探索できるか試していく

幅優先探索というのは理解出来たがどのように実装していくのかは理解出来なかったので見ていく
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
3 3
...
.#.
...

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def dfs(sx, sy, px, py):
        if sx == px and sy == py and seen[px][py] == True: return 0
        seen[px][py] = True

        ret = -10000
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            print(nx, ny)
            if nx < 1 or ny < 1 or nx > H or ny > W or maps[nx][ny] == '#': continue
            if (sx != nx or sy != ny) and seen[nx][ny] == True: continue

            v = dfs(sx, sy, nx, ny)
            ret = max(ret, v+1)
        seen[px][py] = False
        return ret

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    H, W = map(int, input().split())
    maps = [input() for _ in range(H)]

    seen = [[False] * (W+1) for _ in range(H+1)]
    ans = -1
    for i in range(H):
        for j in range(W):
            ans = max(ans, dfs(i, j, i, j))
        print(ans)
    if ans <= 2: ans = -1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
