"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
1 3 2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    li = list(map(lambda x: int(x)-1, input().split()))

    same = 0
    for idx, value in enumerate(li):
        if idx == value:
            same += 1
    
    ans = same * (same - 1) // 2
    for idx, value in enumerate(li):
        if idx < value and li[value] == idx:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
