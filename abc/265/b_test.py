import sys
import time
from io import StringIO

_INPUT = """\
4 1 10
5 7 5
2 10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n, m, t = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    dic = defaultdict(int)
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        dic[x] = y
    for i in range(n):
        t -= a[i]
        if t <= 0: break
        t += dic[i]
    else:exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
