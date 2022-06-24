"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))
    return

main()
