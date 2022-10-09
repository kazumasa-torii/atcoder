"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
def main():
    x = int(input())
    i = x
    li = []
    while True:
        li.append(i)
        if i == 0: break
        i = (i-1)&x
    li.sort()
    for i in li:
        print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
