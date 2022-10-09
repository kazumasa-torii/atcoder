"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1
2
3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(2)]
    cnt = []
    def bfs(x, y, c):
        if x >= 2 or y >= n:
            cnt.append(c)
            return
        c = c + maps[x][y]
        bfs(x+1, y, c)
        bfs(x, y+1, c)
        return
    bfs(0, 0, 0)
    print(max(cnt))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
