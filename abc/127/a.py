"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    if A <= 12:
        B /= 2
    elif A <= 5:
        B = 0
    else:
        pass
    print(int(B))
    return

main()
