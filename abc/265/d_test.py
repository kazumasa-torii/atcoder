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
10 5 7 5
1 3 2 2 2 3 1 4 3 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    acc = set(acc)

    for x in acc:
        if x+p in acc and x+p+q in acc and  x+p+q+r in acc: exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()

    print(f'[Sec] {str(time.time() - StartTime)}')
