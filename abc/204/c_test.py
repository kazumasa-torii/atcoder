"""

"""
import sys
import time
from io import StringIO
from typing import List



_INPUT = """\
3 3
1 2
2 3
3 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
sys.setrecursionlimit(50000)

def main():
    def bfs(idx):
        seen = [False] * N
        seen[idx] = True
        que = deque([idx])
        while que:
            u = que.popleft()
            for v in li[u]:
                if seen[v]:
                    continue
                seen[v] = True
                que.append(v)
        return seen.count(True)

    N, M = map(int, input().split())
    li = [[] for _ in range(N)]
    for _ in range(M):
        x, y = (x - 1 for x in map(int, input().split()))
        li[x].append(y)
    ans = 0

    for i in range(N):
        ans += bfs(i)
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
