"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6
-1 -1
0 1
0 2
1 0
1 2
2 0

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    class UnionFind:
        """0-indexed"""

        def __init__(self, n):
            self.n = n
            self.parent = [-1] * n
            self.__group_count = n

        def unite(self, x, y) -> bool:
            """xとyをマージ"""
            x = self.root(x)
            y = self.root(y)

            if x == y:
                return False

            self.__group_count -= 1

            if self.parent[x] > self.parent[y]:
                x, y = y, x

            self.parent[x] += self.parent[y]
            self.parent[y] = x

            return True

        def is_same(self, x, y) -> bool:
            """xとyが同じ連結成分か判定"""
            return self.root(x) == self.root(y)

        def root(self, x) -> int:
            """xの根を取得"""
            xc = x
            while self.parent[x] >= 0:
                x = self.parent[x]
            while xc != x:
                self.parent[xc], xc = x, self.parent[xc]
            return x

        def size(self, x) -> int:
            """xが属する連結成分のサイズを取得"""
            return -self.parent[self.root(x)]

        def all_sizes(self) -> List[int]:
            """全連結成分のサイズのリストを取得 O(N)"""
            sizes = []
            for i in range(self.n):
                size = self.parent[i]
                if size < 0:
                    sizes.append(-size)
            return sizes

        def groups(self) -> List[List[int]]:
            """全連結成分の内容のリストを取得 O(N・α(N))"""
            groups = dict()
            for i in range(self.n):
                p = self.root(i)
                if not groups.get(p):
                    groups[p] = []
                groups[p].append(i)
            return list(groups.values())

        @property
        def group_count(self) -> int:
            """連結成分の数を取得 O(1)"""
            return self.__group_count
    dx = [-1, -1, 0, 0, 1, 1]
    dy = [-1, 0, -1, 1, 0, 1]
    memo = [[0] * 2010 for _ in range(2010)]

    n = int(input())
    uf = UnionFind(n)
    x = [0] * (n + 1)
    y = [0] * (n + 1)

    for i in range(n):
        x[i], y[i] = map(int, input().split())
        x[i], y[i] = x[i] + 1005, y[i] + 1005
        memo[x[i]][y[i]] = i
    for i in range(n):
        for k in range(6):
            nx = x[i] + dx[k]
            ny = y[i] + dy[k]
            if memo[nx][ny] > 0:uf.unite(i, memo[nx][ny])
    print(uf.group_count)

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
