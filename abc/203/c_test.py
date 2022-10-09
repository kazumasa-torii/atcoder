"""

"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
2 3
2 1
5 10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from operator import itemgetter
def main():
    ans = 0
    N, K = map(int, input().split())
    li = []
    for _ in range(N):
        x, y = map(int, input().split())
        li.append([x, y])
    li.sort(key=itemgetter(0))
    ans += K
    j = 0
    while j < N and li[j][0] <= ans:
        ans += li[j][1]
        j += 1
    print(ans)

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
