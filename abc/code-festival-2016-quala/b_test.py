import sys
import time
from io import StringIO

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = dict()
    cnt = 0
    for i in range(n):
        ans[a[i]] = a[a[i]-1]
    for i, v in enumerate(ans):
        if v > ans[v]: continue
        if v == ans[ans[v]]: cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
