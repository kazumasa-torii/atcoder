"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))
    return

main()
