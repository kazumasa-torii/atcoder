"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法

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
from copy import deepcopy
from typing import List
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    sort_a = deepcopy(A)
    sort_a.sort()
    max_a = sort_a[-1]
    max_a_index = A.index(max_a)
    two_max_a = sort_a[-2]
    for i in range(N):
        if i == max_a_index:
            print(two_max_a)
            continue
        print(max_a)

    return

main()
