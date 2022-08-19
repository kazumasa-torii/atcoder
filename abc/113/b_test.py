from distutils.spawn import spawn
import sys
import time
from io import StringIO

_INPUT = """\
3
21 -11
81234 94124 52141

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    li = []
    for i in range(n):
        li.append(abs(t-(h[i]*0.006)-a))
    print(li.index(min(li)) + 1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
