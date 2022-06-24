"""
for 一つで考える
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    k, x = map(int, input().split())
    ans = []
    for i in range(x-(k-1), x+(k)):
        ans.append(i)
    print(*ans)
    return

main()
