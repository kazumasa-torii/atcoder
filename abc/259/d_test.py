"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
4
0 -2 3 3
0 0 2
2 0 2
2 3 1
-3 3 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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

def main():
    def is_cross(xi,yi,ri,xj,yj,rj):
        d = (xi-xj)**2+(yi-yj)**2
        if (ri-rj)**2 <= d <= (ri+rj)**2:
            return True
        else:
            return False

    n = int(input())
    sx, sy, gx, gy = map(int,input().split())

    xyr = [(sx,sy,0), (gx,gy,0)]
    for i in range(n):
        x, y, r = map(int, input().split())
        xyr.append((x, y, r))

    uf = UnionFind(n+2)

    for i in range(n+2):
        for j in range(i+1, n+2):
            xi, yi, ri = xyr[i]
            xj, yj, rj = xyr[j]
            if is_cross(xi, yi, ri, xj, yj, rj):
                uf.unite(i, j)

    if uf.is_same(0, 1):
        print('Yes')
    else:
        print('No')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
