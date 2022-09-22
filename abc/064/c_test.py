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
1100 1900 2800 3200 3200

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [False] * 8
    ex = 0
    for i in a:
        if 1 <= i <= 399:ans[0] = True
        elif 400 <= i <= 799: ans[1] = True
        elif 800 <= i <= 1199: ans[2] = True
        elif 1200 <= i <= 1599: ans[3] = True
        elif 1600 <= i <= 1999: ans[4] = True
        elif 2000 <= i <= 2399: ans[5] = True
        elif 2400 <= i <= 2799: ans[6] = True
        elif 2800 <= i <= 3199: ans[7] = True
        elif 3200 <= i: ex += 1
    print(max(1, sum(ans)), sum(ans) + ex)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
