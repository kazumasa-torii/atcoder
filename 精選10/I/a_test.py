import sys
import time
from io import StringIO

_INPUT = """\
9 45000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    satu = [10000, 5000, 1000]
    ans = []
    n, y = map(int, input().split())
    for i in satu:
        tmp = y // i
        y -= tmp*i
        ans.append(tmp)
    if sum(ans) <= n:print(*ans)
    else:print('-1 -1 -1')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
