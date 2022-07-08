"""
queにわたす時にどうやって渡すのかが不明瞭だったので理解できた。
このように実装すれば確かに動いていくな…。
後は計算量を今後落とすような内容を考える

"""

import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6 7
0 1
0 5
1 3
1 5
2 3
3 4
4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    N, M = map(int, input().split())
    frend = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        frend[x].append(y)
        frend[y].append(x)

    dist = [-1] * N
    dist[0] = 0

    que = deque()
    que.append(0)

    while que:
        v = que.popleft()

        # listで入っていた内容をqueにわたす必要もあるのでiterにする
        for next_v in frend[v]:
            if dist[next_v] != -1:
                continue

            dist[next_v] = dist[v] + 1
            que.append(next_v)

    print(max(dist))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
