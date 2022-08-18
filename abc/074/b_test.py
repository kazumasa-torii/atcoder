import sys
import time
from io import StringIO

_INPUT = """\
5
20
11 12 9 17 12

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    k = int(input())
    line = k // 2
    one = []
    two = []
    tmp = list(map(int, input().split()))
    for i in tmp:
        if line < i: two.append(i)
        else: one.append(i)
    ans = sum(one)
    for i in two:
        ans += abs(i - k)
    print(ans * 2)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
