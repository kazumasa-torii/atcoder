import sys
from typing import List
input = sys.stdin.readline

def main():
    X, A, D, N = map(int,input().split())
    X -= A
    tmp = X / D
    if tmp < 0:
        tmp *= -1
    ans = tmp * D
    if ans < 0:
        ans *= -1
    print(int(ans))
    return

main()
