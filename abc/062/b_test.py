import sys
import time
from io import StringIO

_INPUT = """\
1 1
z

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    a.insert(0,'#'*w)
    a.append('#'*w)
    for i in range(h+2):
        a[i] = '#'+a[i]+'#'
    for ans in a:
        print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
