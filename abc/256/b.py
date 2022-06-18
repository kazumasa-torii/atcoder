"""
for 一つで考える
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    li = []
    for i in range(N):
        li.append(0)
        for j in range(len(li)):
            li[j] += A[i]
    ans = 0
    for i in li:
        if i > 4:
            ans += 1

    print(ans)
    return

main()
