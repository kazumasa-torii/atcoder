import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
5 1 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
