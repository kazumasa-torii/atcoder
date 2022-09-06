"""
累積和を使用した計算の高速化
差分を生かした計算方法
の二点が大事

1. 累積和を作成
1. 現時点での計算を行う
1. 内容をlistとして保持する
1. 一番最後の計算した内容から以下の公式を使って計算結果を求めていく
1. s1 - ((a + b + c + d) - (e * m))
1. 最後に求めた数から各項目を一度ずつ引いて追加する数字を掛け算した状態で追加する
1. これにより各項目に掛け算した内容を引いていき順番をずらすことができる
"""

import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    now = 0
    si = []
    for i in range(m): now += a[i]*(i+1)
    si.append(now)
    for i in range(n-m):
        si.append(si[-1] - ((acc[i+m] - acc[i] )- (a[i+m] * m)))
    print(max(si))
    return

if __name__ == '__main__':
    main()