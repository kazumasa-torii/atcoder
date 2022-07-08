"""
listを作らずにどう数字の動きを作るのかが肝

1.使えない数字より少ない数字で使える数字の数を取得しlist化する
1.list化するときには、各使えない数字からindex数+1(0を使用しないため)引く
1.クエリが来たら上記のリストを二分探索する
1.二分探索した結果が0ならば使えない数字より小さい数字なので最大値を出力
1.上記以外ならば二分探索した結果の使えない数字と指定しているindex数を足し合わせる
1.足した数字から使える数字の数分差し引いて行き過ぎた分を差し引く
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = [A[i] - (i + 1) for i in range(N)]
    for _ in range(Q):
        K = int(input())
        i = bisect_left(S, K)
        if i == 0:
            print(K)
        else:
            print(A[i-1] + (K - S[i - 1]))
    return

if __name__ == '__main__':
    main()
