import sys
import time
from io import StringIO

_INPUT = """\
54

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    def f(n):
        if li[n] == 2:
            return
        if n % 2 == 0:
            tmp = int(n/2)
            li[tmp] += 1
            f(tmp)
        else:
            tmp = 3 * n + 1
            li[tmp] += 1
            f(tmp)
        return
    s = int(input())
    li = defaultdict(int)
    li[s] += 1
    f(s)
    ans = 0
    for _, i in enumerate(li):
        ans += li[i]
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
