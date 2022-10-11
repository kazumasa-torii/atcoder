import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
130 100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    print((a-b)/3 + b)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
