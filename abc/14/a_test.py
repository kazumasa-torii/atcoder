import sys
import time
from io import StringIO

_INPUT = """\
4 12 20

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    A, B, C = map(int, input().split())

    if A % 2 == 1 or  B % 2 == 1 or C % 2 == 1:
        exit(print(0))

    if A == B == C: exit(print(-1))

    ans = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = B // 2 + C // 2, C // 2 + A // 2, A // 2 + B // 2
        ans += 1

    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
