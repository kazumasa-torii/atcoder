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
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(len(b)):
        if a[i] < b[i]:
            cnt += a[i]
            tmp = b[i] - a[i]
            if a[i+1] - tmp < 0:
                cnt += a[i+1]
                a[i+1] = 0
            else:
                cnt += tmp
                a[i+1] -= tmp

        else:
            cnt += b[i]
    print(cnt)
    return

main()
