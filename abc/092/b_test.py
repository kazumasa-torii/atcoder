import sys
import time
from io import StringIO

_INPUT = """\
3
7 1
2
5
10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    d, x = map(int, input().split())
    ans = 0
    for _ in range(n):
        day = 1
        tmp = int(input())
        while day <= d:
            ans += 1
            day += tmp
    print(ans + x)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
