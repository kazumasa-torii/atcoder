import sys
import time
from io import StringIO

_INPUT = """\
4
3
4
1
2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = [int(input()) - 1 for _ in range(n)]
    memo = [False] * n
    button = 0
    while True:
        if memo[button]:break
        memo[button] = True 
        button = a[button]
    print(sum(memo) - 1 if memo[1] else -1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
