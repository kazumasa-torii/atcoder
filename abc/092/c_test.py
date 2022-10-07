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
6
-679 -2409 -3258 3095 -3291 -4462

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    moveCost = []
    tot = 0
    for i in range(1, len(a)):
        tot += abs(a[i] - a[i-1])
        moveCost.append(abs(a[i] - a[i-1]))
        # [3, 2, 6, 1]

    for i in range(1, len(a)-1):
        tmp = tot
        tmp -= moveCost[i]
        tmp -= moveCost[i-1]
        tmp += abs(a[i-1] - a[i+1])
        print(tmp)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
