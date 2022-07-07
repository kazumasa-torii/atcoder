import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
1 4 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c = map(int, input().split())
    si = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    print(si[a] + si[b] + si[c])
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
