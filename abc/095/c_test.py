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
1500 2000 500 90000 100000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, x, y = map(int, input().split())
    ac = min(c*2, a+b)
    ans = 0
    while x > 0 and y > 0:
        ans += ac
        x -= 1
        y -= 1
    if x > 0:ans += min(ac, a) * x
    else:ans += min(ac, b) * y
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
