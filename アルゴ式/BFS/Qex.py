"""
ちょっといまいち理解できないので問題を再度解いてみる
"""

import sys
import time
from io import StringIO

_INPUT = """\
3 3
0 2
1 0
2 1
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    # 各頂点の出次数を管理する配列
    deg = [0] * n

    # グラフの辺を受け取り、出次数を更新していく

    for i in range(m):
        a, b = map(int, input().split())
        # グラフ作成
        g[a].append(b)
        # 頂点 B の出次数を増やす
        deg[b] += 1

    q = deque()
    # 入次数が 0 であるようなソースをキューに入れる
    num = 0  # 除去された頂点の個数

    for v in range(n):
        if deg[v] == 0:
            q.append(v)
            num += 1

    while q:
        v = q.popleft()
        # 頂点 v に繋がる頂点 v2 の出次数を減らす
        for v2 in g[v]:
            deg[v2] -= 1

            # もし v2 が新たにソースになるならキューに入れる
            if deg[v2] == 0:
                q.append(v2)
                num += 1
    # すべての頂点が除去されたなら Yes
    print("Yes" if num == n else "No")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
