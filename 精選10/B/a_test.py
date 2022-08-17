import sys
import time
from io import StringIO

_INPUT = """\
3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    print('Even' if (a*b)%2 == 0 else 'Odd')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
