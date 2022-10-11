import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
3 4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import heapq
def main():
    li = list(map(lambda x: int(x) * -1, input().split()))
    heapq.heapify(li)
    a = heapq.heappop(li) * -1
    b = heapq.heappop(li) * -1
    print(a + b)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
