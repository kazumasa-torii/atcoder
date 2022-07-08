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
