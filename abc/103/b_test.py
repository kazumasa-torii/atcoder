import sys
import time
from io import StringIO

_INPUT = """\
kyoto
tokyo

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    t = input()

    n = len(s)
    ss = s+s
    for i in range(n, -1, -1):
        if t == ss[i:i+n]:exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
