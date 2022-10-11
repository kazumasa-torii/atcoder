import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from math import gcd
def main():
    n = int(input())
    t = [int(input()) for _ in range(n)]
    ans = t[0]
    for i in range(1,n):
        ans = ans * t[i] // gcd(ans, t[i])
    print(ans)
    return

if __name__ == '__main__':
    main()