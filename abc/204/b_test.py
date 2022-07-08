import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
3
6 17 28

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in li:
        if i <= 10:
            continue
        ans += (i-10)
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
