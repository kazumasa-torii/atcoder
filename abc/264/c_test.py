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
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    ah, aw = map(int, input().split())
    a = dict()
    for _ in range(ah):
        tmp = list(map(int, input().split()))
        for i in tmp:
            if not a.get(i):
                a[i] = 1
            else:
                a[i] += 1
    bh, bw = map(int, input().split())
    b = dict()
    for _ in range(bh):
        tmp = list(map(int, input().split()))
        for i in tmp:
            if not b.get(i):
                b[i] = 1
            else:
                b[i] += 1

    for _, key in enumerate(b):
        if not a.get(key, False):exit(print('No'))
        if a[key] < b[key]:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
