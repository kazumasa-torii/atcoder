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

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    acc = [0]
    tmp = a[0]
    for i in range(1, n):
        if a[i] <= tmp: acc.append(acc[-1] + 1)
        else:acc.append(0)
        tmp = a[i]
    print(max(acc))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
