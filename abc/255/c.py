import sys
from typing import List
input = sys.stdin.readline
"""
A 初項
D 公差
N 項数

1. 公差が0以下の場合は初項を予め求めておいて右からの配列に直し公差を正の整数にする
1. Xから予め初項を引いておく
1. DとXが1以上であればX//Dを行い公差でどの程度割れるのか把握する
1. 条件分岐させ答えを出力

肝は条件を把握してコーナーケースも十分に考慮すること
あとは負の整数を正の整数にして考慮する条件を少なくする
"""
def main():
    X, A, D, N = map(int,input().split())
    if D < 0:
        A = A+D*(N-1)
        D *= -1
    
    X -= A
    ans = abs(X)
    if D > 0 and X > 0:
        index = X//D
        # 項数の最大値より小さいため一番近い数値を取得する
        if index < N-1:
            ans = min(X-index*D, (index+1)*D-X)
        # 項数の最大値より大きいため項数の一番最後の値からXを引く
        else:
            ans = X-(N-1)*D
    print(ans)

    return

main()
