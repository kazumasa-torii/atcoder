import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(1, b+1):
        if i >= a:
            ans += 1

    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
