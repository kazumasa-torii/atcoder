"""

"""
import re
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 2 5
1 2
1 3
3 4
3 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def dfs(n):
        if memo[n]: return
        memo[n] = True
        if n == y:
            ans.append(n) 
            return True
        for next_n in g[n]:
            result = dfs(next_n)
            if result: 
                ans.append(n) 
                return True
        return False
    n, x, y = map(int, input().split())
    memo = [False] *  (n + 1)
    ans = []
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    dfs(x)
    print(*reversed(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
