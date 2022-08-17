import sys
import time
from io import StringIO

_INPUT = """\
72
128 256
myonmyon

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a = int(input())
    b, c = map(int, input().split())
    s = input().strip()

    print(f'{a+b+c} {s}')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
