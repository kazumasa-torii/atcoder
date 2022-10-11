import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
0 0

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    li = list(map(int, input().split()))
    if len(set(li)) == 1:
        print(li[0])
    elif 0 not in li:
        print(0)
    elif 1 not in li:
        print(1)
    elif 2 not in li:
        print(2)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
