"""
簡単のifelse
"""
import sys
from typing import List
input = sys.stdin.readline

def main():
    R, C = map(int,input().split())
    one, onetwo = map(int,input().split())
    two, twoone = map(int,input().split())
    if R == 1 and C == 1:
        print(one)
    elif R == 1 and C == 2:
        print(onetwo)
    elif R == 2 and C == 1:
        print(two)
    elif R == 2 and C == 2:
        print(twoone)
    return

main()
