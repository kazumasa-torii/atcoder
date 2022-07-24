"""
グラフ…。

BFSしたあとにDPする内容
意味合いとしては、スタートから各頂点まで行く最短経路を求めておきそこからゴール地点の通り数を調べるみたい
あんまり理解していないけどやっていることは、初歩的な気がする

1. グラフとしてデータ構造を持っておく
1. 0からスタートして各頂点
1.
1.
1.
1.
"""

import sys
from collections import deque
input = sys.stdin.readline

def main():
    INF = 100100010
    mod = 10 ** 9 + 7
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
    
    dp = [0] * n
    dp[0] = 1
    for v in vs:
        for u in maps[v]:
            if dist[u] == dist[v] + 1:
                dp[u] += dp[v]
                dp[u] %= mod
    print(dp[n-1])
    return

if __name__ == '__main__':
    main()
