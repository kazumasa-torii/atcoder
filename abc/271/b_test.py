from distutils.spawn import spawn
import sys
import time
from io import StringIO

_INPUT = """\
2 2
3 1 4 7
2 5 9
1 3
2 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    num = []
    for i in range(n):
        num.append(list(map(int, input().split()))[1:])
    for i in range(m):
        x, y = map(int, input().split())
        print(num[x-1][y-1])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
