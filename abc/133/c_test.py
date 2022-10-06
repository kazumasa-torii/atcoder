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

_INPUT = """\
4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 2019
    l, r = map(int, input().split())
    ans = int(1e19)
    if r > l+mod: exit(print((0)))
    l %= mod
    r %= mod
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            ans = min(ans, (i*j)%mod)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
