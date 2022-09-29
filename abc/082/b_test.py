import sys
import time
from io import StringIO

_INPUT = """\
cd
abc

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    print('Yes' if s < t else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
