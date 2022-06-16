"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    X, A = map(int, input().split())
    print(0 if X < A else 10)
    return

main()
