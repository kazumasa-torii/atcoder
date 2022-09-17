import sys
import time
from io import StringIO

_INPUT = """\
1 2 5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, d = map(int, input().split())
    print((a+b) * (c-d))
    print("Takahashi")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
