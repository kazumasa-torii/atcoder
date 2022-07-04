import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
200

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import ceil
def main():
    N = int(input())
    print(ceil(N / 100))
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
