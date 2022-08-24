import sys
import time
from io import StringIO

_INPUT = """\
2 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    d, n = map(int, input().split())
    if n == 100: n += 1
    print(n*100**d)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
