"""
BFSということはわかったが実装までたどり着けない…。
まだまだなのでもっと勉強
"""
import sys
input = sys.stdin.readline
from itertools import product
from collections import deque
def main():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    mov1 = tuple((r, c) for r, c in zip(dr, dc))
    mov3 = tuple((r, c) for r, c in product(range(-2, 3), repeat=2) if 1 <= abs(r) + abs(c) <= 3)

    def solve():
        dist = [[10 ** 7] * W for _ in range(H)]
        dist[0][0] = 0
        deq = deque()
        deq.appendleft((0, 0, 0))

        while deq:
            cost, r, c = deq.popleft()

            for ar, ac in mov1:
                nr, nc = r + ar, c + ac
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == "." and cost < dist[nr][nc]:
                        dist[nr][nc] = cost
                        deq.appendleft((cost, nr, nc))

            for ar, ac in mov3:
                nr, nc = r + ar, c + ac
                if 0 <= nr < H and 0 <= nc < W:
                    if cost + 1 < dist[nr][nc]:
                        dist[nr][nc] = cost + 1
                        deq.append((cost + 1, nr, nc))
        return dist[-1][-1]

    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        _r = input()
        grid.append(_r)

    print(solve())


if __name__ == '__main__':
    main()
