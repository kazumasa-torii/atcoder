"""
1.二分探索で中間地点を取得
1.それを使用して何個に分割できるかを判定
1.K個以上できればrightを中間地点に変更して
1.K個以上できなければleftを中間地点に変更する
1.中間地点が縮まれば大体大きさが同じ長さが取得できる

...正直二分探索でこんなことができるのでびっくり
...まだまだ理解していないので今後もう少し考えてみる
"""

import sys
import math
input = sys.stdin.readline

# 最大何個の長さM以上のピースに分割できるか判定
def solve(mid: int) -> bool:
    cnt: int = 0
    pre: int = 0
    for i in range(N):
        if A[i] - pre >= mid and L - A[i] >= mid:
            cnt += 1
            pre = A[i]
    if cnt >= K: return True
    return False


def main():
    left: int = -1
    right: int = L + 1
    # 二分探索
    while right - left > 1:
        mid: int = math.ceil(left + (right -left) / 2)
        if solve(mid) == False: right = mid
        else: left = mid

    print(left)

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
main()
