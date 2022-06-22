"""
for 一つで考える
"""
import sys
from math import ceil
from typing import List
input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    print(ceil(N/(D*2+1)))
    return

main()
