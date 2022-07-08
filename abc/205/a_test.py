import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
37 450

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    A, B = map(int, input().split())
    print((A/100) * B)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
