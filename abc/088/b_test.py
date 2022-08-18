import sys
import time
from io import StringIO

_INPUT = """\
4
20 18 2 18

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import heapq
def main():
    n = int(input())
    a = list(map(lambda x: int(x) * -1, input().split()))
    heapq.heapify(a)
    one, two = [], []
    idx = 0
    while a:
        tmp = heapq.heappop(a)
        if idx % 2 == 0: one.append(-tmp)
        else: two.append(-tmp)
        idx += 1
    print(abs(sum(one) - sum(two)))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
