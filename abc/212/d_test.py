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
5
1 3
1 5
3
2 2
3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import heapq
def main():
    q = int(input())
    hq = []
    s = 0
    heapq.heapify(hq)
    for _ in range(q):
        li = list(map(int, input().split()))
        if li[0] == 1:
            heapq.heappush(hq, li[1] - s)
        elif li[0] == 2:
            s += li[1]
        elif li[0] == 3:
            tmp = heapq.heappop(hq)
            print(tmp+s)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
