import sys
import time
from io import StringIO

_INPUT = """\
3 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = 'atcoder'
    l, r = map(int, input().split())
    l -= 1
    print(s[l:r])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
