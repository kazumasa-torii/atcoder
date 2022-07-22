"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法,鳩の巣原理

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
4 5
2 4
1 2
2 3
1 3
3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
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
    print(f'[Sec] {str(time.time() - StartTime)}')
