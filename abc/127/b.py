import sys
from typing import List
input = sys.stdin.readline

def main():
    r, D, x = map(int, input().split())
    tmp = x
    for i in range(1, 11):
        ans = (r*tmp)-D
        print(ans)
        tmp = ans
    return

main()
