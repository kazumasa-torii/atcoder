"""
尺取法


コンビネーションの計算（階乗の計算を早くおこなったもの）
N*(N+1)/2
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    num_sum: int = 0
    length: int = 0
    ans: float = 0
    for i in range(N):
        while length < N and num_sum+A[length] < K:
            num_sum += A[length]
            length += 1
        # 何通り行けたか記載
        # 前から順番に1つの数まで,2つの数まで,3つの数までみたいに計算
        ans += length - i
        # 先頭の数字分削除してスタートをずらす
        num_sum -= A[i]
    ans = N*(N+1)/2 - ans
    print(int(ans))
    return

main()
