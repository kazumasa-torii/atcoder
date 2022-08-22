import sys
import time
from io import StringIO

_INPUT = """\
5
7 2 3 8 5
3
4 2
1 7
4 13

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    p = [list(map(int, input().split())) for _ in range(m)]

    for i in range(m):
        drink = p[i]
        tmp = 0
        for j in range(n):
            if drink[0]-1 == j:
                tmp+=drink[1]
                continue
            tmp += t[j]
        print(tmp)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
