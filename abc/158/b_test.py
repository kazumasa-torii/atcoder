import sys
import time
from io import StringIO

_INPUT = """\
8 3 4
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int, input().split())
    if a == 0:exit(print(0))
    if b == 0:exit(print(n))
    ab = a + b
    ans = (n // ab) * a
    rem = n % ab
    ans += min(rem, a)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
