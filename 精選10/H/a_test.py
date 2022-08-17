import sys
import time
from io import StringIO

_INPUT = """\
7
50
30
50
100
50
80
30

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    x = set()
    for _ in range(n):
        x.add(int(input()))
    print(len(x))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
