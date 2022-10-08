import sys
import time
from io import StringIO

_INPUT = """\
4 2
3 1 2 4
3 2 3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    p = [[i+1] for i in range(n)]
    for _ in range(m):
        a = list(map(int, input().split()))
        for i in a[1:]:
            p[i-1].extend(a[1:])
    for i in p:
        tmp = set()
        for j in i:
            tmp.add(j)
        if len(tmp) != n:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
