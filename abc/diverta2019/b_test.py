import sys
import time
from io import StringIO

_INPUT = """\
13 1 4 3000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    r, g, b, n = map(int, input().split())
    cnt = 0
    for R in range(n+1):
        for G in range(n+1):
            ans = R * r + G * g
            if ans <= n and (n - ans) % b == 0 and (n - ans) >= 0 : cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
