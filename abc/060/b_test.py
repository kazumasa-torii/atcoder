import sys
import time
from io import StringIO

_INPUT = """\
7 5 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c = map(int, input().split())
    tmp = a
    for i in range(100):
        tmp += a
        if tmp % b == c: exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
