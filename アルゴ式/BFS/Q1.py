"""
考え方として必要なのは、
* すでに通ったところをメモしておくlist
* graphのデータ構造
* graphのデータ構造を使った探索方法
ここらへんが理解できていない気がする
どう動作するのかを理解して動きを理解する。
"""

import sys
import time
from io import StringIO
from typing import List, Tuple

_INPUT = """\
7 13
4 3
1 4
1 6
0 3
5 0
6 0
5 6
2 6
6 4
5 1
2 4
4 5
5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    q = deque()
    for i in G[0]:
        q.append(i)
    memo = [False for _ in range(n)]
    memo[0] = True

    ans = []
    ans.append([0])

    for i in range(1, n):
        get = []
        while q:
            tmp = q.popleft()
            if memo[tmp]:
                continue
            memo[tmp] = True
            get.append(tmp)
        if get:
            ans.append(get)
        for j in G[i]:
            q.append(j)
    for i in ans:
        i.sort()
        print(*i)

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
