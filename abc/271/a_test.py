import sys
import time
from io import StringIO

_INPUT = """\
12

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    n = '{:02x}'.format(n)
    print(n.upper())
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
