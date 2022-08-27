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
0 0
1 1
-1 0
1 -1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

import math
def main():
    li = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(2):
            if li[i][j] < 0:li[i][j] = -li[i][j]
    flag = True

    def angle(pt1, pt2, pt0) -> float:
        dx1 = float(pt1[0,0] - pt0[0,0])
        dy1 = float(pt1[0,1] - pt0[0,1])
        dx2 = float(pt2[0,0] - pt0[0,0])
        dy2 = float(pt2[0,1] - pt0[0,1])
        v = math.sqrt((dx1*dx1 + dy1*dy1)*(dx2*dx2 + dy2*dy2) )
        return (dx1*dx2 + dy1*dy2)/ v

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
