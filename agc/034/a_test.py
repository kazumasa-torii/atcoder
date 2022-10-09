import sys
import time
from io import StringIO

_INPUT = """\
15 1 3 15 13
...#.#...#.#...

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b, c, d = map(int, input().split())
    s = input()
    for i in range(a, max(c, d)):
        if s[i-1:i+1] == '##':exit(print('No'))
    if c < d: exit(print('Yes'))
    for i in range(b, d):
        if s[i-1:i+2] == '...':exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
