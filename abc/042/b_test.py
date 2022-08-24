import sys
import time
from io import StringIO

_INPUT = """\
3 3
dxx
axx
cxx

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, l = map(int, input().split())
    s = [input() for _ in range(n)]
    s.sort()
    print(''.join(s))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
