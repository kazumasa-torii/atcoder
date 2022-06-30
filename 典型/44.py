"""
見かけ上の変化をメモ
問題文通りに記載しても計算量が追いつかないときは、どこかを小さくできる
言い換え大事

1. シフトする数を初期化する
1. tが2のときはシフトする数を1増やす
1. tが1のときは、xとyを1とシフト分減らして負になればnプラスして正の整数にする
1. そしてxとyの数字を入れ替える
1. tが3のときは、xを1とシフト分減らして負になればnプラスして正の整数にする
"""

import sys
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    a = list(map(int,input().split()))
    shft = 0
    for _ in range(q):
        t, x, y = map(int, input().split())
        ido = 1 + shft
        if t == 1:
            x -= ido
            y -= ido
            while x < 0:
                x += n
            while y < 0:
                y += n
            tmp = a[x]
            a[x] = a[y]
            a[y] = tmp
            continue
        if t == 2:
            shft += 1
            continue
        if t == 3:
            x -= ido
            while x < 0:
                x += n
            print(a[x])

if __name__ == "__main__":
    main()
