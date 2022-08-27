import sys
import time
from io import StringIO

_INPUT = """\
atcoder

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    print(s[len(s)//2])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
