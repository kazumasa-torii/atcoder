import sys
import time
from io import StringIO

_INPUT = """\
3
5 7
2 6
8 10

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    ma = int(1e19)
    mb = 0
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ma = min(a, ma)
        mb = max(b, mb)
        ab.append([a,b])
    ans = int(1e19)
    for i in range(ma, mb+1):
        for j in range(i+1, mb+1):
            tmp = 0
            for k, h in ab:
                tmp += abs(i-k)+1
                tmp += abs(j-h)+1
            ans = min(tmp, ans)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
