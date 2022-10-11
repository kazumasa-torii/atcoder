"""

"""
import sys
import time
from io import StringIO
from typing import List

from soupsieve import select_one


_INPUT = """\
8
1 5 3 2 5 2 3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
class UnionFind:
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
    N = int(input())
    A = list(map(int, input().split()))

    def solve():
        # Const = 2 * 10 ** 5 + 5
        Const = 10
        uf = UnionFind(Const)
        l = N // 2
        r = N // 2
        if N % 2 != 0:
            r += 1

        first = A[:l]
        second = A[r:][::-1]

        for x, y in zip(first, second):
            uf.unite(x, y)
        ans = 0
        for x in uf.all_sizes():
            ans += x - 1

        return ans

    print(solve())
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
