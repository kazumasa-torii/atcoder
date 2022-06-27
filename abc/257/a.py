"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    for i in al:
        for _ in range(n):
            index += 1
            if x == index:
                print(i)
                sys.exit()
    return

main()
