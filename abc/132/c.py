import sys
from typing import List
input = sys.stdin.readline

def main():
    N = int(input())
    li = list(map(int, input().split()))
    li.sort()
    mid = int(N / 2)
    length = abs(li[mid-1] - li[mid])
    print(length)
    return

main()
