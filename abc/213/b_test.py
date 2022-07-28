import sys
import time
from io import StringIO

_INPUT = """\
5
3 1 4 15 9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from copy import deepcopy
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = deepcopy(a)
    ans.sort()
    print(a.index(ans[-2]) + 1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
