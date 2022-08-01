import sys
import time
from io import StringIO

_INPUT = """\
3000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    y = int(input())
    x = y % 4
    if x == 3:
        print(y-1+4)
    elif x == 2:
        print(y)
    elif x == 1:
        print(y+1)
    elif x == 0:
        print(y+2)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
