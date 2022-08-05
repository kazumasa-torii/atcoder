import sys
import time
from io import StringIO

_INPUT = """\
4 10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int,input().split())
    ans = a
    cnt = 1
    while True:
        if ans >= b: break
        ans -= 1
        ans += a
        cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
