"""
bfsで値が自分の都市含めどこまで行けるか試していく
すべての都市でbfsを行い行ける都市を足していく

考察はあっていた
だが実装ができていなかったのでbfsの実装やるようにする
"""

import sys
from collections import deque
input = sys.stdin.readline
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
