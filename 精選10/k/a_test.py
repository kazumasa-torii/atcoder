import sys
import time
from io import StringIO

_INPUT = """\
2
5 1 1
100 1 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    ta, tb, tc = 0, 0, 0
    for _ in range(n):
        flag = True
        a, b, c = map(int, input().split())
        bc = b + c
        if a % 2 == 0:
            if bc % 2 != 0 :flag = False
        else:
            if bc % 2 == 0:flag = False
        if not flag: exit(print('No'))
        a = abs(a - ta)
        b = abs(b - tb)
        c = abs(c - tc)
        if b + c > a:exit(print('No'))
        ta, tb, tc = a, b, c
    print('Yes')

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
