import sys
import time
from io import StringIO

_INPUT = """\
3 3
0 0 2 1
WWW
WBW
WWW

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def bfs(x, y, idx):
        if not isValid(x, y): return
        if maps[x][y] == 'B': return
        if x == gh and y == gw: return
        grid[x][y] = idx
        print(idx)
        for d in range(4):
            xd = x + dx[d]
            yd = y + dy[d]
            bfs(xd, yd, idx+1)
        return
    
    def isValid(x, y):
        if 0 <= x < h and 0 <= y < w: return True
        else: return False

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    h, w = map(int, input().split())
    sh, sw, gh, gw = map(int, input().split())
    maps = [input() for _ in range(h)]
    grid = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'B': grid[i][j] = -1
    print(grid)
    bfs(sh, sw, 0)
    print(grid)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
