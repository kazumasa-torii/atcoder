import sys
import time
from io import StringIO

_INPUT = """\
    8 12
0 1
0 4
1 3
1 7
2 0
2 4
3 2
5 3
5 4
5 6
6 3
6 7

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
    for _ in range(m):
        a, b = map(int, input().split())
        maps[a].append(b)

    seen = [False for _ in range(n)]
    ans = []

    dfs(0)
    print(n-len(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
