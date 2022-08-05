import sys
import time
from io import StringIO

_INPUT = """\
1079

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    tax = 1.08
    one = int(n / tax)
    two = one + 1
    if int(one * tax) == n:print(one)
    elif int(two * tax) == n:print(two)
    else: print(':(')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
