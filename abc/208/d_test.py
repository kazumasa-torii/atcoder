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

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, M = map(int, input().split())
    ABC = map(int, input().split())
    d = [[1 << 60] * N for _ in range(N)]

    for i in range(N):
        d[i][i] = 0
    
    for a, b, c in zip(ABC, ABC, ABC):
        d[a-1][b-1] = c
    ans = 0
    for k in range(N):
        nxt = [0 * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if nxt[i][j] < 1 << 59:
                    ans += nxt[i][j]
        d = nxt
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
