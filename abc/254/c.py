"""
バブルソートの応用
変更できる距離で各値の位置が変更できるかグループ分けする
例
距離  : 2
list : [3, 4, 1, 3, 4]

あまりが０
[3, 1, 4]
あまりが１
[4, 3]
この各グループに関しては、入れ替えができるのでsortしておく

最後にグループを順番に取り出していきsortしておいたlistと照らし合わせる
"""
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    li = list(map(int, input().split()))

    amari = [[] for _ in range(K)]
    # 割ったあまりをグループ分けで管理
    for i, x in enumerate(li):
        amari[i % K].append(x)
    # sortしておく
    for i in range(K):
        amari[i].sort()

    cheng_li = [0] * N
    # sort しておいた値を各グループから前から順番に取り出していきlist化しておく
    for i in range(N):
        cheng_li[i] = amari[i % K][i // K]

    return cheng_li == sorted(li)

print('Yes' if main() else 'No')
