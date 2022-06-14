"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    P, R, Q = map(int, input().split())
    print(min(P+R, P+Q, Q+R))
    return

main()
