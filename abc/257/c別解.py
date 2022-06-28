"""
肝はデータの持ち方
ここがあんまり想像できていなかったのでできなかった可能性あり
データ構造の持ち方理解する

1. 子供と大人を分ける
1. 各内容をsortしておき長さも取得させる
1. 片方が0ならば最大値はもう片方になるのでその時点でreturnさせる
1. そうじゃないならば大人の数(x)を一つずつ見ていきから子供のlistを二分探索させてx以下の個数を算出
1. 子供の個数と大人のlistの長さから現在の数字以下の箇所を間違いと判定させて答えから引く
1. 答え同士を比較して大きい数字を最終答えとして出力させる
"""
import sys
from bisect import bisect_left
from typing import List
input = sys.stdin.readline

def main():
    n = int(input())
    s = input().strip()
    li = list(map(int, input().split()))

    A = []
    B = []

    for i in range(n):
        if s[i] == "1":
            A.append(li[i])
        else:
            B.append(li[i])
    A.sort()
    B.sort()

    x = len(B)
    l = len(A)

    for i in range(l):
        a = bisect_left(B,A[i])
        x = max(x, a+l-i)

    print(x)
    return

main()
