import sys
import time
from io import StringIO

_INPUT = """\
1 10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    if n == 1:exit(print(k))
    ans = k*(k-1)
    for i in range(n-2):
        ans *= k-1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
