"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import itertools
def main():
    n, m = map(int, input().split())
    li = [i for i in range(1, m+1)]
    pt = list(itertools.permutations(li, n))
    ans = []
    for i in range(len(pt)):
        tmp = 0
        flag = True
        for j in pt[i]:
            if tmp < j:
                tmp = j
                continue
            flag = False
            break
        if flag: ans.append(pt[i])
    ans.sort()
    for i in ans:
        print(*i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
