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
5 5 10
2 3
4 10
5 10
6 9
2 9
4 8
1 7
3 6
8 10
1 8
6
3
5
8
10
2
7

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
    N, M, E = map(int, input().split())
    edge = []
    for i in range(E):
        u, v = map(int, input().split())
        # N以上なら発電所なので、すべてNに置き換える
        edge.append((min(u - 1, N), min(v - 1, N)))

    Q = int(input())
    X = []
    # Q個のイベントの後、残っている辺をつなげる
    connected = [True] * E
    for i in range(Q):
        x = int(input())
        x -= 1
        connected[x] = False
        X.append(x)

    uf = UnionFind(N + 1)
    for i in range(E):
        if connected[i]:  # 切れてない辺なら接続
            u, v = edge[i]
            uf.unite(u, v)

    ans = [0] * Q  # 逆再生します
    for i in reversed(range(Q)):
        ans[i] = uf.size(N) - 1
        u, v = edge[X[i]]
        uf.unite(u, v)  # 逆再生なので、答えを求めてから接続します
    print(*ans, sep='\n')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
