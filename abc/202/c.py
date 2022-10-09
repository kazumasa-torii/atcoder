"""

"""
import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda x: int(x) - 1, input().split()))
    a_dict = defaultdict(int)
    for i in range(10 ** 5):
        a_dict[i] = 0
    for i in A:
        a_dict[i] += 1
    ans = 0
    for i in C:
        if a_dict[B[i]]:
            ans += a_dict[B[i]]
    print(ans)
    return

main()
