"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, M = map(int, input().split())
    ABC = map(int, input().split())
    d = [[1 << 60] * N for _ in range(N)]

    for i in range(N):
        d[i][i] = 0
    
    for a, b, c in zip(ABC, ABC, ABC):
        d[a-1][b-1] = c
    ans = 0
    for k in range(N):
        nxt = [0 * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if nxt[i][j] < 1 << 59:
                    ans += nxt[i][j]
        d = nxt
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
