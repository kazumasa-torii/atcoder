import sys
import time
from io import StringIO

_INPUT = """\
-9982443534

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    c = 998244353
    print(n%c)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
