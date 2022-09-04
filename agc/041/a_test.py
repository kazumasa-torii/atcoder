import sys
import time
from io import StringIO

_INPUT = """\
5 2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int, input().split())
    sa = b-a
    if sa % 2 == 0:
        print(sa//2)
    else:
        print(min(a-1, n-b)+1+(b-a-1)//2)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
