import sys
import time
from io import StringIO

_INPUT = """\
3
2 7 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    print(sum(list(map(int, input().split()))))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
