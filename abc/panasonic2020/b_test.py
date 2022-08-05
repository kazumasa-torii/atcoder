import sys
import time
from io import StringIO

_INPUT = """\
1000000000 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        print(1)
        exit()
    ans = h * w // 2
    amari = h * w % 2
    print(ans + amari)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
