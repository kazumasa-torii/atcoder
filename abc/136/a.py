import sys
from typing import List
input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())
    print(b+c-a if b+c-a > 0 else 0)
    return

main()
