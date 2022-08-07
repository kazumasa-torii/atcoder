import sys
import time
from io import StringIO

_INPUT = """\
3 70
20 30 10

"""

StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, x = map(int, input().split())
    ch = list(map(int, input().split()))
    cnt = 0
    ch.sort()
    for i in range(n):
        if x < ch[i]: break
        x -= ch[i]
        cnt += 1
    if x > 0 and cnt == n: cnt -= 1
    print(max(cnt, 0))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
