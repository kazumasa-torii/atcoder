"""
for 一つで考える
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    N: int = int(input())
    li: List[int] = list(map(int, input().split()))
    ans = 10 ** 5
    for i in range(N):
        S_one: List[int] = []
        S_two: List[int] = []
        for j in range(N):
            if i < j:
                S_two.append(li[j])
            else:
                S_one.append(li[j])
        ans = min(ans, abs(sum(S_two) - sum(S_one)))
    print(ans)
    return

main()
