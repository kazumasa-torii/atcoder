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
from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda x: int(x) - 1, input().split()))
    a_dict = defaultdict(int)
    for i in range(10 ** 5):
        a_dict[i] = 0
    for i in A:
        a_dict[i] += 1
    ans = 0
    for i in C:
        if a_dict[B[i]]:
            ans += a_dict[B[i]]
    print(ans)
    return

main()
