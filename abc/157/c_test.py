"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3 3
1 7
3 2
1 7

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    li = []
    for _ in range(m):
        x, y = map(int, input().split())
        li.append([x-1, str(y)])
    
    for i in range(1000):
        i = str(i)
        if n != len(i): continue

        flag = True
        for x, y in li:
            if i[x] != y: flag = False
        if flag:exit(print(i))
    print(-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
