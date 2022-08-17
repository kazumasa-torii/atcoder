from distutils.spawn import spawn
import sys
import time
from io import StringIO

_INPUT = """\
6
382253568 723152896 37802240 379425024 404894720 471526144

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i % 2 != 0:exit(print(0))
    while True:
        tmp = []
        for i in range(n):
            a[i] /= 2
            tmp.append(a[i].is_integer())
        if not all(tmp): break
        ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
