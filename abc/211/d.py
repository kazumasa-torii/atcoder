import sys
from collections import deque
input = sys.stdin.readline

def main():
    INF = 1001001001
    n, m = map(int, input().split())
    maps = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        maps[a].append(b)
        maps[b].append(a)
    dist = [INF] * n
    q = deque()
    q.append(0)
    dist[0] = 0
    vs = []

    while q:
        v = q.popleft()
        vs.append(v)
        for u in maps[v]:
            if dist[u] != INF: continue
            dist[u] = dist[v] + 1
            q.append(u)
    
    dp = [int() for _ in range(n)]
    dp[0] = 1
    for v in vs:
        for u in maps[v]:
            if dist[u] == dist[v] + 1:
                dp[u] += dp[v]
    print(dp[n-1])
    return

if __name__ == '__main__':
    main()
