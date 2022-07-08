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
input = sys.stdin.readline

def main():
    N = int(input())
    li = list(map(int, input().split()))
    li.sort()
    if N <= 2:
        print(max(li))
        return
    sum_num = 0
    if sum(li) % 2 != 0:
        sum_num = sum(li) // 2 + 1
    else:
        sum_num = sum(li) // 2
    print(sum_num)
    return

main()
