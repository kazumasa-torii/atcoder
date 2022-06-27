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
from typing import List
from operator import itemgetter
input = sys.stdin.readline

def main():
    # n = int(input())
    # s = input().strip()
    n = 5
    s = '10101'
    # li = []
    # index = 0
    # for i in map(int, input().split()):
    #     tmp = [0, 0]
    #     if int(s[index]):
    #         tmp[0] += 1
    #     else:
    #         tmp[1] += 1
    #     li.append([i, tmp])
    #     index += 1
    li = [[60, [1, 0]], [45, [0, 1]], [30, [1, 0]], [40, [0, 1]], [80, [1, 0]]]
    li.sort(key=itemgetter(0))
    print(li)
    return

main()
