"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3
2 3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    li = list(map(int, input().split()))
    dic = dict()
    for i in range(n):
        dic[i] = li[i]
    dic = sorted(dic.items(), key=lambda x:x[1])
    ans = []
    for i in range(n):
        x, y = dic[i]
        ans.append(x + 1)
    print(*ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
