import sys
import time
from io import StringIO

_INPUT = """\
3 2
1 2
5 5
-2 8

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import sqrt
def main():
    n, d = map(int, input().split())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            tmp = 0
            for k, h in zip(li[i],li[j]):
                tmp += pow(abs(k - h), 2)
            if sqrt(tmp).is_integer():ans+=1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
