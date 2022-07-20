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
9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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
    print(f'[Sec] {str(time.time() - StartTime)}')
