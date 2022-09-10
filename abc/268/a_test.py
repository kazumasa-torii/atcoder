import sys
import time
from io import StringIO

_INPUT = """\
31 9 24 31 24

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    print(len(set(map(int, input().split()))))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
