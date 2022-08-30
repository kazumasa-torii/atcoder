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
1 0
1 1
0 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    # 角ABC（角度は時計回りに測る）が180度未満なら true
    def angle(a, b, c):
        return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) > 0

    ax, ay, bx, by, cx, cy, dx, dy = map(int, open(0).read().split())
    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)
    d = (dx, dy)

    if angle(b, a, d) and angle(c, b, a) and angle(d, c, b) and angle(a, d, c):
        print('Yes')
    else:
        print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
