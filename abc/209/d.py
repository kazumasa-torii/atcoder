"""
グラフで木としてデータ構造を持つように考える

1. グラフの木として考える
1. グラフを用意してdfsで頂点から根までの長さを取得する
1. そしてその長さを取得したらLCA(最近共通祖先)を取得
1. 頂点から根までの長さを取得してLCAまでの距離を2回引いてmod2を取る
（結局mod2なのでLCAまでの距離は引かなくてもOK）
1. modを取った距離が偶数ならTownで奇数ならRoadを出力する
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    def dfs(v: int, _dep = 0, p=-1):
        dep[v] = _dep
        for u in to[v]:
            if u == p: continue
            dfs(u, _dep+1, v)
        return
    
    n, q = map(int, input().split())
    to = [[] for _ in range(n)]
    dep = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    dfs(0)
    for qi in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        ans = (dep[c]+dep[d])%2
        print('Town' if ans == 0 else 'Road')

    return

if __name__ == '__main__':
    main()
