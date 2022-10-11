import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
6
3 1 4 1 5 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    N = int(input())
    dic = defaultdict(int)
    for i in map(int, input().split()):
        dic[i] += 1

    for i, v in enumerate(dic):
        if dic[v] > 1:
            print('No')
            sys.exit()

    print('Yes')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
