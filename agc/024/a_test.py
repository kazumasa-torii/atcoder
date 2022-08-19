import sys
import time
from io import StringIO

_INPUT = """\
1 2 3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, k = map(int, input().split())
    ans = a - b
    if k % 2 != 0: ans *= -1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
