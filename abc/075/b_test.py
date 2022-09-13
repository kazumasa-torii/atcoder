import sys
import time
from io import StringIO

_INPUT = """\
6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    dx = [1, 0, -1, 0, 1, -1, -1, 1]
    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    ans = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '#': 
                ans[i][j] = '#'
                continue
            for k in range(8):
                ni = i + dy[k]
                nj = j + dx[k]
                if ni < 0 or h <=ni:continue
                if nj < 0 or w <=nj:continue
                if maps[ni][nj] == '#':ans[i][j] += 1
            ans[i][j] = str(ans[i][j])
    for i in range(h):print(''.join(ans[i]))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
