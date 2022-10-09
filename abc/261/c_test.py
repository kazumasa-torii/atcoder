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
5
newfile
newfile
newfolder
newfile
newfolder

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        tmp = input().strip()
        if dic[tmp] != 0:
            print(f'{tmp}({dic[tmp]})')
            dic[tmp] += 1
        else:
            dic[tmp] += 1
            print(tmp)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
