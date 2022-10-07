import sys
import time
from io import StringIO

_INPUT = """\
6 3 3
7
6
2
8
10
6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, c, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    t.sort()
    ans = 0
    cnt = 0
    te = 0
    for i in range(n):
        if te < t[i] or cnt == c:
            ans += 1
            te = t[i] + k
            cnt = 1
        else: cnt += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
