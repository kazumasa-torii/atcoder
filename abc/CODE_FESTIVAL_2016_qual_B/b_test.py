import sys
import time
from io import StringIO

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int, input().split())
    limit = a + b
    s = input().strip()
    cnt = 0
    overseas = 0
    for i in range(n):
        if s[i] == 'c':
            print('No')
            continue
        if cnt >= limit:
            print('No')
            continue
        if s[i] == 'b': overseas += 1
        if overseas > b and s[i] == 'b':
            print('No')
            continue
        print('Yes')
        cnt += 1
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
