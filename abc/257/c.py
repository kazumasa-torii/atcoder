"""
肝はデータの持ち方
ここがあんまり想像できていなかったのでできなかった可能性あり
データ構造の持ち方理解する

1. 一つ区切りを入れる問題に変更
1. 最初に区切りが一番左に来ている状態での正解数を取得（すべての大人なので大人の場合はどうなるか判定）
1. その後区切りを右に動かしていくと子供の数が増えていく
1. 条件分岐で区切りを右に動かした時に子供だったら＋ 大人だったらーを行いそれを以前の区切りと比較する
1. 最終的に大きかったサイズのものでOK
"""
import sys
from typing import List
from operator import itemgetter
input = sys.stdin.readline

def main():
    n = int(input())
    s = input().strip()
    li = []
    index = 0
    ans = 0
    for i in map(int, input().split()):
        li.append([i, int(s[index])])
        if int(s[index]):
          ans += 1
        index += 1
    li.sort(key=itemgetter(0))
    x = ans
    for i in range(n):
        if li[i][1]:
            x -= 1
        else:
            x += 1
        ans = max(x, ans)
    print(ans)
    return

main()
