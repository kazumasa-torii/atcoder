"""
三角形の公式
ただ中心点を見つけた後に計算した結果がどれを提出するかわからないので脱落…。
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    li = [list(map(int, input().split())) for _ in range(N)]
    root = []
    Ali = []
    for i in range(K):
        A[i] -= 1
        Ali.append(abs(li[A[i]][0]-li[A[i]][1]))
    target = A[Ali.index(min(Ali))]

    for j in range(N):
        if j == target:
            continue
        x = abs(li[target][0] - li[j][0])
        y = abs(li[target][1] - li[j][1])
        root.append((x ** 2 + y ** 2) ** 0.5)
    print(max(root))
    return

main()
