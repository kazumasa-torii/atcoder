"""

"""
from os import cpu_count
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
1 2
4 2
3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
sys.setrecursionlimit(10 ** 6)
def main():
    def dfs(v, p=-1):
        ans.append(v)
        for v2 in g[v]:
            if v2 == p: continue
            dfs(v2, v)
            ans.append(v)
        return
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    ans = []
    for i in range(n):
        if not g[i]: continue
        g[i].sort()

    dfs(0)
    for i in range(len(ans)):
        ans[i] += 1
    print(*ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
