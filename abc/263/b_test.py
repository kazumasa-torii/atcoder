import sys
import time
from io import StringIO

_INPUT = """\
10
1 2 3 4 5 6 7 8 9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.insert(0, 0)
    tmp = li[-1]
    cnt = 0
    while tmp != 0:
        cnt += 1
        print(li[tmp])
        tmp = li[tmp-1]
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
