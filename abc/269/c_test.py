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
11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
def main():
    n = int(input())
    a = []
    for i in range(60):
        if n&(1<<i):a.append(i)
    
    k = len(a)
    res = []
    for i in range(1<<k):
        cur = 0
        for j in range(k):
            if i & (1 <<j): cur |= 1 << a[j]
        res.append(cur)
    for i in res:
        print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
