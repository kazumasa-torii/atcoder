"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    ans = A + B
    ans /= 2
    print(int(ans) if ans.is_integer() else 'IMPOSSIBLE')
    return

main()
