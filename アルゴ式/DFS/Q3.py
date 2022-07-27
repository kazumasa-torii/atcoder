import sys
import time
from io import StringIO

_INPUT = """\
3 6
1 2
0 2
1 0
2 1
2 0
0 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

sys.setrecursionlimit(3000)
def main():
    def dfs(v):
        if seen[v]: return
        ans.append(v)
        seen[v] = True
        for v2 in maps[v]:
            dfs(v2)
        return
    n, m = map(int, input().split())
    maps = [[] for _ in range(n)]
    seen = [False for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        maps[a].append(b)
    for i in range(n):
        maps[i].sort()
    ans = []
    dfs(0)
    print(*ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
