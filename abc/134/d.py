"""
後ろからボールの個数を確定していって条件に合致しているか計算しつつ対応する
"""
import sys
from typing import List
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))

b = [0 for i in range(N)]

# ボールの個数を数える
def check(i):
    cnt = 0
    n = i
    while n <= N:
        cnt += b[n-1]
        n += i
    return cnt

def main():
    for i in range(N-1, -1 ,-1):
        # iの倍数が書かれている箱に対してボールの個数の和を2で割ったあまり
        if (a[i] + check(i+1))%2 == 1:
            b[i] = 1

    ans = []
    cnt = 0
    # ボールを何個入れたか個数数えて入れた場所をansに突っ込む
    for i in range(N):
        if b[i] == 1:
            cnt += 1
            ans.append(i+1)

    print(cnt)
    L = [str(int(i)) for i in ans]
    print(' '.join(L))

    return 0

main()
