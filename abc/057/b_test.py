import sys
import time
from io import StringIO

_INPUT = """\
5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        a, b = ab[i]
        tmp = []
        for j in range(m):
            c, d = cd[j]
            tmp.append(abs(a-c)+abs(b-d))
        print(tmp.index(min(tmp)) + 1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
